'''
Date         : 2022-08-02 15:04:56
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2022-08-17 14:47:50
LastEditors  : BDFD
Description  : 
FilePath     : \server.py
Copyright (c) 2022 by BDFD, All Rights Reserved. 
'''
# from requests import request
from flask import Flask, render_template, request
import smtplib
import ssl
from email.message import EmailMessage
import os

app = Flask(__name__)
email_sender = 'lejuan.jasiel@gmail.com'
email_password = 'tebsqtbdgnsfjeqs'

subscribes = []

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  names = ['John','Mary','Wes','Sally']
  return render_template('about.html', names=names)

@app.route('/subscribe')
def subscribe():
  return render_template('subscribe.html')

@app.route('/form',methods=['POST'])
def form():
  first_name = request.form.get('first_name')
  last_name = request.form.get('last_name')
  email = request.form.get('email')

  if not first_name or not last_name or not email:
    error_statement = 'All Form Fields Required...'
    return render_template(
      'fail.html',
      error_statement=error_statement, 
      first_name=first_name, 
      last_name=last_name, 
      email=email)

  # Set the subject and body of the email
  subject = f'Hello, {first_name},{last_name}'
  body = """
  hello msg from lejuan
  """

  em = EmailMessage()
  em['From'] = email_sender
  em['To'] = email
  em['Subject'] = subject
  em.set_content(body)

  # Add SSL (layer of security)
  context = ssl.create_default_context()

  # Log in and send the email
  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
      smtp.login(email_sender, email_password)
      smtp.sendmail(email_sender, email, em.as_string())

  subscribes.append(f'{first_name},{last_name}|{email}')
  return render_template(
    'form.html',
    first_name=first_name,
    last_name=last_name,
    email=email,
    subscribes=subscribes)

if __name__ == '__main__':
  app.run(debug=True)
