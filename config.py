class Config():
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:Royal12@localhost/blogs'

    SECRET_KEY ='secret'

class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG =True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}