#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	:author: Tim Wang
"""
#import the flask class from the flask module
from flask import Flask, make_response, render_template, redirect, url_for, request #, jsonify

from commontools import log

#create the application object
app = Flask(__name__, template_folder='templates/')
app._static_folder = 'static/'

#use decorators to link the function to a url 
@app.route('/')
def home():
	return render_template("login.html")

@app.route('/welcome', methods=['GET','POST'])
def welcome():
	return render_template("welcome.html") #render a template

@app.route('/login', methods=['GET','POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid credentials. Please try again.'
		else:
			#return redirect(url_for('welcome'))
			return render_template("welcome.html")
	return render_template('login.html', error=error)

#start the server with the 'run()' method
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')

#-----------------------------------
#@app.errorhandler(500)
#def internal_error(error):

#	reply = []
#	return jsonify(reply)

#-----------------------------------
#@app.errorhandler(404)
#def not_found(error):
#	return make_response(jsonify( { 'error': 'Not found' } ), 404)




