# -*- coding: utf-8 -*-

class MyProperty(object):  #プロパティ
    def __init__(self, val):
        print('__init__', val)
        self.val = val

    def fget(self):
        print('fget', self.val)
        return self.val

    def fset(self, val):
        print('fset', val)
        self.val = val

    def fdel(self):
        del self.val

    #プロパティ定義
    attr=property(fget, fset, fdel)

if __name__ == "__main__":
    my=MyProperty("piyo")   #init
    print(my.attr)   #get
    my.attr="bar"    #set
    del my.attr      #delete
