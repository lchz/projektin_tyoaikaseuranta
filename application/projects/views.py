from application import app, db
from flask import render_template, request, redirect, url_for
from application.projects.models import Project
from application.projects.forms import ProjectForm


@app.route('/projects', methods=['GET'])
def projects_index():
    return render_template('/projects/projectList.html', projects=Project.query.all())


@app.route('/projects/new')
def projects_form():
    return render_template('projects/projectForm.html', form=ProjectForm())


@app.route('/projects', methods=['POST'])
def projects_create():

    form = ProjectForm(request.form)

    if not form.validate():
        return render_template('projects/projectForm.html', form=form)

    project = Project(form.name.data, form.description.data)

    db.session().add(project)
    db.session().commit()

    return redirect(url_for('projects_index'))
