from flask import Flask, request, jsonify
from ansible import runner as ansible
from pymongo import MongoClient

user = MongoClient()['disrupt']['user']

app = Flask(__name__)

@app.route("/deploy", methods=["POST"])
def deploy():
	

if __name__ == "__main__":
	app.run()
