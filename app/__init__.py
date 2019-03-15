from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
import logging, os, time

db = SQLAlchemy()
logger = logging.getLogger(__name__)

def create_app(configName):
    app = Flask(__name__)
    logger.setLevel(level = logging.INFO)
    handler = logging.FileHandler(os.getcwd()+'/'+'log')
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    app.config.from_object(config[configName])
    from .main import main
    db.init_app(app)
    app.register_blueprint(main)
    logger.info("init!")
    return app
