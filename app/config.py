# -*- coding: utf-8 -*-
'''
    config
    ~~~~~~

    Configuration settings.

    :copyright: 2011 by Lee Olayvar.
    :license: MIT, see LICENSE for more details.
'''
config = {}

config['flask'] = {
    # The name of the flask app to use. This is used mostly for debugging
    # and making your app unique among others.
    'app_name':'flask_app',
    # Each app listed here will be registered as a Flask module object.
    'installed_apps': [
        'apps.hello_world',
    ],
}
