from application import app, db, login_required
from flask import render_template, request, redirect, url_for, abort
from flask_login import current_user

from application.projects.models import Project
from application.auth.models import User
from application.tasks.models import Task



@app.route('/projects/<project_id>/data', methods=['GET'])
@login_required(role='MASTER')
def project_data(project_id):

    project = Project.query.get(project_id)
    participants = Task.find_project_participants(project_id)

    return render_template('/data/projectData.html', 
                            project=project,
                            participants=participants)
