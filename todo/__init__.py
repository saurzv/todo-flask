import os
from os.path import join, dirname
from flask import Flask
from .extensions import mongo
from dotenv import load_dotenv
from todo.main.routes import main

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGO_URI = os.environ.get('MONGO_URI')


def create_app():
    todoapp = Flask(__name__)
    todoapp.config['MONGO_URI'] = MONGO_URI
    todoapp.register_blueprint(main)
    mongo.init_app(todoapp)
    return todoapp
