from flask import Flask
from flask_pymongo import PyMongo

# Initialize mongo db with app
app = Flask(__name__)

mongodb_client = PyMongo(app, uri='mongodb://localhost:27017/todo_db')
db = mongodb_client.db

user_collection = db['users']
leaderboard = db['leaderboard']

# add user as {'username' : username, 'wins' : '0', 'loss' : '0'}
def add_user(username):
    pass

# add a win or loss to the users stats
def update_player_stats(username, stat_to_change, increment):
    pass


#change users score to {'username' : username, 'score' : new_score}... score will be a integer that ranks the player based on # games played and W/L ratio
def update_leaderboard(username, new_score):
    pass

# retuns a dictionary of form {rank : [score, usernmae]}
def get_leaderboard():
    pass

