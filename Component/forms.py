'''
Author: BDFD
Date: 2022-02-04 14:11:26
LastEditTime: 2022-02-04 14:34:14
LastEditors: BDFD
Description: Import Form use module flask-wtf
FilePath: \Heroku_Python_Template\forms.py
'''

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class SignUpForm(FlaskForm):
    username = StringField('Username :')
    password = PasswordField('Password :')
    submit = SubmitField('Sign Up')