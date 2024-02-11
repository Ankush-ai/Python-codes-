class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"{self.make} {self.model}")



car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Accord")

car1.display_info()  # Output: Toyota Camry
car2.display_info()  # Output: Honda Accord
