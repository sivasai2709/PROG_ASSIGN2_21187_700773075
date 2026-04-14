from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from resolvers import (
    execute_nl_query,
    create_node,
    get_all,
    update_node,
    delete_node
)

app = Flask(__name__, template_folder="../frontend/templates")
CORS(app)

#  route for home page
@app.route("/")
def home():
    return render_template("index.html")

#  NLP GRAPH QUERY 
@app.route("/nlq", methods=["POST"])
def nl_query():
    data = request.json
    result = execute_nl_query(data["text"])
    return jsonify(result)

#  CRUD APIs 
@app.route("/create", methods=["POST"])
def create():
    data = request.json
    return jsonify(create_node(data["label"], data["props"]))

@app.route("/read/<label>")
def read(label):
    return jsonify(get_all(label))

@app.route("/update", methods=["POST"])
def update():
    data = request.json
    return jsonify(update_node(data["label"], data["name"], data["props"]))

@app.route("/delete", methods=["POST"])
def delete():
    data = request.json
    return jsonify(delete_node(data["label"], data["name"]))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)