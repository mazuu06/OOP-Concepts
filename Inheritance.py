class cal:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def multi(self):
        print("Multiple of Two Numbers is : ", self.a*self.b)
        
        
class calculation(cal):         # Here we are inheriting methods of cal class
    def __init__(self, a, b):
        self.a = a
        self.b = b
            
    def sum(self):
        print("Sum of two numbers is : ", self.a+self.b)
        
        
        
    
        
obj = cal(5, 8)
obj.multi()

obj_1 = (calculation(7, 3))
obj_1.sum()
obj_1.multi()