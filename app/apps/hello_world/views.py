# -*- coding: utf-8 -*-
'''
    views
    ~~~~~

    Some basic views.

    :copyright: 2011 by Lee Olayvar.
    :license: MIT, see LICENSE for more details.
'''

from apps.hello_world import module


@module.route('/')
def hello_world():
    '''Render the hello world page.'''
    print 'Wooo'
    return 'Hi'

@module.route('/pretty')
def pretty_hello():
    '''A pretty hello.'''
    pass

