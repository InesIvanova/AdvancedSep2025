from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "woof-woof"


class Cat(Animal):
    def make_sound(self):
        return "meow"


class Pig(Animal):
    def make_sound(self):
        return "pig sound"


class Turtle(Animal):
    def make_sound(self):
        return "turtle sound"

def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Dog(), Cat(), Pig(), Turtle()]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, {self.name}, I am {self.age} years old."


class Student(Person):
    def greet(self):
        result = super().greet()
        return result + " and I am student"