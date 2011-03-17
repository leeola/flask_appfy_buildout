# -*- coding: utf-8 -*-
'''
    main
    ~~~~

    Run Flask apps.

    :copyright: 2011 by Lee Olayvar.
    :license: MIT, see LICENSE for more details.
'''
import os
import sys

if 'lib' not in sys.path:
    # Add /lib as primary libraries directory, with fallback to /distlib
    # and optionally to distlib loaded using zipimport.
    sys.path[0:0] = ['lib', 'distlib']

from wsgiref.handlers import CGIHandler

from config import config
from flask import Flask

# Is this the development server?
debug = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')

# Instantiate the application.
app = Flask(config['flask'].get('app_name', 'flask_app')) 

def main():
    # Register all of the installed apps
    for app_location in config['flask'].get('installed_apps', []):
        # This seemingly weird syntax is the 'official' way to import a package
        # and grab the tail module.
        __import__(app_location)
        app_module = sys.modules[app_location]
        # Register each app.
        app.register_module(app_module.flask_module)
    CGIHandler().run(app)

if __name__ == '__main__':
    main()
