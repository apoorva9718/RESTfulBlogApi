import os

class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = "secretkey12234356677"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:apoorva@localhost/blog_api_db"

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    JWT_SECRET_KEY = "secretkey12234356677"

app_config = {
    'development': Development,
    'production': Production,
}