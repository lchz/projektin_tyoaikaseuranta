from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application.projects.models import Project
from application.auth.models import User
from application.projects.forms import ProjectForm

# <li><a href="{{ url_for('tasks_index') }} ">List all tasks</a></li>
#         <li><a href="{{ url_for('tasks_form') }} ">Create a task</a></li>



@app.route('/projects/<project_id>', methods=['GET'])
def project_index(project_id):

    project = Project.query.get(project_id)

    return render_template('/projects/project.html', 
                            project=project, 
                            creator=User.query.get(project.account_id))


@app.route('/projects', methods=['GET'])
def projects_index():
    return render_template('/projects/projectList.html', projects=Project.query.all())


@app.route('/projects/new')
@login_required
def projects_form():
    return render_template('projects/projectForm.html', form=ProjectForm())


@app.route('/projects', methods=['POST'])
@login_required
def projects_create():

    form = ProjectForm(request.form)

    if not form.validate():
        return render_template('projects/projectForm.html', form=form)

    project = Project(form.name.data, form.description.data)
    project.account_id = current_user.id

    db.session().add(project)
    db.session().commit()

    return redirect(url_for('projects_index'))
