import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 's1dfvx24c2vtwe84fcsdfwe'