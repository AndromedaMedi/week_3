from app import app
from flask import render_template, request, redirect
from models.event import Event
from models.events_list import events, get_event, add_event
from datetime import datetime

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/events')
def get_events():
    return render_template('events.html', events=events)

@app.route('/events/<int:event_index>')
def get_event(event_index):
    current_event = get_event(event_index)
    return render_template('event.html', event=current_event)

@app.route('/events/new')
def new_event():
    return render_template('new_event.html')

@app.route('/events', methods=['POST'])
def save_event():
    form_data = request.form
    date = form_data['date']
    date = datetime.strptime(date, '%Y-%m-%d')
    name = form_data['name']
    guests = form_data['guests']
    recurring = True if 'recurring' in request.form else False
    location = form_data['location']
    description = form_data['description']
    new_event = Event(date=date, name=name, guests=guests, recurring=recurring, location=location, description=description)
    add_event(new_event)

    return redirect('/events')