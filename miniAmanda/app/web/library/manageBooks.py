from flask import jsonify
from . import library
from web.transport import pushMessage

@library.route('/search')
def search():
	message = {
		'user': 'varadarajan-a',
		'dob': '28 April 1986'
	}
	t = pushMessage.Transport('amqp://amqp', 5672)
	resp = t(message)
	return jsonify({"response": resp})