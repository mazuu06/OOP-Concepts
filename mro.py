class A:
    def fun(self):
        print("I'm in class A")


class B(A):
    def done(self):
        print("I'm in class B")


class C(B, A):
    def gun(self):
        print("I'm in class C")

print(C.mro())          # returns the oder of inheritance