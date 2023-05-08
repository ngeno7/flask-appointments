from flask import Blueprint, render_template, request, url_for, redirect, jsonify
from flask_login import login_required

import json
from ..db import db
from .models import Appointment, AppointmentSchema
appointments = Blueprint('appointments', __name__)


@appointments.route('/appointments', methods=['GET', 'POST'])
@login_required
def index():
    appointments = Appointment.query.all()
    appointment = Appointment()
    if request.form.get('id'):
        appointment = Appointment.query.filter_by(id=request.form.get('id')).first()
    if request.method == 'POST':
        appointment.title = request.form.get('title')
        appointment.date = request.form.get('date')
        appointment.time = request.form.get('time')
        appointment.status = 1
        db.session.add(appointment)
        db.session.commit()

        return redirect(url_for('appointments.index'))
    if request.args.get('json'):
        appointmentsSchema = AppointmentSchema(many=True)
        return jsonify(appointmentsSchema.dump(appointments))

    return render_template('appointments/index.html', title='Appointments', appointments=appointments)