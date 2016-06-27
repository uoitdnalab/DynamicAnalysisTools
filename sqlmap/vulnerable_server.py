#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

from flask import Flask
from flask import request

conn = sqlite3.connect(‘:memory:’) #in-memory SQL database for this example
sql_cur = conn.cursor()

#Create the SQL table
sql_cur.execute(‘CREATE TABLE users(username text, password text, balance real)’)

#Fill the table with some dummy customer data
sql_cur.execute(‘INSERT INTO users (username,password,balance) VALUES (“john”,”pass”,43.21)’)
sql_cur.execute(‘INSERT INTO users (username,password,balance) VALUES (“uoit”,”eng123”,233.82)’)
sql_cur.execute(‘INSERT INTO users (username,password,balance) VALUES (“dc”,”j102”,208.19)’)
app = Flask(__name__)

@app.route(‘/get_balance’,methods=[“GET”,”POST”])
def login():
	username = request.args.get(‘username’)
	password = request.args.get(‘password’)

	try:
		dat = sql_cur.execute(‘SELECT balance FROM users WHERE username”’ + str(username) + ‘” AND password=”’ + str(password) + ‘”’).next()[0]
		balance = str(dat)
	except:
		balance = “UNAUTHORIZED”

	return balance
 
