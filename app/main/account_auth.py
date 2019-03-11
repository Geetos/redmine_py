from flask import render_template, jsonify, request,session, json
from ..db_models import Users
from . import main
from .. import db


@main.route('/signin',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('signin.html')
    
    rec = json.loads(request.get_data())

    username = rec['username']
    password = rec['password']

    info = Users.query.filter_by(username = username).first()

    if(info):
        if not info.password == password:
            res = {
                'status' : 500,
                'msg' : '密码错误'
            }

        else:
            session['user_info'] = {
                'id' : info.id,
                'username' : info.username,
                'type' : info.type
            }

            res = {
                'status' : 200,
                'msg' : 'success'
            }
    else:
        res = {
            'status' : 500,
            'msg' : '用户名不存在'
        }
    
    return jsonify(res = res)

@main.route('/signup',methods = ['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')

    rec = json.loads(request.get_data())

    if not Users.query.filter_by(username = rec['username']).first(): 
        new_user = Users(
            username = rec['username'],
            password = rec['password'],
            email = rec['email'],
            type = "user"
        )

        db.session.add(new_user)
        db.session.commit()
        res = {
            'status' : 200,
            'msg' : 'success'
        }

    else:
        res = {
            'status' : 500,
            'msg' : '用户名重复'
        }

    return jsonify(res = res)

@main.route('/signout')
def signout():
    if 'user_info' in session:
        session.pop('user_info')
    return jsonify(res = {
        "status" : 200
    })