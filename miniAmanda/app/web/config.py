import os

class Config:
	DEBUG = False
	TESTING = False
	DATABASE_URI = 'sqlite:///:memory:'
	AMQP_URI = os.getenv('AMQP_URI')

class DevelopmentConfig(Config):
	DEBUG = True


class ProductionConfig(Config):
	pass


class TestingConfig(Config):
	pass


config = eval(os.getenv('ENV', 'DevelopmentConfig'))