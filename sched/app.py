from flask import Flask, render_template, abort, jsonify, redirect
from flask import request, url_for
import datetime
import os, sys
import requests
import json

__author__ = 'cpuskarz'

app = Flask(__name__)

#APPSERVER = "http://127.0.0.1:5002"

@app.route('/')
def drummer_list():
    u = APPSERVER + "/options"
    page = requests.get(u)
    options = page.json()
    #drummer_list = options["drummers"]
    drummer_list = options["options"]

    return render_template('home.html', drummer_list=drummer_list)
    
@app.route("/about")
def about():
    return render_template('about.html', title="About")
    

@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """convert a datetime to a different format."""
    return value.strftime(format)

app.jinja_env.filters['datetimefilter'] = datetimefilter


if __name__ == '__main__':
    APPSERVER = os.getenv('app_server')
    app.run(debug=True, host='0.0.0.0')
