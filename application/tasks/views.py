from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application.tasks.models import Task
from application.projects.models import Project
from application.tasks.forms import TaskForm

import datetime


@app.route('/projects/<project_id>/tasks', methods=['GET'])
@login_required
def tasks_index(project_id):

    project = Project.query.get(project_id)

    return render_template('tasks/taskList.html',
                           tasks=Task.query.filter_by(project_id=project_id),
                           project=project)

@app.route('/projects/<project_id>/tasks/<task_id>', methods=['GET'])
@login_required
def task_index(task_id):
    return render_template('tasks/task.html', task=Task.query.get(task_id))


@app.route('/projects/<project_id>/tasks/new')
@login_required
def tasks_form(project_id):
    return render_template('tasks/taskForm.html', form=TaskForm(), project_id=project_id)


@app.route('/projects/<project_id>/tasks', methods=['POST'])
@login_required
def tasks_create(project_id):
    form = TaskForm(request.form)

    if not form.validate():
        return render_template('tasks/taskForm.html', form=form, project_id=project_id)

    status = form.status.data
    date = datetime.date(1999, 9, 19)

    if status:
        date = datetime.datetime.now().date()

    task = Task(form.name.data, form.content.data,
                form.estimatedTime.data, date, status)

    task.account_id = current_user.id
    task.project_id = project_id

    db.session().add(task)
    db.session().commit()

    return redirect(url_for('tasks_index', project_id=project_id))


@app.route('/projects/<project_id>/tasks/<task_id>', methods=['POST'])
@login_required
def tasks_set_done(project_id, task_id):

    task = Task.query.get(task_id)
    task.status = True
    task.date = datetime.datetime.now().date()

    db.session().commit()

    return redirect(url_for('tasks_index', project_id=project_id))


@app.route('/projects/<project_id>/tasks/<task_id>/actualTime', methods=['POST'])
@login_required
def tasks_set_actualTime(project_id, task_id):

    task = Task.query.get(task_id)
    task.actualTime = request.form.get('set_actualTime')

    db.session().commit()

    return redirect(url_for('tasks_index', project_id=project_id))
