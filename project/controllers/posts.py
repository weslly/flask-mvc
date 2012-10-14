# -*- coding: utf-8 -*-
from project import app
from flask import render_template, request, flash
from flask.ext.wtf import Form, TextField, TextAreaField, Required
from project.models.Post import Post
from project.models import db

class AddPostForm(Form):
    title = TextField('Title: ', validators=[Required()])
    content = TextAreaField('Content: ', validators=[Required()])


@app.route('/posts')
def index():
    return render_template('posts/index.html')


@app.route('/posts/view/<slug>')
def view(slug):
    return render_template('posts/view.html')

@app.route('/posts/add', methods=('GET', 'POST'))
def add():
    form = AddPostForm()

    if request.method == 'POST' and form.validate_on_submit():

        post = Post(form.title.data, form.content.data)
        db.session.add(post)
        db.session.commit()

        flash('The post was sucessfuly added.')
        return render_template('posts/index.html')

    else:
        return render_template('posts/add.html', form=form)
