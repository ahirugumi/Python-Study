# -*- coding: utf-8 -*-

class MyDescriptor(object):
    def __init__(self, val):
        print('__init__', val)
        self.val = val

    def __get__(self, ins, klass):
        print('__get__', self.val)
        return self.val

    def __set__(self, ins, val):
        print('__set__', val)
        self.val = val

    def __delete__(self, ins):
        print('__delete__', self.val)

class MyClass(object):
    des=MyDescriptor("foo")

if __name__ == "__main__":
    my=MyClass()    #init
    print(my.des)   #get
    my.des="bar"    #set
    del my.des      #delete
