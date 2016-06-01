# project/models.py


from project import db

import datetime


class Task(db.Model):

    __tablename__ = "tasks"

    task_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    posted_date = db.Column(db.Date, default=datetime.datetime.utcnow())
    status = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, due_date, priority, posted_date, status, user_id):
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.posted_date = posted_date
        self.status = status
        self.user_id = user_id

    def __repr__(self):
        return '<name {0}>'.format(self.name)


class Schedule(db.Model):
    
    __tablename__ = "schedule"

    schedule_id = db.Column(db.Integer, primary_key=True)
    workshift = db.Column(db.String, nullable=False)
    productionline = db.Column(db.String, nullable=False)
    start_date = db.Column(db.String, nullable=False)
    start_time = db.Column(db.String, nullable=False)
    end_date = db.Column(db.String, nullable=False)
    end_time = db.Column(db.String, nullable=False)
    posted_date = db.Column(db.Date, default=datetime.datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, workshift, productionline,start_date,start_time,end_date,end_time,posted_date, user_id):
        self.workshift = workshift
        self.productionline = productionline
        self.start_date = start_date
        self.start_time = start_time
        self.end_date = end_date
        self.end_time = end_time
        self.posted_date = posted_date
        self.user_id = user_id

    def __repr__(self):
        return '<name {0}>'.format(self.name)




class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    tasks = db.relationship('Task', backref='poster')
    role = db.Column(db.String, default='user')

    def __init__(self, name=None, email=None, password=None, role=None):
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def __repr__(self):
        return '<User {0}>'.format(self.name)
