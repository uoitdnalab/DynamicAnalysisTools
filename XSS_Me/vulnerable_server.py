#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file implements a web server that is vulnerable to
Cross-site-scripting (XSS).
"""

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

app.route(‘/’)
def home_page():
	return render_template(‘index.html’)

@app.route(‘/upload_blogpost’,methods=[“POST”])
def upload_blogpost():
	try:
		blogpost = request.form[“blog_text”]
		return render_template(‘index.html’,blogpost_contents=str(blogpost))
	except:
		return “ERROR”

if __name__ == ‘__main__’:
	app.run()
 
