from . import db

class Users(db.Model):
    __table__name  = 'users'
    id             = db.Column(db.Integer,primary_key=True)
    username       = db.Column(db.String(45))
    password       = db.Column(db.String(45))
    email          = db.Column(db.String(100))
    type           = db.Column(db.String(45))

class Project(db.Model):
    __table__name  = 'project'
    id             = db.Column(db.Integer, primary_key=True)
    name           = db.Column(db.String(45))
    description    = db.Column(db.Text)
    is_public      = db.Column(db.Boolean)
    created_on     = db.Column(db.Date)
    status         = db.Column(db.Integer)

class Tracker(db.Model):
    __table__name  = 'tracker'
    id             = db.Column(db.Integer, primary_key=True)
    name           = db.Column(db.String(45))

class Projects_tracker(db.Model):
    __table__name  = 'projects_tracker'
    id             = db.Column(db.Integer, primary_key=True)
    project_id     = db.Column(db.Integer)
    tracker_id     = db.Column(db.Integer)


class Progress(db.Model):
    __table__name  = 'Progress'
    id             = db.Column(db.Integer, primary_key=True)
    tracker_id     = db.Column(db.Integer)
    project_id     = db.Column(db.Integer)
    description    = db.Column(db.Text)
    due_date       = db.Column(db.Date)
    category_id    = db.Column(db.Integer)
    assigned_to_id = db.Column(db.Integer)
    priority       = db.Column(db.String(20))
    author_id      = db.Column(db.Integer)
    created_on     = db.Column(db.Integer)
    start_date     = db.Column(db.Integer)
    done_ratio     = db.Column(db.Integer)
    is_public      = db.Column(db.Boolean)
    closed_on      = db.Column(db.Boolean)

class Members(db.Model):
    __table__name  = 'members'
    id             = db.Column(db.Integer, primary_key=True)
    project_id     = db.Column(db.Integer)
    user_id        = db.Column(db.String(45))