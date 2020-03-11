from application import app, db
from flask import render_template, request, redirect, url_for
from application.tasks.models import Task
from application.tasks.forms import TaskForm

import datetime


@app.route('/projectId/tasks', methods=['GET'])
def tasks_index():
    return render_template('tasks/taskList.html', tasks=Task.query.all())


@app.route('/projectId/tasks/new')
def tasks_form():
    return render_template('tasks/taskForm.html', form=TaskForm())


@app.route('/projectId/tasks', methods=['POST'])
def tasks_create():
    form = TaskForm(request.form)

    if not form.validate():
        return render_template('tasks/taskForm.html', form=form)

    status = form.status.data
    date = datetime.date(1999, 9, 19)

    if status:
        date = datetime.datetime.now().date()

    task = Task(form.name.data, form.content.data,
                form.estimatedTime.data, date, status)

    db.session().add(task)
    db.session().commit()

    return redirect(url_for('tasks_index'))


@app.route('/projectId/tasks/<task_id>', methods=['POST'])
def tasks_set_done(task_id):

    task = Task.query.get(task_id)
    task.status = True
    task.date = datetime.datetime.now().date()

    db.session().commit()

    return redirect(url_for('tasks_index'))


@app.route('/projectId/tasks/<task_id>/actualTime', methods=['POST'])
def tasks_set_actualTime(task_id):

    task = Task.query.get(task_id)
    task.actualTime = request.form.get('set_actualTime')

    db.session().commit()

    return redirect(url_for('tasks_index'))
