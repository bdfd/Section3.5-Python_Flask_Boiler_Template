'''
Date         : 2022-08-02 15:04:56
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2022-08-04 15:52:49
LastEditors  : BDFD
Description  : 
FilePath     : \server.py
Copyright (c) 2022 by BDFD, All Rights Reserved. 
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  title = "BDFD's Blog"
  return render_template('index.html', title=title)

@app.route('/about')
def about():
  names = ['John','Mary','Wes','Sally']
  title = 'About BDFD!'
  return render_template('about.html', names=names, title=title)

if __name__ == '__main__':
  app.run(debug=True)
