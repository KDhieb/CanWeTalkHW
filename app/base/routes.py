# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import socketio

from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, join_room, leave_room, emit, send
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

from flask import jsonify, render_template, redirect, request, url_for
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user
)

from app import db, login_manager
from app.base import blueprint
from app.base.forms import LoginForm, CreateAccountForm
from app.base.models import User, STATUS

from app.base.util import verify_pass


@blueprint.route('/')
def route_default():
    return redirect(url_for('base_blueprint.login'))


@blueprint.route('/error-<error>')
def route_errors(error):
    return render_template('errors/{}.html'.format(error))


## Login & Registration

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if 'login' in request.form:

        # read form data
        username = request.form['username']
        password = request.form['password']

        # Locate user
        user = User.query.filter_by(username=username).first()

        # Check the password
        if user and verify_pass(password, user.password):
            login_user(user)
            return redirect(url_for('base_blueprint.route_default'))

        # Something (user or pass) is not ok
        return render_template('accounts/login.html', msg='Wrong user or password', form=login_form)

    if not current_user.is_authenticated:
        return render_template('accounts/login.html',
                               form=login_form)
    return redirect(url_for('home_blueprint.index'))


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    login_form = LoginForm(request.form)
    create_account_form = CreateAccountForm(request.form)
    if 'register' in request.form:

        username = request.form['username']
        email = request.form['email']

        # Check username exists
        user = User.query.filter_by(username=username).first()
        if user:
            return render_template('accounts/register.html',
                                   msg='Username already registered',
                                   success=False,
                                   form=create_account_form)

        # Check email exists
        user = User.query.filter_by(email=email).first()
        if user:
            return render_template('accounts/register.html',
                                   msg='Email already registered',
                                   success=False,
                                   form=create_account_form)

        # else we can create the user
        user = User(**request.form)
        db.session.add(user)
        db.session.commit()

        print("Username")
        print(user.username)
        print("User access")
        print(user.access)
        print("USER ID")
        print(user.id)

        return render_template('accounts/register.html',
                               msg='User created please <a href="/login">login</a>',
                               success=True,
                               form=create_account_form)

    else:
        return render_template('accounts/register.html', form=create_account_form)


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('base_blueprint.login'))


@blueprint.route('/shutdown')
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...'


## Errors

@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('/page-403.html'), 403


@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('/page-403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('/page-404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('/page-500.html'), 500


@blueprint.route('/', methods=['POST'])
def setStatusOnCall(user):
    getUser = User.query.filter_by(email=user.email)
    getUser.status = STATUS['onCall']
    db.session.commit()


@blueprint.route('/', methods=['POST'])
def setStatusOffCall(user):
    getUser = User.query.filter_by(id=user.id)
    getUser.status = STATUS['offCall']
    db.session.commit()


# TWILIO INTEGRATION

sio = socketio.Client()

# Add Twilio authentication
account_sid = "ACcf38ea43fc81a1e3ad61701d6ebc096d"
auth_token = "19de24461133f84dad89be010d3b2554"
client = Client(account_sid, auth_token)

app = Flask(__name__)
socketio = SocketIO(app)


@blueprint.route('/chat-index')
def home():
    return render_template("chat-index.html")


@blueprint.route('/chat')
def chat():
    print("IS THIS BEING CALLED!%!%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    username = request.args.get('username')
    room = request.args.get('room')

    if username and room:
        return render_template('chat.html', username=username, room=room)
    else:
        return redirect(url_for('base_blueprint.home'))


@socketio.on('send_message')
def handle_send_message_event(data):
    app.logger.info("{} has sent message to the room {}: {}".format(data['username'],
                                                                    data['room'],
                                                                    data['message']))
    socketio.emit('receive_message', data, room=data['room'])
    print(data)
    # Stores the room and message in a variable
    outbound_number = data['room']
    outbound_message = data['message']

    # Sends the message back to the user via SMS
    client.messages.create(
        to=outbound_number,
        from_="+16479058445",
        body=outbound_message
    )


@socketio.on('join_room')
def handle_join_room_event(data):
    app.logger.info("{} has joined the room {}".format(data['username'], data['room']))
    join_room(data['room'])
    socketio.emit('join_room_announcement', data, room=data['room'])


@socketio.on('leave_room')
def handle_leave_room_event(data):
    app.logger.info("{} has left the room {}".format(data['username'], data['room']))
    leave_room(data['room'])
    socketio.emit('leave_room_announcement', data, room=data['room'])


# Routes for Twilio API
@app.route("/inbound_sms", methods=['GET', 'POST'])
def inbound_sms():
    response = MessagingResponse()

    # Grab information from incoming SMS message
    inbound_message = request.form['Body']
    from_number = request.form['From']
    to_number = request.form['To']

    # Store the above information in a data object to pass on
    data = {'username': from_number, 'room': from_number, 'message': inbound_message}

    # Emits a received message using the above data object to the room number
    socketio.emit('receive_message', data, room=from_number)

    return 'message sent'


if __name__ == "__routes__":
    socketio.run(app, debug=True)
