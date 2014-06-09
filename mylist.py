# -*- coding: utf-8 -*-

class MyList(list):

    def __init__(self):
        list.__init__(self)

    def append(self,value):
        list.insert(self, 0, value)

if __name__ == "__main__":
    my = MyList()
    my.append("foo")
    my.append("bar")
    my.append("baz")

    for i in my:
        print i
