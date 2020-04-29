import os # this will help the application work on various operating systems

class Config:
    '''
    Parent class for general configuration
    '''
    OURCES_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
   	ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'

class ProdConfig(Config):
    '''
    Production stage configuration
    '''
    pass

class DevConfig(Config):
    '''
    development stage configration
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}