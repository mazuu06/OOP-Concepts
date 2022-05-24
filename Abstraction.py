from abc import ABC, abstractmethod

class Parent(ABC):          # abstract class 
    def test(self):         # Concrete method
        print("I'm inside test function")
    @abstractmethod         # abstract method
    def print_(self):
        pass
        
class ChildOne(Parent):
    def One(self):
        print("I'm in ChildOne Class.")
        
class ChildTwo(Parent):
    def Two(self):
        print("I'm in ChildTwo Class.")
        
    def print_(self):
        pass
        
        
# obj = Parent()
# obj.test()                We can't Instantiation an abstract class
        
obj_1 = ChildTwo()
obj_1.test()
    
    