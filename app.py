'''
Date         : 2022-08-02 15:04:56
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2022-08-18 16:25:04
LastEditors  : BDFD
Description  : 
FilePath     : \app.py
Copyright (c) 2022 by BDFD, All Rights Reserved. 
'''
# from requests import request
from flask import Flask, render_template, request, redirect
import smtplib
import ssl
from email.message import EmailMessage
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
email_sender = 'customerservice@diligentgroup.ca'
email_password = 'RQG@&cLQAHS+'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///friends.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

# Initialize the database
db = SQLAlchemy(app)

# Create a db Model
class Friends(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(200), nullable=False)
  date_created = db.Column(db.DateTime, default=datetime.utcnow)
  
  #Create a function to return a string when we add something
  def __repr__(self):
    return '<Name %r>' % self.id


subscribes = []

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  names = ['John','Mary','Wes','Sally']
  return render_template('about.html', names=names)

@app.route('/friends', methods=['POST','GET'])
def friends():
  if request.method == 'POST':
    friend_name = request.form['name']
    new_friend = Friends(name=friend_name)
    # Push to Database
    try:
      db.session.add(new_friend)
      db.session.commit()
      return redirect('/friends')
    except:
      return 'There was an error adding your friends...'
  else:
    friends = Friends.query.order_by(Friends.date_created)
    return render_template('friends.html', friends=friends)

@app.route('/update/<int:id>', methods=['POST','GET'])
def update(id):
  friend_to_update = Friends.query.get_or_404(id)
  if request.method == 'POST':
    friend_to_update.name = request.form['name']
    try:
      db.session.commit()
      return redirect('/friends')
    except:
      return "There was a problem when updating that name..."
  else:
    return render_template('updatefriends.html',friend_to_update=friend_to_update)

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
  subject = f'Diligent Group'
  body = f"""
  Hello, {first_name},{last_name}
  This email is regarding the usage of Diligent Management software
  """

  em = EmailMessage()
  em['From'] = email_sender
  em['To'] = email
  em['Subject'] = subject
  em.set_content(body)

  # Add SSL (layer of security)
  context = ssl.create_default_context()

  # Log in and send the email
  with smtplib.SMTP_SSL('mail.diligentgroup.ca', 465, context=context) as smtp:
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
