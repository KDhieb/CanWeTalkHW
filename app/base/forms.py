# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SelectField, StringField
from wtforms.validators import InputRequired, Email, DataRequired
from app.base.models import ACCESS

## login and registration

CHOICES = [(ACCESS['staff'], 'Staff'),(ACCESS['student'], 'Student')]

class LoginForm(FlaskForm):
    username = StringField    ('Username', id='username_login'   , validators=[DataRequired()])
    password = PasswordField('Password', id='pwd_login'        , validators=[DataRequired()])

class CreateAccountForm(FlaskForm):
    username = StringField('Username'     , id='username_create' , validators=[DataRequired()])
    email    = StringField('Email'        , id='email_create'    , validators=[DataRequired(), Email()])
    password = PasswordField('PasswordChange' , id='pwd_create'      , validators=[DataRequired()])
    access   = SelectField('Access',id='access_create', validators=[DataRequired()], choices=CHOICES)

# class CreateStudentAccountForm(FlaskForm):
#     username = TextField('Username'     , id='username_create' , validators=[DataRequired()])
#     email    = TextField('Email'        , id='email_create'    , validators=[DataRequired(), Email()])
#     password = PasswordField('Password' , id='pwd_create'      , validators=[DataRequired()])
#
#
# class CreateStaffAccountForm(FlaskForm):
#     username = TextField('Username'     , id='username_create' , validators=[DataRequired()])
#     email    = TextField('Email'        , id='email_create'    , validators=[DataRequired(), Email()])
#     password = PasswordField('Password' , id='pwd_create'      , validators=[DataRequired()])
