# -*- coding: utf-8 -*-
from flask import Flask
from project.helpers import slugify
from project.models import db
import datetime
from flask.ext.sqlalchemy import SQLAlchemy

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(140))
    slug = db.Column(db.String(80))
    content = db.Column(db.Text)

    created = db.Column(db.DateTime)
    modified = db.Column(db.DateTime)

    def __init__(self, title, content):
        self.title = title
        self.slug = slugify(title)
        self.content = content
        self.created = datetime.datetime.now()
        self.modified = datetime.datetime.now()

    def __repr__(self):
        return '<Post %r>' % self.id

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'slug': self.slug,
            'created': self.created.strftime("%s"),
            'modified': self.modified.strftime("%s")
        }
