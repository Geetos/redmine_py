from flask import render_template, jsonify, request,session, json
from ..db_models import Project
from . import main
from .. import db
import datetime

@main.route('/project')
def project_show():
    return render_template("project_show.html")

@main.route('/get_projects')
def get_project():
    projects = Project.query.order_by("created_on").all()
    dicProject = []
    for i in range(0,len(projects)):
        dicProject.append({
            'id' : projects[i].id,
            'name' : projects[i].name,
            'description' : projects[i].description,
            'is_public': projects[i].is_public,
            'created_on': projects[i].created_on,
            'status' : projects[i].status
        })
    return jsonify(res = dicProject)  

@main.route('/new_project',methods=['GET','POST'])
def new_project():
    if request.method == 'GET':
        return render_template('project_add.html')

    rec = json.loads(request.get_data())

    if not Project.query.filter_by(name = rec['name']).first(): 

        date_time = datetime.datetime.now()

        new_project = Project(
            name = rec['name'],
            description = rec['description'],
            is_public = rec['is_public'],
            created_on = str(date_time.year) + '-' + str(date_time.month) + '-' + str(date_time.day),
            status = 0
        )

        db.session.add(new_project)
        db.session.commit()
        res = {
            'status' : 200,
            'msg' : 'success'
        }

    else:
        res = {
            'status' : 500,
            'msg' : '项目名重复'
        }

    return jsonify(res = res)
    
