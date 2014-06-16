# coding: utf-8

"""
noseのテストプログラム
"""
import mynose
from nose.tools import ok_, eq_, with_setup

def test_execute_1():
    """ mynose.executeのテスト1 eq_ assertラッパー"""
    eq_(mynose.execute("test"), "test_nose")

def test_execute_2():
    """ mynose.executeのテスト2 ok_ assertラッパー"""
    ok_(mynose.execute("test")=="test_nose", "テスト失敗 test_noseではない。")

def test_execute_3():
    """ mynose.executeのテスト3 assertも当たり前だが、使える"""
    assert mynose.execute("test")=="test_nose", "テスト失敗 test_noseではない。"

def setup():
    """ setup """
    print "setup"

def setup99():
    print "setup99"

def teardown():
    print "teardown"

def teardown99():
    print "teardown99"

@with_setup(setup99, teardown99)
def test_execute_99():
    """ mynose.execute99 """
    ok_(True)
