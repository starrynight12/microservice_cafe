from flask import Flask, jsonify


app = Flask(__name__)
# URL for microservice (port since you're running 2 programs)
MS_URL = "http://localhost:5000"


categories = [
    {"id": 1, "name": "Hot Coffee", "description": "Our hot coffee selection."},
    {"id": 2, "name": "cold Coffee", "description": "Our cold coffee selection."}

]

items = [
    {"id": 1, "cateogry_id": "1", "name": "item name",
     "description": "item's description.", "price": " $1.59", "image": "url"}
]

modifiers = [
    {"id": 1, "item_id": "1", "name": "modifier name",
     "options": "modifier options.", "additional cost": " $1.59"}
]


@app.route('/')
def index():
    return 'Home page. can call /categories, /items, or /modifiers.'


@app.route("/categories", methods=['GET'])
def get_categories():
    return jsonify(categories)


@app.route("/items", methods=['GET'])
def get_items():
    return jsonify(items)


@app.route("/modifiers", methods=['GET'])
def get_modifiers():
    return jsonify(modifiers)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
