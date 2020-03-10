from application import app, db
from flask import render_template, request, redirect, url_for
from application.tasks.models import Task


from datetime import datetime


@app.route('/projectId/tasks', methods=['GET'])
def tasks_index():
    return render_template('tasks/taskList.html', tasks=Task.query.all())


@app.route('/projectId/tasks/new')
def tasks_form():
    return render_template('tasks/taskForm.html')


@app.route('/projectId/tasks', methods=['POST'])
def tasks_create():
    task = Task(request.form.get('name'), 
                request.form.get('content'), 
                request.form.get('estimatedTime'),
                datetime.strptime(request.form.get('date'), '%Y-%m-%d').date()
               )

    db.session().add(task)
    db.session().commit()

    return redirect(url_for('tasks_index'))


@app.route('/projectId/tasks/<task_id>', methods=['POST'])
def tasks_set_done(task_id):
    task = Task.query.get(task_id)
    task.status = True
    
    db.session().commit()

    return redirect(url_for('tasks_index'))


@app.route('/projectId/tasks/<task_id>/actualTime', methods=['POST'])
def tasks_set_actualTime(task_id):
    print('HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH')
    task = Task.query.get(task_id)
    print('TTTTTTTTT', task.name)
    task.actualTime = request.form.get('set_actualTime')
    # task.actualTime = 4

    # print('DDDDDDDDDDDDDDDDD', request.form.get('reset_actualTime'))
    db.session().commit()

    return redirect(url_for('tasks_index'))