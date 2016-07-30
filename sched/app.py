import json
import urllib
import requests
from flask import Flask, render_template, request, url_for
import os

# Phase 3 - p5000

__author__ = 'cpuskarz'

app = Flask(__name__)

#APPSERVER = "http://127.0.0.1:5002"

@app.route('/', methods=["GET"])
def drummer_list():
    u = APPSERVER + "/options"
    page = requests.get(u)
    options = page.json()
    drummer_list = options["options"]
    return render_template('home.html', drummer_list=drummer_list)


@app.route("/about")
def about():
    return render_template('about.html', title="About")


@app.route("/results", methods=["GET"])
def respick():
    drumman = request.args.get('drummer')
    drumman = drumman.replace(" ", "")
    drumman = drumman.lower()
    u = requests.post(APPSERVER + "/mess", data=drumman)
    page = u.content
    return page

if __name__ == '__main__':
    APPSERVER = os.getenv('app_server')
    app.run(debug=False, host='0.0.0.0')
