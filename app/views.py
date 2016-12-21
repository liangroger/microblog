#coding=utf-8
from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    app.logger.info("==>index")
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': u'中文'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    print posts
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

