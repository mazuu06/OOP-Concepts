class X:
    def display(self):
        print("Display in class X")

class Y(X):
    def fun(self):
        print("Fun in class Y")

class Z(X):
    def gun(self):
        print("Gun in class Z")

class Demo(Y, Z):
    def demo(self):
        print("demo in class Demo")

obj = Demo()
obj.display()