from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

cluster = MongoClient("mongodb+srv://abhi:contrapro472@contractor-l3tgn.mongodb.net/admin?retryWrites=true&w=majority")
db = cluster["testdb"]
collection = db["testcollection"]

post = {
	"_id": 2,
	"name": "Abhi",
	"fav drink": "Chai",
}


@app.route('/create')
def create():
	collection.insert_one(post)
	return '<h1>One post Inserted</h1>'
	

@app.route('/update')
def update():
	collection.update_one({"_id": 1}, {"$set": {"name": "Abhishek Kulkarni"}})
	return '<h1>One post updated</h1>'


@app.route('/delete')
def delete():
	collection.delete_one({"_id": 2})
	return 'Delete Successful'


@app.route('/home')
def index():
	return f'<h1>HOME</h1>'

