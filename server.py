'''
Date         : 2022-08-02 15:04:56
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2022-08-05 14:35:08
LastEditors  : BDFD
Description  : 
FilePath     : \server.py
Copyright (c) 2022 by BDFD, All Rights Reserved. 
'''
from requests import request
from flask import Flask, render_template, request

app = Flask(__name__)

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

  subscribes.append(f'{first_name},{last_name}|{email}')
  return render_template(
    'form.html',
    first_name=first_name,
    last_name=last_name,
    email=email,
    subscribes=subscribes)

if __name__ == '__main__':
  app.run(debug=True)
