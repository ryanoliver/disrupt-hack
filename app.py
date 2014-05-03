from flask import Flask, request, jsonify
from ansible import runner as ansible
from pymongo import MongoClient

user = MongoClient()['disrupt']['user']

app = Flask(__name__)

@app.route('/')
def status():
	print 'lol'
	return jsonify('{}')

@app.route('/deploy', methods=['POST'])
def deploy():
	#user = request.form['username']
	#repo = request.form['repository']
	#repo_url = request.form['url']	
	do_api = request.form['do_api']
	do_client = request.form['api_client']
	droplet = ansible.Runner(
		module_name='digital_ocean',
		module_args='api_key={0}, client_id={1}, state=present'.format(do_api, do_client)
	).run()
	print droplet
	

if __name__ == '__main__':
	app.run(port=80)
