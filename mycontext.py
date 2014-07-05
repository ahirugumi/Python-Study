# -*- coding: utf-8 -*-

from contextlib import contextmanager

@contextmanager
def foo(name):
    try:
        print "mae:" + name
        yield
        print "ushiro:" + name
    except Exception as e:
        print 'error'
    else:
        print 'no error'

with foo("test"):
    print "output:test"
