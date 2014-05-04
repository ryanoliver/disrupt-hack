from flask import Flask, request, jsonify
from pymongo import MongoClient
import paramiko
import socket
import requests
import time
import os

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
user = MongoClient()['disrupt']['user']

app = Flask(__name__)
app.debug = True

@app.route('/deploy', methods=['POST'])
def deploy():
	user = request.form['username']
	repo = request.form['repository']
	do_api = os.getenv('DO_API') 
	do_client = os.getenv('DO_CLIENT')
	do_payload = {'name': 'testing', 'client_id': do_client, 'api_key': do_api, 'size_id': '66', 'image_id': '3447912', 'region_id': '4', 'ssh_key_ids':'122283'}
	droplet = requests.get('https://api.digitalocean.com/droplets/new', params=do_payload).json()
	time.sleep(55)
	droplet = requests.get('https://api.digitalocean.com/droplets/{0}'.format(droplet['droplet']['id']), params={'client_id': do_client, 'api_key': do_api}).json()
	print droplet['droplet']['ip_address']
	ssh.connect(droplet['droplet']['ip_address'], username='root', allow_agent=True)
	_, stdout, stderr = ssh.exec_command('apt-add-repository -y ppa:chris-lea/node.js;apt-get update;apt-get install -y git ruby python-dev python-pip nodejs build-essential; git clone https://github.com/{0}/{1}.git; cd {1}; sh build.sh'.format(user, repo))
	while not stdout.channel.exit_status_ready():
		print stdout.read()
	ssh.close()
	return jsonify({'ip': droplet['droplet']['ip_address']})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
