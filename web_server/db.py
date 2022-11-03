from flask import Flask
from flask_pymongo import PyMongo

# Initialize mongo db with app
app = Flask(__name__)

mongodb_client = PyMongo(app, uri='mongodb://localhost:27017/todo_db')
db = mongodb_client.db

user_collection = db['users']


