from flask import render_template, jsonify, request,session, json
from ..db_models import Project, Tracker, Projects_tracker
from . import main
from .. import db
import datetime

class _Project:
    def __init__(self, name):
        self.name = name

    def get_project(self):
        project = Project.query.filter_by(name = project_name).first()
        return project

    def 

@main.route('/project')
def project_show():
    return render_template("project_show.html")

@main.route('/get_projects')
def get_project():
    projects = Project.query.order_by("created_on").all()
    dicProject = []
    for i in range(0,len(projects)):
        dicProject.append({
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

        new_tracker = Tracker(
            name = 'tracker_' + rec['name']
        )

        db.session.add(new_project, new_tracker)
        db.session.commit()
        
        new_projects_tracker = Projects_tracker(
            project_id = new_project.id,
            tracker_id = new_tracker
        )

        db.session.add(new_tracker)
        db.session.commit()

        res = {
            'status' : 200,
            'msg' : 'success'
        }

    else:
        res = {
            'status' : 500,
            'msg' : '项目名重复'.html", error_info = "Unable to find the project named " + project_name)
        }

    return jsonify(res = res)


@main.route('/project/<project_name>')
def project_outline_page(project_name):
    project = _Project(project_name)
    this_project = _Project.get_project()

    if not this_project:
        return render_template("404.html", error_info = "Unable to find the project named " + project_name)
    # tracker
    return render_template("project_outline.html")

@main.route('/project/<project_name>/outline')
def project_outline():
    pass

@main.route('/project/<project_name>/progress')

    