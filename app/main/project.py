from flask import render_template, jsonify, request,session, json
from ..db_models import Project
from . import main
from .. import db

@main.route('/project',methods = ['GET'])
def project_show():
    projects = Project.query.all()
    return jsonify(projects)
    
