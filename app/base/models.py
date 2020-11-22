# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_login import UserMixin
from sqlalchemy import Binary, Column, Integer, String

from app import db, login_manager

from app.base.util import hash_pass


ACCESS = {
    'admin' : 0,
    'staff' : 1,
    'student' : 2
}

STATUS = {
    'onCall'  : 1,
    'offCall' : 0
}

class User(db.Model, UserMixin):

    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(Binary)
    access = Column(Integer, default=ACCESS['student'])
    status = Column(Integer, default=STATUS['onCall'])

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                value = hash_pass( value ) # we need bytes here (not plain str)
                
            setattr(self, property, value)

    def __repr__(self):
        return str(self.username)

    def is_admin(self):
        return self.access == ACCESS['admin']

    def is_staff(self):
        return self.access == ACCESS['staff']

    def is_student(self):
        return self.access == ACCESS['student']

    def is_onCall(self):
        return self.status == STATUS['onCall']

    def set_status_onCall(self):
        self.status = STATUS['onCall']
        return self.status

    def set_status_offCall(self):
        self.status = STATUS['offCall']
        return self.status

@login_manager.user_loader
def user_loader(id):
    return User.query.filter_by(id=id).first()

@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()
    return user if user else None