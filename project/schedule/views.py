# project/tasks/views.py


import datetime
from functools import wraps
from flask import flash, redirect, render_template, \
    request, session, url_for, Blueprint

from .forms import AddTaskForm
from .forms import AddScheduleForm
from project import db
from project.models import Task


################
#### config ####
################

schedule_blueprint = Blueprint('schedule', __name__)


##########################
#### helper functions ####
##########################

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap


def pending_schedule():
    return db.session.query(Schedule)

################
#### routes ####
################


@schedule_blueprint.route('/schedule/')
@login_required
def schedule():
    return render_template(
        'schedule.html',
        form=AddScheduleForm(request.form),
        open_tasks=open_tasks(),
        closed_tasks=closed_tasks(),
        username=session['name']
    )


@schedule_blueprint.route('/addschedule/', methods=['GET', 'POST'])
@login_required
def new_schedule():
    error = None
    form = AddScheduleForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_schedule = Schedule(
                form.WorkShift.data,
                form.ProductionLine.data,
                form.start_date.data,
                form.start_time.data,
                form.end_date.data,
                form.end_time.data,
                session['user_id']
            )
            db.session.add(new_schedule)
            db.session.commit()
            flash('New schedule entry was successfully posted. Thanks.')
            return redirect(url_for('tasks.schedule'))
    return render_template(
        'schedule.html',
        form=form,
        error=error,
        pendingschedule = pendingschedule()
    )



