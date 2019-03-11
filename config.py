class Config:
    SECRET_KEY = 'hard to guess'
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:1234@localhost/bluemine_development'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app():
        pass

class DevConfig(Config):
    pass

config = {
    "dev" : DevConfig
}