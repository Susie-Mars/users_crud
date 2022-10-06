from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user_model import User

@app.route('/')
@app.route('/user')
def show_all():
    all_users = User.get_all()
    return render_template("users.html", all_users=all_users)

@app.route('/user/<int:id>')
def get_one(id):
    data = { 'id': id }
    user = User.get_one(data)
    return render_template("show.html", user=user)

@app.route('/user/create', methods=["POST"])
def create_user():
    User.create(request.form)
    return redirect('/user')

@app.route('/user/new')
def new_user_table():
    return render_template("add_user.html")

@app.route('/user/<int:id>/edit')
def edit_user(id):
    data = {'id': id}
    user = User.get_one(data)
    return render_template("edit_user.html", user=user)

@app.route('/user/<int:id>/update', methods=["POST"])
def update(id):
    data = {'id': id, 'first_name': request.form['first'], 'last_name': request.form['last'], 'email':request.form['email']}
    User.edit_user(data)
    return redirect('/user')

@app.route('/user/<int:id>/delete')
def del_user(id):
    data = {'id': id}
    User.del_user(data)
    return redirect('/')


@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Sorry! No response. Try again.</h1>"
