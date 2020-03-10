from application import app, db
from flask import render_template, request, redirect, url_for
from application.projects.models import Project


@app.route('/projects', methods=['GET'])
def projects_index():
    return render_template('/projects/projectList.html', projects=Project.query.all())


@app.route('/projects/new')
def projects_form():
    return render_template('projects/projectForm.html')


@app.route('/projects', methods=['POST'])
def projects_create():

    project = Project(request.form.get('name'), request.form.get('description'))

    db.session().add(project)
    db.session().commit()

    return redirect(url_for('projects_index'))
