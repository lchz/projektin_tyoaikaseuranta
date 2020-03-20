from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from sqlalchemy.exc import IntegrityError

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.forms import SignupForm


@app.route('/auth/login', methods=['GET', 'POST'])
def auth_login():
    if request.method == 'GET':
        return render_template('auth/loginForm.html', form=LoginForm())

    form = LoginForm(request.form)

    if not form.validate():
        return render_template('auth/loginForm.html', form=form)

    user = User.query.filter_by(username=form.username.data,
                                password=form.password.data).first()

    if not user:
        return render_template('auth/loginForm.html',
                               form=form,
                               error='No such username or password')

    login_user(user)
    return redirect(url_for('index'))


@app.route('/auth/signup/basic', methods=['GET', 'POST'])
def auth_signup_basic():
    if request.method == 'GET':
        return render_template('auth/signupForm.html', form=SignupForm(), role="BASIC")

    form = SignupForm(request.form)

    if not form.validate():
        return render_template('auth/signupForm.html', form=form, role="BASIC")

    user = User(form.name.data, form.username.data, form.password.data)
    user.roles.append("BASIC")

    try:
        db.session().add(user)
        db.session().commit()
    except IntegrityError:
        return render_template('auth/signupForm.html', 
                                form=form, 
                                error='Username is occupied.', 
                                role="BASIC"
                              )

    return redirect(url_for('auth_login'))


@app.route('/auth/signup/master', methods=['GET', 'POST'])
def auth_signup_master():
    if request.method == 'GET':
        return render_template('auth/signupForm.html', form=SignupForm(), role="MASTER")

    form = SignupForm(request.form)

    if not form.validate():
        return render_template('auth/signupForm.html', form=form, role="MASTER")

    user = User(form.name.data, form.username.data, form.password.data)
    user.roles.append("MASTER")

    try:
        db.session().add(user)
        db.session().commit()
    except IntegrityError:
        return render_template('auth/signupForm.html', 
                                form=form, 
                                error='Username is occupied.',
                                role="MASTER"
                              )

    return redirect(url_for('auth_login'))


@app.route('/auth/logout')
def auth_logout():
    logout_user()
    return redirect(url_for('index'))
