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
    data = Task.find_project_participants(project_id)
    timeData = Task.time_of_project(project_id)

    for d in data:
        taskData = Task.find_tasks_of_participant(project.id, d.get('accountId'))

        uncom = taskData[0].get('uncom')
        com = taskData[1].get('com')

        d['total'] = uncom + com
        d['uncom'] = uncom
        d['com'] = com

    return render_template('/data/dataProject.html',
                           project=project,
                           data=data,
                           timeData=timeData)

@app.route('/projects/<project_id>/data/tasks/<account_id>', methods=['GET'])
@login_required(role="ANY")
def tasks_data_of_participant(project_id, account_id):

    account = User.query.get(account_id)
    project = Project.query.get(project_id)
    tasks = Task.find_my_tasks(account_id, project_id)
    timeData = Task.time_of_person(project_id, account_id)

    return render_template('data/dataTasks.html', 
                            account=account,
                            project=project, 
                            tasks=tasks,
                            timeData=timeData)

