# -*- coding: utf-8 -*-

from contextlib import contextmanager

@contextmanager
def foo(name):
    try:
        print "mae:" + name
        yield   # print "output:test"が実行される
        print "ushiro:" + name
    except Exception as e:
        print 'error'
    else:
        print 'no error'

# withとcontextmanagerで簡単に挟み込める
with foo("test"):
    print "output:test"
