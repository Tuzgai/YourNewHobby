from flask import Flask, render_template, redirect, send_from_directory
from flaskext.markdown import Markdown
from datetime import datetime
import os, random

app = Flask(__name__)
Markdown(app)

template_list = []

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico')

@app.before_first_request
def get_site_list():
    path = os.getcwd()

    for root, dirs, files in os.walk('./templates/'):
        for filename in files:
            template_list.append(files) 

@app.route('/')
def home():
    return redirect(random.choice(template_list[0]))

@app.route('/<hobby>')
def show_hobby(hobby):
    print(hobby)
    return render_template(f'{hobby}')