from flask import render_template
from app import app
from app import db
from app.models import User
from flask import jsonify
from flask import request
from flask import redirect

@app.route('/', methods = ['GET', 'POST'])
def index():
    users = User.query.all()
    print users
    if request.method == 'POST':
        if request.form['action'] == "delete":
            myid = request.form['user_id']
            thisuser = User.query.get(myid)
            db.session.delete(thisuser)
            db.session.commit()
            return redirect('/')
    return render_template("index.html", users=users)


@app.route('/add',  methods = ['GET', 'POST'])
def add():
    if request.method == 'POST':
        user = User(request.form["username"], request.form["email"])
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    return render_template("add.html")


@app.route('/edit/<id>',  methods = ['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        user_id = id
        user = User.query.get(user_id)
        user.username = request.form["name"]
        user.email = request.form["email"]
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    else:
        print "get edit"
        user_id = id
        print user_id
        user = User.query.get(user_id)
        print user
        return render_template("edit.html", user=user)

#Other edit method (need edit button to be <a href="/edit/?id={{ user.id }}"><button class="btn btn-outline-info">Edit</button></a>)
# @app.route('/edit/',  methods = ['GET', 'POST'])
# def edit():
#     if request.method == 'POST':#
#         print id
#     else:
#         print "get edit"
#         id = request.args.get('id')
#         print id
#         user = None
#         # user = User.query.filter_by(id=id)
#         # print user
#         return render_template("edit.html", user=user)
