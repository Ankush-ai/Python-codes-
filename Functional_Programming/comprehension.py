#  list comprehension
list=[100,200,300,400,500]
l2=[value* value for value in list]
print(l2)

l = [10, 25, 30, 45, 60, 75]
l2 = ["Even" if value % 2 == 0 else "Odd" for value in l]
print(l2)

# Dictionary comprehension
squares_dict={num:num**2 for num in range(5)}
print(squares_dict)


# set comprehension
# Create a set of squares for numbers 0 to 4
squares_set = {num**2 for num in range(5)}
print(squares_set)