import os
from flask import jsonify, request
from . import library
from web.transport import pushMessage

@library.route('/search', methods=['GET', 'POST'])
def search():
	if request.method == "POST":
		message = request.get_json()
		## REPLACE WITH SESSION IN FUTURE.
		message.update({'user': os.getenv('LOGNAME')})
		t = pushMessage.Transport('amqp://amqp', 5672)
		resp = t(message)
		return jsonify({"response": resp})
	else:
		return jsonify({})

@library.route('/books/add', methods=['POST'])
def addBook():
	info = request.get_json()
	## REPLACE WITH SESSION IN FUTURE.
	message = request.get_json()
	message.update(
		{'user': os.getenv('LOGNAME')}
	)
	t = pushMessage.Transport('amqp://amqp', 5672)
	return None
