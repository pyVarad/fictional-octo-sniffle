from flask import Flask, jsonify
from .config import config
from .transport import pushMessage
from .library import library
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface


def create_app(config):
	app = Flask(__name__)
	app.config.from_object(config)
	app.register_blueprint(library)
	return app

app = create_app(config)
db = MongoEngine()
db.init_app(app)
app.session_interface = MongoEngineSessionInterface(db)

@app.route('/')
def index():
	return jsonify({'greeting': 'Welcome Guest.'})
