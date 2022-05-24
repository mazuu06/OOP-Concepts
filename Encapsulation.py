class Base:
    def __init__(self):
        self._a = 2          # this Protected member but we can access it from outside the class and in drived class
 

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling protected member of base class: ",
              self._a)
       
        self._a = 3          # Modify the protected variable:
        print("Calling modified protected member outside class: ",
              self._a)
        
obj = Derived()

obj_1 = Base()
print(obj_1._a)


# ********************************************************************************************************************

class Base:
    def __init__(self):
        self.__a = 2        # This is a private variable that we can't accesss outside the class and drived classes   
 

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling protected member of base class: ",self.__a)      # This will raise an error because it is calling a private veriable
     
        
obj = Derived()

# obj_1 = Base()
# print(obj_1.__a)            # This will raise an error because it is calling a private veriable