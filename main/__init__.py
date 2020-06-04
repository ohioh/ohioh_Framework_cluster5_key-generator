import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from celery import Celery

from config import Config
from dotenv import load_dotenv

load_dotenv()

ma = Marshmallow()
db = SQLAlchemy()
celery = Celery(__name__, broker=Config.broker_url)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    with app.app_context():
        from main.models.user import User
        db.create_all()
    


    from .api import blue_print
    app.register_blueprint(blue_print, url_prefix='/api/v1')

    return app


app = create_app(Config)
celery.conf.update(app.config)

celery.autodiscover_tasks(
    ['main.tasks'], 
    related_name='tasks', 
    force=True
)
