from flask import Flask, request, render_template, redirect
from gevent.pywsgi import WSGIServer
from gevent import monkey, sleep
import threading
import json
import os

class server_class():

	__name = "[Flask Server]"

	def __init__(self, threadID, name, client, delivery, delman):
		self.name = name

		self.client_obj = client
		self.delivery_obj = delivery
		self.delman_obj = delman

		self.http_server = None
		self.thread_server = None

	def run(self):
		# Weird Fix
		monkey.patch_all()

		app = Flask(__name__)

		self.http_server = WSGIServer(("0.0.0.0",80), app)
		self.thread_server = threading.Thread(target=self.http_server.serve_forever)

		# Routes
		@app.route('/', methods=['GET','POST'])
		def hermes_index():
			return render_template('index.html', request=request, delivery_obj=delivery_obj)

		@app.route('/newclient', methods=['GET','POST'])
		def new_client_page():
			return render_template('newclient.html', request=request, client_obj=client_obj)

		@app.route('/newdelivery', methods=['GET','POST'])
		def new_delivery_page():
			return render_template('newdelivery.html', request=request, delivery_obj=delivery_obj)

		@app.route('/newdeliveryman', methods=['GET','POST'])
		def new_deliveryman_page():
			return render_template('newdeliveryman.html', request=request, delman_obj=delman_obj)		



		self.thread_server.start()

	def stop(self):
		self.http_server.stop()
		self.thread_server.join()
		