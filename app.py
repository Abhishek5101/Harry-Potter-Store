from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

cluster = MongoClient("mongodb+srv://abhi:contrapro472@contractor-l3tgn.mongodb.net/admin?retryWrites=true&w=majority")
db = cluster["store"]
magic_collection = db["magic"]
cart = db["shopping cart"]

post = [
	{"_id": 1, "name": "love"},
	{"_id": 2, "name": "CONJURING"},
	{"_id": 3, "name": "SPELL INVENTION"},
	{"_id": 4, "name": "RUDIMENTARY MAGIC"},
	{"_id": 5, "name": "NAMING SEER"},
	{"_id": 6, "name": "MAGICAL RESISTANCE"},
	{"_id": 7, "name": "VEELA CHARM"},
	{"_id": 8, "name": "APPARITION AND DISAPPARITION"},
	{"_id": 9, "name": "UNBREAKABLE VOW"},
	{"_id": 10, "name": "FLIGHT"},
	{"_id": 11, "name": "SEERS"},
	{"_id": 12, "name": "ANIMAGI"},
	{"_id": 13, "name": "METAMORPHMAGI"},
	{"_id": 14, "name": "OCCLUMENCY"},
	{"_id": 15, "name": "LEGITIMACY"}
	
]


@app.route('/create')
def create():
	magic_collection.insert_many(i for i in post)
	return '<h1>All posts Inserted</h1>'


# @app.route('/update')
# def update():
# 	collection.update_one({"_id": 1}, {"$set": {"name": "Abhishek Kulkarni"}})
# 	return '<h1>One post updated</h1>'
#
#
# @app.route('/delete')
# def delete():
# 	collection.delete_one({"_id": 2})
# 	return 'Delete Successful'
#
#
# @app.route('/home')
# def index():
# 	return f'<h1>HOME</h1>'
#

print(post)
