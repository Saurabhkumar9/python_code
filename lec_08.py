from abc import ABC, abstractmethod

# 141. Person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 142. Add greeting method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# 143. Car class with constructor
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# 144. Inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

# 145. Method overriding
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

# 146. Encapsulation
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private attribute

# 147. Getter and setter
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, value):
        if value > 0:
            self.__salary = value
        else:
            raise ValueError("Salary must be positive")

# 148. Polymorphism
class Cat:
    def sound(self):
        print("Meow")

def make_sound(animal):
    animal.sound()

dog = Dog()
cat = Cat()
make_sound(dog)
make_sound(cat)

# 149. Classmethod decorator
class MyClass:
    count = 0
    
    @classmethod
    def increment_count(cls):
        cls.count += 1

# 150. Staticmethod decorator
class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

# 151. __str__ and __repr__
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

# 152. Operator overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(3, 4)
print(v1 + v2)

# 153. Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
  

# 154. Bank Account class
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid amount")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount")

# 155. Track instantiated objects
class Tracked:
    count = 0
    
    def __init__(self):
        Tracked.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count

# 156. Singleton pattern
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# 157. Rectangle class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# 158. Circle class with property
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")
    
  

# 159. Multiple inheritance
class Flyable:
    def fly(self):
        print("Flying")

class Swimmable:
    def swim(self):
        print("Swimming")

class Duck(Flyable, Swimmable):
    pass

# 160. Use super() to call parent constructor
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age