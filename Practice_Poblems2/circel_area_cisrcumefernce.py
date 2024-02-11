import math
def circel_properties(radius):
    area=math.pi * radius **2
    circumference= 2 * math.pi * radius
    return area,circumference

radius=5
area,circumference = circel_properties(radius)
print(area)
print(circumference)

