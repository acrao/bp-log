from bp_log import app
from utils import login_required
from flask import request, render_template, url_for, redirect, flash
from models import Measurement
from forms import MeasForm
from google.appengine.api import users
from google.appengine.ext import db

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/meas_add', methods=['GET','POST'])
@login_required
def meas_add():
    form = MeasForm(request.form, csrf_enabled=False)
    if request.method == 'POST' and form.validate():
        meas = Measurement(sys=form.sys.data,
                           dia=form.dia.data,
                           pulse=form.pulse.data)
        meas.put()
        return redirect(url_for('meas_add'))
    return render_template('meas_form.html', form=form)

@app.route('/show_meas')
@login_required
def show_meas():
    user = users.get_current_user()
    meas_query = Measurement.gql("WHERE user = :curr_user", curr_user=user)
    meas_list = meas_query.fetch(10)
    return render_template('render_meas.html',
                           meas_dict=[meas.to_dict() for meas in meas_list])
