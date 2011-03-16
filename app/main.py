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
    sys.path[0:0] = ['lib', 'distlib', 'distlib.zip']

from config import config
from flask import Flask

# Is this the development server?
debug = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')

# Instantiate the application.
app = Flask(config['app_name']) 

def main():
    # Register all of the installed apps
    for app in config['installed_apps']:
        flask_module = __import__('%s.module' % app)
        app.register_module(flask_module)
    app.run(debug=debug)

if __name__ == '__main__':
    main()
