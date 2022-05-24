class Salary:
    def __init__(self, pay):
        self.pay = pay
 
    def get_total(self):
        return (self.pay*12)
 
 
class Employee:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
 
    def annual_salary(self):
        return "Total: " + str(self.pay.get_total() + self.bonus)
 
 
obj_sal = Salary(600)
obj_emp = Employee(obj_sal, 500)            # here we are using obj_sal variable as a parameter
print(obj_emp.annual_salary())