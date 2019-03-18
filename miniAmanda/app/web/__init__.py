from flask import Flask, jsonify
from .config import config
from .transport import pushMessage
from .library import library

def create_app(config):
	app = Flask(__name__)
	app.config.from_object(config)
	app.register_blueprint(library)
	return app

app = create_app(config)
