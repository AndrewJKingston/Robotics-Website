from my_app import app
from flask import render_template, request, redirect
import requests
import sys

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/outreach.html")
def outreach():
    return render_template("outreach.html")

@app.route("/officers.html")
def officers():
    return render_template("officers.html")

@app.route("/blog.html")
def blog():
    return render_template("blog.html")

@app.route("/alumni.html")
def alumni():
    return render_template("alumni.html")

@app.route("/adders.html")
def adders():
    return render_template("adders.html")

@app.route("/pithons.html")
def pithons():
    return render_template("pithons.html")

@app.route("/diamondbacks.html")
def diamondbacks():
    return render_template("diamondbacks.html")

@app.route("/diamonds.html")
def diamonds():
    return render_template("diamonds.html")
