# -*- coding: utf-8 -*-
from project import app
from flask import render_template, request, get_flashed_messages
from flask.ext.wtf import Form, TextField, Required


class MyForm(Form):
    text = TextField('Text: ', validators=[Required()])


@app.route('/')
def start():
    return render_template('printer/index.html')

@app.route('/print', methods=['GET', 'POST'])
def printer():
    form = MyForm()

    if request.method == 'POST' and form.validate_on_submit():
        # return str()
        from project.models.Printer import Printer
        printer = Printer()
        printer.show_string(form.text.data)
        return render_template('printer/index.html')

    else:
        return render_template('printer/print.html', form=form)
