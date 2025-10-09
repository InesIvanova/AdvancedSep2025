class Person:
    def __init__(self, name):
        self.name = name

person = Person('Peter')
print(person.name)
del person.name
print(delattr(person, 'name'))     # None
print(person.name)