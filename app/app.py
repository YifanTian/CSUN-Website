from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
import requests
import json

# app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
    # return "Hello World"
    return render_template('index.html')

@app.route('/introduction')
def show_introduction():
	return render_template('introduction.html')

@app.route('/event')
def show_event():
	return render_template('event.html')

@app.route('/dept1')
def show_dept1():
	return render_template('dept.html')

@app.route('/dept2')
def show_dept2():
	return render_template('dept.html')

@app.route('/dept3')
def show_dept3():
	return render_template('dept.html')

@app.route('/dept4')
def show_dept4():
	return render_template('dept.html')

if __name__ == "__main__":
    app.run(debug = True)