===> Constructor ?
Constructor is a special type of method that called automatically when an object is ceated. In python __init__ method is used as a constructor.
 
===> Inheritance ?
Inheritance is a concept in object oriented programming in which we can use all the methods and properties of one class into another class.
The Parent class is known as base class,child class is known as derived class.
Inheritance is (is a) Relationship.
There is three types of inheritance.
	-> 1) Single inheritance 
	-> 2) Multi level inheritance
	-> 3) Multiple inheritamce

--> When we use only one class properties and methods into another class is called single inheritance.
--> When we use one class properties and methods into second class and then inherit second class into third class known as multiple inheritance.
--> When we use multiple classes properties and methods into one class called multiple inheritance. 

===> Method overriding ?
When we inherit a method from another class and that class also have same method.It will use derived class method.


===> Instance variable vs class variable?
variables or properties of an object or instance called istance variable.
variables or properties of a class called class variable.

===> Dunder Methods ?
A special type of methods that start and end with double underscore known as dunder methods.
For example : 
	__str__
	__init__
	__getattr__
	
===> Decorators ?
A special functions Properties use in methods called decoretors. It is start with @ symbol. 
For Example :
	@classmethod

====> Composition?
A class which contanis an object of an other class are known as compostion.
composition is (has a) relationship.
A class which have an object of an other class called composite.
A class which instance created in composite class known as component class.

====> UML?
Unified modeling language(UML) is a modeling language that is used to visualize the design of program.

====> Abstract Base Class?
A  class which have one or more abstacrt methods known as abstract base class.

====>  Interface Inheritance:
The derived class inherit all the methods,properties and atributes of the base class is known as implementation inheritance.

====> Implementation Inheritance?
The derived class inherits all the code that implemented in drive class interface.

====> What is Duck Tiping?
"If it walks like a duck it quacks like a duck,it must be a duck"
Duck Typing is a concept in which program does not check which type of an object created,it just check the presence of particular method.

====> Class Explosion Problem?
Sometime by using inheritance,it will create a huge hieraichal structure that is hard to maintain and understand.It is known as class explosition.

====> What is __MRO__?
Method Resolution order(__MRO__).It is method to see the flow of program which is develop by using inheritance.It returns a order to track programe flow.

====> Diamond problem in Inheritance?
If we using multiple inheritance some time we use two base classes in a class that base classes have a same their base class that is known as Diamond problem in inheritance.

====> Liskov's Substitution Principal?
It stated that if there is a class A,The base class of class B.If we replace class B in place of Class A,The Programe output never change.This Process is known as liskov's Substitution Principal.

====> Where we cannot use Inheritance?
IF Liskov's Substitution Principal is true for two classes then we cannot use Inheritance Between Two Classes.

=====>Interface?
An interface is an abstract class which contain only abstract methods but not a single concrete method.

====> Concrete Method?
All methods that we use in class instead of abstract method clled concrete methods.

====> Abstract Method?
An Abstract method is a method that has a declaration but does not have an implementation.There is no any built in abstract method creating thing in python. We use ABC module for using abstract method.
	1:We can not instanciate abstract base class because obj o abstract base class does not created.
	2:If an other class derived frm abstract base class,it must have abstract method.

===> Mixin ?
It is not a new thing. It is just a way to perform inheritance in a specific way.

===> Inheritace vs Composition ?
If our classes relation is (is a) relationship we use inheritance. If our classes relation is (has a) relationship we use composition.

