from flask import Flask, make_response, redirect, request, jsonify, render_template, flash
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io
import numpy as np

app = Flask(__name__)


# Default home page. This is the page the user first sees when visting the site
@app.route('/')
def index():
    return render_template("FrontPage.html",renderJumbotron=True)

# Career Page
@app.route('/Work')
def Work():
    return render_template("Work.html",renderJumbotron=False)

# Education Page
@app.route('/Education')
def Education():
    return render_template("Education.html",renderJumbotron=False)

# Competitions Page
@app.route('/Competitions')
def Competitions():
    return render_template("Competitions.html",renderJumbotron=False)


# Projects Page
@app.route('/Projects')
def Projects():
    return render_template("Projects.html",renderJumbotron=False)

# Papers Page
@app.route('/Papers')
def Papers():
    return render_template("Papers.html",renderJumbotron=False)

# Resume Page
@app.route('/Resume')
def Resume():
    return render_template("Resume.html",renderJumbotron=False)

# More Page
@app.route('/More')
def More():
    return render_template("More.html",renderJumbotron=False)

if __name__ == "__main__":
    app.run(debug=True)
