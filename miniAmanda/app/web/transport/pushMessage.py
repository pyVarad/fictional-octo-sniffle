from kombu import Connection, Exchange, Producer, Queue, uuid, Consumer


class Transport(object):
	def __init__(self, host, port):
		self._host = host
		self._port = port
		self._uri = self._host + ':' + str(self._port)
		self._callbackQueue = Queue(uuid(), exclusive=True, auto_delete=True)

	def _publish(self, msg={}):
		with Connection(self._uri) as connection:
			with connection.channel() as channel:
				exchange = Exchange('Logging', type='topic', channel=channel)
				Producer(exchange=exchange, channel=channel).publish(
					body=msg, 
					routing_key='log'
				)

	def on_response(self, msg):
		if msg.properties['correlation_id'] == self.correlation_id:
			self.response = msg
			print(msg.payload)

	def _publishRPC(self, msg={}):
		self.response = None
		self.correlation_id = uuid()
		self.connection = Connection(self._uri)

		exchange = Exchange('Logging', type='topic', channel=self.connection.channel())
		with Producer(self.connection) as producer:
			producer.publish(
				body=msg,
				exchange=exchange,
				routing_key='log',
				declare=[self._callbackQueue],
				correlation_id=self.correlation_id,
				reply_to=self._callbackQueue.name
			)

		with Consumer(channel=self.connection.channel(), 
			on_message=self.on_response,
			queues=[self._callbackQueue], no_ack=True):
			while self.response is None:
				self.connection.drain_events()

		print(self.response.payload['result'])
		return self.response.payload['result']

	def __call__(self, msg):
		return self._publishRPC(msg)