# -*- coding: utf-8 -*-
'''
    Hello World App
    ~~~~~~~~~~~~~~~

    A simple hello world app for the flask boiler.

    :copyright: 2011 by Lee Olayvar
    :license: MIT, see LICENSE for more details.
'''

# Import the flask Module object
from flask import Module
# Note that this object *needs* to exist.
flask_module = Module('apps.hello_world')

# Now import our views. This way the module decorators get called.
import views
