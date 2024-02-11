class Person:
    def __init__(self, name,age):
        self.name=name
        self.age=age

    def greet(self):
        print(f"hii my name is {self.name},and I am {self.age} years old")

person =Person("Ankush",23)
person.greet()