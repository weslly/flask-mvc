# -*- coding: utf-8 -*-
from project import app
from flask import render_template, request, flash

@app.route('/')
def index():
    return render_template('pages/index.html')
