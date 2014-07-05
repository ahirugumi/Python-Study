# -*- coding: utf-8 -*-

# 通常のやり方
def mynotwith():
    myfile=open('myclass.py')
    try:
        for line in myfile:
            print line,
    finally:
        myfile.close()

# withのやり方
def mywith():
    with open('myclass.py') as myfile:
        for line in myfile:
            print line,

# with独自クラス
# __enter__, __exit__を持つクラスを作成する
class MyWithClass:
    def __init__(self, args):
        print "init"
        self.foo = args
    def __enter__(self):
        print "enter"
        return self
    def __exit__(self, type, value, traceback):
        print "exit"

    def hoge(self):
        print self.foo

mynotwith()
print '======='
mywith()
print '======='
with MyWithClass("test") as my:
    my.hoge()
