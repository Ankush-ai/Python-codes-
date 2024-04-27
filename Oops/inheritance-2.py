from Car import Car  # Assuming Car class is in a separate file named "Car.py"

class ElectricCar(Car):
    """A simple model of an electric car"""

    def __init__(self, make, model, year):
        """Initialize an electric car"""
        super().__init__(make, model, year)

        # Attributes specific to electric car
        # Battery in kWh
        self.battery_size = 70
        self.charge_level = 0

    # Adding new methods to child class
    def charge(self):
        """Fully charge vehicle"""
        self.charge_level = 100
        print("The vehicle is successfully charged")

# Using child methods and parent methods
my_ecar = ElectricCar('Tesla', 'Model S', 2020)
my_ecar.charge()
my_ecar.drive()
