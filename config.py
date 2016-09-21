import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
        'haohaoxuexitiantianxiangshang'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
    #     os.path.join(basedir, 'data-dev.sqlite')
    SQLALCHEMY_DATABASE_URI = \
        'mysql+pymysql://lolhfdev:lolhfdev@localhost/lolhfdev'


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = \
        'mysql+pymysql://lolhftest:lolhftest@localhost/lolhftest'


class PrdConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''


config = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': PrdConfig,
    'default': DevConfig
}
