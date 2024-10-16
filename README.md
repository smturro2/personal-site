# Turro's Personal Site

[![Website https://personal-site-5mhro.ondigitalocean.app//](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](https://personal-site-5mhro.ondigitalocean.app//)

This website is to provide a more detailed view of my work than a standard resume:
[personal-site-5mhro.ondigitalocean.app/](https://personal-site-5mhro.ondigitalocean.app/)

## Setup
1. **Clone** the repo to your local computer
2. Install using pipenv
3. Run app.py with top level folder as the working directory

---


* To run the app just run the **app.py** script

* To update the Quantum-Tomography code run the command:

        git submodule update --remote --merge

* To update the live site go into the cpanel terminal run:

        cd Flask_App_new/Flask_App_git_repo_new
        git status
        git pull

## Troubleshooting

Note(after 6 years of python development): Ahh... the hell of trying to set up python for the first time...

- *'py' is not recognized*. 
  - Depending on how you downloaded python your PATH variable for python (the _py_ in this walkthrough) may be diffrent.
Other common names are _python_ or _python3_. Its whatever you type into the command prompt in order to start python. 
  Replace the _py_ with whatever your PATH variable for python is. Follow [this tutorial](https://www.educative.io/edpresso/how-to-add-python-to-path-variable-in-window) 
  if you can't figure out your python's PATH variable and you know for certain python is installed.

- *'pip' is not recognized*. 
  - pip is not defined as a PATH variable. Instead of just using *pip*
use *py -m pip*. It is rare but if you downloaded python in a weird way you may not have pip installed. You'll have to search for how to install pip on your computer. 
The process differs depending on if you're using PC/mac/ubuntu.

[//]: # ()
[//]: # (## Quantum-Tomography Code)

[//]: # ()
[//]: # (Note: I dont know if I still need this)

[//]: # ()
[//]: # (This code uses the quantum-tomography python code as a submodule. You will need to update this when)

[//]: # (you first clone this repo.)

[//]: # ()
[//]: # (        git submodule update --init)

[//]: # ()
[//]: # (To update the Quantum-Tomography code run the command:)

[//]: # ()
[//]: # (        git submodule update --remote --merge)