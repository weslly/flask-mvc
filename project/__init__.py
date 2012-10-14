# -*- coding: utf-8 -*-
__version__ = '0.1'
from flask import Flask
app = Flask('project')
app.config.from_object('project.config')
from project.controllers import *
