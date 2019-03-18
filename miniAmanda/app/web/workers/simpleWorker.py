from __future__ import absolute_import, unicode_literals

from kombu import Connection, Queue
from kombu.mixins import ConsumerProducerMixin

queue = Queue('logging')

class Worker(ConsumerProducerMixin):
	def __init__(self, connection):
		self.connection = connection

	def get_consumers(self, Consumer, channel):
		print("I am triggered")
		return [Consumer(
			queues=[queue],
			on_message=self.on_request,
			accept={'application/json'},
			prefetch_count=1,
		)]

	def on_request(self, message):
		result = "Recieved Message from {0}".format(message.payload['user'])
		print(message.payload)

		self.producer.publish(
			{'result': result},
			exchange='', 
			routing_key=message.properties['reply_to'],
			correlation_id=message.properties['correlation_id'],
			serializer='json',
			retry=True,
		)
		message.ack()


def start_worker(broker_url):
    connection = Connection(broker_url)
    print(' [x] Awaiting RPC requests')
    worker = Worker(connection)
    worker.run()


if __name__ == '__main__':
    try:
        start_worker('amqp://amqp:5672')
    except KeyboardInterrupt:
        pass