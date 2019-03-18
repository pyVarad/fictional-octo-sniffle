from flask import Flask, jsonify
from .config import config
from .transport import pushMessage

def create_app(config):
	app = Flask(__name__)
	app.config.from_object(config)
	return app

app = create_app(config)

@app.route('/')
def index():
	message = {
		'user': 'varadarajan-a',
		'dob': '28 April 1986'
	}
	t = pushMessage.Transport('amqp://amqp', 5672)
	resp = t(message)
	return jsonify({"response": resp})