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

@app.route('/user/new', methods=["POST"])
def add_user():
    User.create(request.form)
    return redirect('/user')

@app.route('/user/<int:id>/edit')
def edit_user(id):
    data = {'id': id}
    user = User.get_one(data)
    return render_template("edit_user.html", user=user)

@app.route('/user/<int:id>/delete')
def del_user(id):
    data = {'id': id}
    User.delete(data)
    return redirect('/user')

# @app.route('/user/<int:id>/show')
# def show_user(id):
#     print("Showing the User Info From the Form")
#     print(request.form)
#     return render_template("show.html")


@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Sorry! No response. Try again.</h1>"
