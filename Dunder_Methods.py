######################################## __len__ Method#####################################
class LenExample:
    def __init__(self, item):
        self.item = item
    def __len__(self):
        return len(self.item)
len_instance = LenExample([1, 2, 3])
print(len(len_instance))


######################################## Relational Method#####################################

class Comparison:
    def __init__(self, a):
        self.a = a
    def __lt__(self, object2):
        return self.a < object2.a
    def __gt__(self, object2):
        return self.a > object2.a
    def __le__(self, object2):
        return self.a <= object2.a
    def __ge__(self, object2):
        return self.a >= object2.a
    def __eq__(self, object2):
        return self.a == object2.a
    def __ne__(self, object2):
        return self.a != object2.a
a = Comparison(1)
b = Comparison(2)
print(
    a < b,
    a > b,
    a <= b,
    a >= b,
    a == b,
    a != b
)

######################################## str & repr Method#####################################

class Person:

    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age

    def __str__(self):
        return f'Person name is {self.name} and age is {self.age}'

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'


p = Person('Pankaj', 34)

print(p.__str__())
print(p.__repr__())
