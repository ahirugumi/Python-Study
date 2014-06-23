# -*- coding: utf-8 -*-

def foo(self):
    return "foo"

myMetaClass = type('MyMetaClass',
        (object,),
        {'myMethod': foo})

ins = myMetaClass()
print (ins.__class__)
print (type(ins))
print (ins.__class__.__class__)
print ins.myMethod()
