import os
from logging.config import dictConfig


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 's1dfvx24c2vtwe84fcsdfwe'


CREATE_PAYMENT_LOG_MESSAGE = 'Try to create payment with {} protocol: ' \
                             'amount: {}, currency: {}, shop_order_id: {}, timeline: {}, ' \
                             'description: {}'

dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s.%(funcName)s Line %(lineno)s: %(message)s',
        }},
        'handlers': {'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'filename': 'logging.log',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['file']
        }
    })
