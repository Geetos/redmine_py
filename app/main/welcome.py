from . import main
from flask import render_template, session, jsonify


@main.route('/')
def welcome():     
    return render_template('welcome.html')

@main.route('/hasLogin')
def hasLogin():
    if 'user_info' in session:
        res = {
            "status" : 200,
            "user_info" : session['user_info']
        }
    else:
        res = {
            "status" : 500
        }
    return jsonify(res = res)