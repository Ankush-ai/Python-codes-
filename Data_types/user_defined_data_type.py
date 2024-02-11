#Classe Data type is a user defined data type in python, a collection of objects or a blueprint where instaces can be created
# An instance or an object is an identiafiable entity having some charecrterstics and behavior


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an instance of the Person class
person1 = Person("Bob", 28)

print("Person's name:", person1.name)
print("Person's age:", person1.age)
