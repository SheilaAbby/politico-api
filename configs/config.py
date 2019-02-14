""" politico-app configurations """

import os


class Config(object):
    """
    main config class
    """
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    """
    configurations for development env
    """
    DEBUG = True


class TestingConfig(Config):
    """
    Testing env configs
    """
    TESTING = True
    DEBUG = True


class StagingConfig(Config):
    """
    configs for staging app
    """
    DEBUG = True


class ProductionConfig(Config):
    """
    Config settings for production
    """
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}

