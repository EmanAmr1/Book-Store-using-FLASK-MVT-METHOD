class Config:
    @staticmethod
    def init_app():
        pass


class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='sqlite:///project.db'

class ProductionConfig(Config):
    DEBUG=False
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:1234@localhost:5432/flask_book_store'



config_options ={
    "dev": DevelopmentConfig,
    "prd":ProductionConfig
}