#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

#First set up web filesystem

os.makedirs(“webroot”) #Authorized public access
os.makedirs(“privateroot”) #Unauthorized public access

#Create a publicly accessible file
f = open(‘webroot/public_file_001.bin’, ‘w’)
f.close()

#Create a privately accessible file
f = open(‘privateroot/private_file_001.bin’, ‘w’)
f.close()

from flask import Flask

app = Flask(__name__)

@app.route(‘/<path:filepath>’)
def list_dir(filepath):
	return str(os.listdir(‘webroot/’ + str(filepath)))

if __name__ == ‘__main__’:
	app.run()
 
