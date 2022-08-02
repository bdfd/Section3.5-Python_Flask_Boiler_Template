'''
Author: BDFD
Date: 2022-02-03 15:32:30
LastEditTime: 2022-06-14 10:49:30
LastEditors: BDFD
Description: 
FilePath: \Heroku_Python_Template\server.py
'''
# from crypt import methods
# from pickle import TRUE
# from unittest import result
# from uuid import RESERVED_FUTURE
from distutils.debug import DEBUG
from doctest import debug
from flask import Flask, render_template, request, redirect, url_for, flash
from Component.forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY']= 'bdfd2005'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/blog')
def blog():
  posts = [
    {'title':'Technology in 2019', 'author':'avi'},
    {'title':'China is stronger than ever', 'author':'david'}
  ]
  return render_template(
    'blog.html', 
    author = 'bdfd', 
    sunny = True, 
    posts=posts)

@app.route('/signup', methods=['GET','POST'])
def signup():
  form = SignUpForm()
  if form.is_submitted():
    result = request.form
    print('Hello World, result is',result)
    return render_template('/function/signup/user.html', result=result)
  return render_template('/function/signup/signup.html', form=form)

@app.route('/upload')
def upload():
    return render_template('function/upload/upload.html')


@app.route('/upload/success', methods=['POST'])
def upload_success():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return render_template('function/upload/upload_success.html', name=f.filename)

@app.route('/login')
def login():
    return render_template('function/login/login.html')


@app.route('/login/validate', methods=['POST'])
def login_validate():
    if request.method == 'POST' and request.form['email'] == 'test@gmail.com' and request.form['password'] == 'test':
        return redirect(url_for('login_success'))
    else:
      flash('Incorrect Username/Password')
      return redirect(url_for('login'))
    

@app.route('/login/success')
def login_success():
    return 'Logged in successfully.'

@app.route('/test/<name>')
def test(name):
  return render_template('test.html',author=name, contents=['Bill','Tom','Alex'])

def home():
  return render_template('home.html')
app.add_url_rule('/home','home',home)

@app.route('/home/<int:age>')
def home_age(age):
  return 'Age: {}'.format(age)

@app.route('/home/<name>')
def home_name(name):
  return render_template('home_name.html',name=name)

if __name__ == '__main__':
  app.run(debug=True)
