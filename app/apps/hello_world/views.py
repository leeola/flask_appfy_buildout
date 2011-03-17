# -*- coding: utf-8 -*-
'''
    views
    ~~~~~

    Some basic views.

    :copyright: 2011 by Lee Olayvar.
    :license: MIT, see LICENSE for more details.
'''
from flask import render_template

from apps.hello_world import flask_module


@flask_module.route('/')
def hello_world():
    '''A basic hello.'''
    return 'Hello World!'

@flask_module.route('/pretty')
def pretty_hello():
    '''A pretty hello.'''
    return render_template('hello_world.html',
                           message='Hello Pretty World!')

