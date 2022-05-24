class demo:
    def __init__(self, fname, lname):       # This is a constructor in python
        self.fname = fname
        self.lname = lname
        
    def email(self):
        print(f"Your email Address is : {self.fname}.{self.lname}@compny.com")


obj = demo("Mazhar", "Naseer")
obj.email()