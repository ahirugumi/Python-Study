from myclass import MyClass
class MyIterator(object):
    def __init__(self):
        self.myclasses = []
        self.index = 0
    def add(self, myclass):
        self.myclasses.append(myclass)
        return self
    def next(self):
        if self.index >= len(self.myclasses):
            self.index=0
            raise StopIteration
        ret=self.myclasses[self.index]
        self.index += 1
        return ret
    def __iter__(self):
        return self

my=MyIterator().add(MyClass(1, "foo1")).add(MyClass(2, "foo2")).add(MyClass(3, "foo3"))
for hoge in my:
    print(hoge)

print [x.name for x in my if x.id == 2]
