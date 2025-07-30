import logging
import logging.handlers
from logging.config import dictConfig
from flask import current_app
import os


class Logger():
    def __init__(self, name='Logger'):

        dictConfig({
            'version': 1,
            'formatters': {
                'default': {
                    'format': '[%(asctime)s] %(levelname)s in module %(module)s: %(message)s',
                },
                'psr3': {
                    'format': '[%(asctime)s] %(levelname)s in %(name)s: %(message)s',
                    'datefmt': '%Y-%m-%dT%H:%M:%S%z %Z'
                }
            },
            'handlers': {
                'wsgi': {
                    'class': 'logging.StreamHandler',
                    'stream': 'ext://flask.logging.wsgi_errors_stream',
                    'level': 'DEBUG',
                    'formatter': 'psr3'
                },
                'file': {
                    'class': 'logging.handlers.RotatingFileHandler',
                    'filename': 'app/logs/flask.log',
                    'formatter': 'psr3',
                    'level': 'INFO',
                    'maxBytes': 1024*1024,
                    'backupCount': 7
                },
            },
            'root': {
                'level': 'DEBUG',
                'handlers': ['wsgi', 'file']
            }
        })

        loggerName = name if isinstance(
            name, str) else name.__module__ + '.' + name.__name__

        self.logger = logging.getLogger(loggerName)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def exteption(self, message):
        self.logger.error(message, exc_info=True)

    def critical(self, message):
        self.logger.critical(message)
