# Turro's Personal Site

[![Website https://turroscott-wn697.ondigitalocean.app](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](https://personal-site-5mhro.ondigitalocean.app//)

[This website](https://turroscott-wn697.ondigitalocean.app)
provides a more detailed view of my work than a standard resume.

# Dev Setup
1. Use **Pipenv**
2. Run **app.py** as target with top level folder as the working directory

# Prod Setup (New)
Use cloud.digitalocean.com
1. Create new **App Platform**
2. If trouble with github, uninstall and reinstall digitialocean on your github account
3. Make sure to downgrade the hell out the infra
3. For **Deployment settings**, change the **run command**: `gunicorn --worker-tmp-dir /dev/shm app:app`


Guide: https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-app-using-gunicorn-to-app-platform#step-5-mdash-deploying-to-digitalocean-with-app-platform