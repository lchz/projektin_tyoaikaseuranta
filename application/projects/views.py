from application import app, db
from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user
from application.projects.models import Project
from application.auth.models import User
from application.projects.forms import ProjectForm


@app.route('/projects/<project_id>', methods=['GET'])
def project_index(project_id):

    project = Project.query.get(project_id)
    canRegister = True

    for participant in project.participants:
        if participant.id == current_user.id:
            canRegister = False
            
    return render_template('/projects/project.html', 
                            project=project, 
                            creator=User.query.get(project.account_id),
                            canRegister=canRegister
                          )


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


@app.route('/projects/<project_id>/register', methods=['POST'])
def project_registration(project_id):

    try:
        project = Project.query.get(project_id)

        project.participants.append(current_user)

        db.session().commit()
        return redirect(url_for('projects_index'))
        
    except:
        abort(400)
