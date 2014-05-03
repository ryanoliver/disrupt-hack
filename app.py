from flask import Flask, request, jsonify
from pymongo import MongoClient
from fabric.api import env, run 
import requests
import time
import 
user = MongoClient()['disrupt']['user']

app = Flask(__name__)
app.debug = True

@app.route('/deploy', methods=['POST'])
def deploy():
	#user = request.form['username']
	#repo = request.form['repository']
	#repo_url = request.form['url']	
	print request.form
	do_api = request.form['do_api']
	do_client = request.form['do_client']
	do_payload = {'name': 'testing', 'client_id': do_client, 'api_key': do_api, 'size_id': '66', 'image_id': '3447912', 'region_id': '4'}
	droplet = requests.get('https://api.digitalocean.com/droplets/new', params=do_payload).json()
	time.sleep(55)
	droplet = requests.get('https://api.digitalocean.com/droplets/{0}'.format(droplet['droplet']['id']), params={'client_id': do_client, 'api_key': do_api}).json()
	env.hosts = [droplet['droplet']['ip_address']]
	print env.hosts
	print run('ls -al')
	return jsonify({})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
