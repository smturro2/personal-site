from flask import Flask, render_template, # flash, make_response, redirect, request, jsonify,
# import matplotlib.pyplot as plt
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# import io
# import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("FrontPage.html",renderJumbotron=True)

@app.route('/Work')
def Work():
    return render_template("Work.html",renderJumbotron=False)

@app.route('/Education')
def Education():
    return render_template("Education.html",renderJumbotron=False)

@app.route('/Competitions')
def Competitions():
    return render_template("Competitions.html",renderJumbotron=False)


@app.route('/Projects')
def Projects():
    return render_template("Projects.html",renderJumbotron=False)

@app.route('/Papers')
def Papers():
    return render_template("Papers.html",renderJumbotron=False)

@app.route('/Resume')
def Resume():
    return render_template("Resume.html",renderJumbotron=False)

@app.route('/More')
def More():
    return render_template("More.html",renderJumbotron=False)

if __name__ == "__main__":
    app.run(debug=True)
