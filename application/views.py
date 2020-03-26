from flask import render_template
from application import app

from flask_login import login_required, current_user
from application.tasks.models import Task



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/myPage')
@login_required
def myPage():

    if current_user.get_roles() == 'MASTER':
        projects = current_user.created_projects
    else:
        projects = current_user.registrations

    return render_template('myPage.html', projects=projects, role=current_user.get_roles())
