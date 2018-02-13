#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from HTMLParser import HTMLParser

import requests

URLS_LIST_FILE = sys.argv[1]
BASEURL = sys.argv[2]
REMAINDER_URL = sys.argv[3]
KEYSTRING = sys.argv[4]
CHECK_FILE = sys.argv[5]
METHOD = sys.argv[6]
OUTPUT_LOGFILE = sys.argv[7]

html_parse = HTMLParser()

isVulnerable = False

#Open urls file
f_urls = open(URLS_LIST_FILE, 'r')

while True:
	url_line = f_urls.readline()
	if not url_line:
		break
	
	url_line = str(url_line).rstrip('\n')
	
	url_line = BASEURL + url_line + REMAINDER_URL
	
	print url_line
	
	if METHOD == "GET":
		test_req = requests.get(url_line)
	elif METHOD == "POST":
		test_req = requests.post(url_line)
	
	req_output = str(html_parse.unescape(test_req.text))
	
	#Can we read secret output
	if KEYSTRING in req_output:
		isVulnerable = True
		break
	
	#Can we modify files which we are not supposed to
	f_secret = open(CHECK_FILE, 'r')
	secret_file_contents = f_secret.read()
	f_secret.close()
	if secret_file_contents != 'YouAreInSecretFile\n':
		#File was modified therefore vulnerable
		isVulnerable = True
		break

f_urls.close()

if isVulnerable:
	print "Found Path Traversal Vulnerability!"
	f_logout = open(OUTPUT_LOGFILE, 'w')
	f_logout.write("PATHTRAVERSAL")
	f_logout.close()

