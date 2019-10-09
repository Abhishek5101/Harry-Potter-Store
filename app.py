from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

cluster = MongoClient("mongodb+srv://abhi:contrapro472@contractor-l3tgn.mongodb.net/admin?retryWrites=true&w=majority")
db = cluster["store"]
magic_collection = db["magic"]
cart = db["shopping cart"]

post = [
	{"_id": 1, "name": "love", "image": "https://static0.srcdn.com/wordpress/wp-content/uploads/2016/11/Harry-Potter-and-Ginny-Weasley-in-Love.jpg?q=50&fit=crop&w=738&h=369"},
	{"_id": 2, "name": "CONJURING", "image": "https://static0.srcdn.com/wordpress/wp-content/uploads/2016/11/Snake-from-Harry-Potter-and-the-Chamber-of-Secrets.jpg?q=50&fit=crop&w=738&h=369"},
	{"_id": 3, "name": "SPELL INVENTION", "image": "https://static0.srcdn.com/wordpress/wp-content/uploads/2016/11/Snake-from-Harry-Potter-and-the-Chamber-of-Secrets.jpg?q=50&fit=crop&w=738&h=369"},
	{"_id": 4, "name": "RUDIMENTARY MAGIC", "image": "https://static3.srcdn.com/wordpress/wp-content/uploads/2016/11/Troll-in-Harry-Potter.jpg?q=50&fit=crop&w=738&h=369"},
	{"_id": 5, "name": "NAMING SEER", "image": "https://static0.srcdn.com/wordpress/wp-content/uploads/2016/11/Harry-Potter-Crystal-Ball.jpg?q=50&fit=crop&w=738&h=369"},
	{"_id": 6, "name": "MAGICAL RESISTANCE", "image": "https://static3.srcdn.com/wordpress/wp-content/uploads/2016/11/Harry-Potter-Magical-Resistance.jpg?q=50&fit=crop&w=738&h=369"},
	{"_id": 7, "name": "VEELA CHARM", "image": "https://static0.srcdn.com/wordpress/wp-content/uploads/2016/11/Fleur-Delacour-in-Harry-Potter-Veela-Charm.jpg?q=50&fit=crop&w=738&h=369"},
	{"_id": 8, "name": "APPARITION AND DISAPPARITION", "image": "https://static0.srcdn.com/wordpress/wp-content/uploads/2016/11/Apparition-in-Harry-Potter.jpg?q=50&fit=crop&w=738&h=369"},
	{"_id": 9, "name": "UNBREAKABLE VOW", "image": "https://static1.srcdn.com/wordpress/wp-content/uploads/2016/11/An-Unbreakable-Vow-in-Harry-Potter.jpg?q=50&fit=crop&w=738&h=369"},
	{"_id": 10, "name": "FLIGHT", "image": "https://static2.srcdn.com/wordpress/wp-content/uploads/2016/11/Snape-in-Harry-Potter.jpg?q=50&fit=crop&w=738&h=369"},
	{"_id": 11, "name": "SEERS", "image": "https://static0.srcdn.com/wordpress/wp-content/uploads/2016/11/Trelawney-in-Harry-Potter.jpg?q=50&fit=crop&w=738&h=369"},
	{"_id": 12, "name": "ANIMAGI", "image": "https://static2.srcdn.com/wordpress/wp-content/uploads/2016/11/Sirius-Black-Metamorphmagi-in-Harry-Potter.jpg?q=50&fit=crop&w=738&h=369"},
	{"_id": 13, "name": "METAMORPHMAGI", "image": "https://static3.srcdn.com/wordpress/wp-content/uploads/2016/11/Metamorphmagus-in-Harry-Potter.jpg?q=50&fit=crop&w=738&h=369"},
	{"_id": 14, "name": "OCCLUMENCY", "image": "https://static3.srcdn.com/wordpress/wp-content/uploads/2016/11/Harry-Potter-Occlumency.jpg?q=50&fit=crop&w=738&h=369"},
	{"_id": 15, "name": "LEGITIMACY", "image": "https://static3.srcdn.com/wordpress/wp-content/uploads/2016/11/Harry-Potter-Legilimency.jpg?q=50&fit=crop&w=738&h=369"}
	
]


@app.route('/create')
def create():
	magic_collection.insert_many(i for i in post)
	return render_template('layout.html', post=post)


