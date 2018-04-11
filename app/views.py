# -*- coding:utf-8 -*-
from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm, CommentForm, FindForm
from app import db
import datetime


@app.route('/', methods = ['GET', 'POST'])
@app.route('/index/', methods = ['GET', 'POST'])
@app.route('/index/<name>', methods = ['GET', 'POST'])
def index(name='public'):
    user = {'nickname':''}
    # posts = db.get_all_data()
    posts = db.get_data_byname(name)
    # posts = [ # fake array of posts
    #     {
    #         'name': 'li',
    #         'comment': 'Beautiful day in Portland!'
    #     },
    #     {
    #         'name': 'de',
    #         'comment': 'The Avengers movie was so cool!'
    #     }
    # ]
    form = CommentForm()
    if form.validate_on_submit():
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
        # print("-------------------%s-------------", nowTime)
        db.insert(form.name.data, form.comment.data, nowTime)
        print("%s\t%s 发表了: %s"%(nowTime,form.name.data,form.comment.data))
        return redirect('/index')
    form2 = FindForm()
    if form2.validate_on_submit():
        name = form2.name.data
        print(name)
        return redirect('/index/%s'%name)
    return render_template('index.html',
                           title = 'Home',
                           # user = user,
                           posts = posts,
                           form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
        title = 'Sign In',
        form = form)
