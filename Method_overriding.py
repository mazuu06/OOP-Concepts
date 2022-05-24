class Demo:
    def display(self):
        print("I'm in Demo Class")

    def test(self):
        print("I'm learning Python")

class Nano(Demo):
    def display(self):
        print("I'm in Nano Class")

obj = Nano()
obj.test()
obj.display()

