#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route(‘/login’,methods=[“GET”,”POST”])
def login():
	username = request.args.get(‘username’)
	password = request.args.get(‘password’)
	print “USERNAME was “ + str(username)
	print “PASSWORD was “ + str(password)
	print os.popen(‘echo ‘ + str(password) + ‘ | sha256sum – ‘).read()
	return “OK”

if __name__ == ‘__main__’:
	app.run()
 
