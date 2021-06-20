import os
class Config():
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:Royal12@localhost/blogs'
    BASE_URL='http://quotes.stormconsultancy.co.uk/random.json'

    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    #Simplemde configuration
    SECRET_KEY ='secret'
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG =True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}