class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # Fuel capacity in gallons
        self.fuel_capacity = 15
        self.fuel_level = 0  # Initialize fuel level to 0

    def fill_tank(self):
        """Fill gas tank to capacity"""
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full")

    def drive(self):
        """Simulate driving"""
        if self.fuel_level > 0:
            print("Car is moving")
            self.fuel_level -= 1  # Simulate fuel consumption
        else:
            print("Car can't drive, it's out of fuel!")

# Making objects from a class
my_car = Car('Audi', 'A4', 2016)

# Accessing attribute values
print(my_car.make)
print(my_car.model)
print(my_car.year)

# Calling methods
my_car.fill_tank()
my_car.drive()


# Modifying Attributes
# We can modify an atributes value directly, or we can write methods that manage updating values more carefully

my_new_car=Car('audi','a5','2020')
my_new_car.fuel=_level=5

# Writing method to update the attribute's value
def update_fuel_level(self,new_level):
    # """updated fuel level"""
    if new_level<=self.fuel_capacity:
        self.fuel_level=new_level
    else:
        print("The tank cannot hold that much")
