import os

class Config:
	DEBUG = False
	TESTING = False
	DATABASE_URI = 'sqlite:///:memory:'
	AMQP_URI = os.getenv('AMQP_URI')

class DevelopmentConfig(Config):
	DEBUG = True
	MONGODB_DB = 'project_1'
	MONGODB_HOST = 'mongo'
	MONGODB_PORT = 27017
	MONGODB_USERNAME = 'root'
	MONGODB_PASSWORD = 'example'


class ProductionConfig(Config):
	pass


class TestingConfig(Config):
	pass


config = eval(os.getenv('ENV', 'DevelopmentConfig'))