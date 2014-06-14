# -*- coding: utf-8 -*-

class MyNew(object):
    def __new__(klass):
        print('__new__ called')
        #__new__ が ClassName のインスタンスを返した場合に限り ClassName.__init__ が呼び出される。
        return object.__new__(klass)
    def __init__(self):
        self.foo='init'
        print('__init__ called' + self.foo)

my=MyNew()
