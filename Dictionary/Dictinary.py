# Using keys(), values(), and items() for dictionaries
# Creating dictionaries
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

keys = my_dict.keys()  # Returns a view of all keys
values = my_dict.values()  # Returns a view of all values
items = my_dict.items()  # Returns a view of key-value pairs as tuples
print(keys)
print(values)
print(items)# Accessing and modifying
name = my_dict['name']  # Accesses the value associated with 'name'
my_dict['age'] = 26  # Modifies the value associated with 'age'
my_dict['gender'] = 'Male'  # Adds a new key-value pair
