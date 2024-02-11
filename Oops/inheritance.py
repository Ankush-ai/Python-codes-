class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print("Woof!")

dog = Dog("Buddy")
print(dog.name)  # Output: Buddy
dog.bark()       # Output: Woof!
