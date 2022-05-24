class A:
    def hello(self):
        print("I'm in class A")


class B:
    def hello(self):
        print("I'm in class B")


class C:
    def hello(self):
        print("I'm in class C")


def fun(obj):
    obj.hello()

obj = A()
fun(obj)

obj = B()
fun(obj)

obj = C()
fun(obj)

