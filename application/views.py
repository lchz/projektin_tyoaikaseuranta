from flask import render_template
from application import app

from flask_login import login_required, current_user


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/myPage')
@login_required
def myPage():

    projects = current_user.registrations

    return render_template('myPage.html', projects=projects)