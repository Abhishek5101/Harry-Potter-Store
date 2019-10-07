from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://abhi:contrapro472@contractor-l3tgn.mongodb.net/admin?retryWrites=true&w=majority")

db = cluster["testdb"]
collection = db["testcollection"]

post = {
	"name": "Abhi",
	"fav drink": "Chai",
	"facebook": "https://www.facebook.com/jesse.phoenix.3154"
}

update = {
	"name": "Abhishek"
}
collection.insert_one(post)
collection.update_one({"_id": 0}, {"$set": {"name": "Abhishek"}})

