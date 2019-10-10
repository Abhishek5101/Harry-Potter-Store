from flask import Flask, request, render_template, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
from random import choice

images = [
	"https://static0.srcdn.com/wordpress/wp-content/uploads/2016/11/Snake-from-Harry-Potter-and-the-Chamber-of-Secrets.jpg?q=50&fit=crop&w=738&h=369",
	"https://static3.srcdn.com/wordpress/wp-content/uploads/2016/11/Troll-in-Harry-Potter.jpg?q=50&fit=crop&w=738&h=369,",
	"https://static0.srcdn.com/wordpress/wp-content/uploads/2016/11/Harry-Potter-Crystal-Ball.jpg?q=50&fit=crop&w=738&h=369",
	"https://static3.srcdn.com/wordpress/wp-content/uploads/2016/11/Harry-Potter-Magical-Resistance.jpg?q=50&fit=crop&w=738&h=369",
	"https://static0.srcdn.com/wordpress/wp-content/uploads/2016/11/Fleur-Delacour-in-Harry-Potter-Veela-Charm.jpg?q=50&fit=crop&w=738&h=369",
	"https://static2.srcdn.com/wordpress/wp-content/uploads/2016/11/Sirius-Black-Metamorphmagi-in-Harry-Potter.jpg?q=50&fit=crop&w=738&h=369"]

app = Flask(__name__, template_folder='templates')

cluster = MongoClient("mongodb+srv://abhi:contrapro472@contractor-l3tgn.mongodb.net/admin?retryWrites=true&w=majority")
db = cluster["store"]
magic_collection = db["magic"]


# cart = db["shopping cart"]

# post = [
# 	{"_id": 1, "name": "love".capitalize(), "image": "https://static0.srcdn.com/wordpress/wp-content/uploads/2016/11/Harry-Potter-and-Ginny-Weasley-in-Love.jpg?q=50&fit=crop&w=738&h=369"},
# 	{"_id": 2, "name": "CONJURING".capitalize(), "image": "https://static0.srcdn.com/wordpress/wp-content/uploads/2016/11/Snake-from-Harry-Potter-and-the-Chamber-of-Secrets.jpg?q=50&fit=crop&w=738&h=369"},
# 	{"_id": 3, "name": "SPELL INVENTION".capitalize(), "image": "https://static0.srcdn.com/wordpress/wp-content/uploads/2016/11/Snake-from-Harry-Potter-and-the-Chamber-of-Secrets.jpg?q=50&fit=crop&w=738&h=369"},
# 	{"_id": 4, "name": "RUDIMENTARY MAGIC".capitalize(), "image": "https://static3.srcdn.com/wordpress/wp-content/uploads/2016/11/Troll-in-Harry-Potter.jpg?q=50&fit=crop&w=738&h=369"},
# 	{"_id": 5, "name": "NAMING SEER".capitalize(), "image": "https://static0.srcdn.com/wordpress/wp-content/uploads/2016/11/Harry-Potter-Crystal-Ball.jpg?q=50&fit=crop&w=738&h=369"},
# 	{"_id": 6, "name": "MAGICAL RESISTANCE".capitalize(), "image": "https://static3.srcdn.com/wordpress/wp-content/uploads/2016/11/Harry-Potter-Magical-Resistance.jpg?q=50&fit=crop&w=738&h=369"},
# 	{"_id": 7, "name": "VEELA CHARM".capitalize(), "image": "https://static0.srcdn.com/wordpress/wp-content/uploads/2016/11/Fleur-Delacour-in-Harry-Potter-Veela-Charm.jpg?q=50&fit=crop&w=738&h=369"},
# 	{"_id": 8, "name": "APPARITION AND DISAPPARITION".capitalize(), "image": "https://static0.srcdn.com/wordpress/wp-content/uploads/2016/11/Apparition-in-Harry-Potter.jpg?q=50&fit=crop&w=738&h=369"},
# 	{"_id": 9, "name": "UNBREAKABLE VOW".capitalize(), "image": "https://static1.srcdn.com/wordpress/wp-content/uploads/2016/11/An-Unbreakable-Vow-in-Harry-Potter.jpg?q=50&fit=crop&w=738&h=369"},
# 	{"_id": 10, "name": "FLIGHT".capitalize(), "image": "https://static2.srcdn.com/wordpress/wp-content/uploads/2016/11/Snape-in-Harry-Potter.jpg?q=50&fit=crop&w=738&h=369"},
# 	{"_id": 11, "name": "SEERS".capitalize(), "image": "https://static0.srcdn.com/wordpress/wp-content/uploads/2016/11/Trelawney-in-Harry-Potter.jpg?q=50&fit=crop&w=738&h=369"},
# 	{"_id": 12, "name": "ANIMAGI".capitalize(), "image": "https://static2.srcdn.com/wordpress/wp-content/uploads/2016/11/Sirius-Black-Metamorphmagi-in-Harry-Potter.jpg?q=50&fit=crop&w=738&h=369"},
# 	{"_id": 13, "name": "METAMORPHMAGI".capitalize(), "image": "https://static3.srcdn.com/wordpress/wp-content/uploads/2016/11/Metamorphmagus-in-Harry-Potter.jpg?q=50&fit=crop&w=738&h=369"},
# 	{"_id": 14, "name": "OCCLUMENCY".capitalize(), "image": "https://static3.srcdn.com/wordpress/wp-content/uploads/2016/11/Harry-Potter-Occlumency.jpg?q=50&fit=crop&w=738&h=369"},
# 	{"_id": 15, "name": "LEGITIMACY".capitalize(), "image": "https://static3.srcdn.com/wordpress/wp-content/uploads/2016/11/Harry-Potter-Legilimency.jpg?q=50&fit=crop&w=738&h=369"}
#
# ]

@app.route('/')
def show_magics():
	return render_template('magics_index.html', magics=magic_collection.find())


@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/magics')
def magic():
	magics = list(magic_collection.find({}))
	return render_template('magics_index.html', magics=magic_collection.find())


@app.route('/magics/new')
def new_magic():
	return render_template('magics_new.html')


@app.route('/magics', methods=["POST"])
def magic_create():
	new_magic = {
		"name": request.form.get("name"),
		"description": request.form.get("description"),
		"image": choice(images)
	}
	magic_collection.insert_one(new_magic)
	return render_template('magics_index.html', magics=magic_collection.find())


@app.route('/delete/<magic_id>', methods=['POST'])
def magic_delete(magic_id):
	"""Delete one guitar."""
	magic_collection.delete_one({'_id': ObjectId(magic_id)})
	return redirect(url_for('magic'))


@app.route('/magic/<magic_id>', methods=['GET'])
def update_magic(magic_id):
	if request.method == "GET":
		print(magic_id)
		magic = magic_collection.find_one({'_id': ObjectId(magic_id)})
	
		return render_template('update.html', magic=magic)
	else:
		return redirect(url_for('magic'))
	
	
@app.route('/update/<magic_id>', methods=['GET', "POST"])
def magic_update(magic_id):
	if request.method == 'POST':
		updated_magic = {
			"name": request.form['name'],
			"description": request.form['description']
		}
		magic_collection.update_one({'_id': ObjectId(magic_id)}, {'$set': updated_magic})
		return redirect(url_for('magic'))
	if request.method == 'GET':
		magic = magic_collection.find_one({'_id': ObjectId(magic_id)})
		return redirect(url_for('magic_update', magic=magic))
