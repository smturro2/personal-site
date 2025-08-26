from flask import (Flask, render_template, jsonify,request)  # flash, make_response, redirect, request, jsonify,

from elio import StateManager, get_random_image

app = Flask(__name__)
state_manager = StateManager()

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


# Elio stuff
@app.route('/elio')
def elio_home():
    return render_template('elio.html')

@app.route('/elio/get-image/<state>')
def get_elio_image(state):
    folder = 'breakfast' if state == 'morning' else 'dinner'
    return jsonify(image=get_random_image(folder))

@app.route('/elio/get-state', methods=['GET'])
def get_elio_state():
    return jsonify(state_manager.get_state())

@app.route('/elio/get-state', methods=['POST'])
def set_elio_state():
    new_state = request.json.get('state')
    state_manager.set_state(new_state)
    return jsonify(state_manager.get_state())

if __name__ == "__main__":
    app.run(debug=True)


