my_list=['apple','banana','mango',3.14]
first_element=my_list[0]
print(first_element)

# slicing
subset=my_list[2:5]
print(subset)

# reverse
my_list[::-1]
print(my_list)
rev=my_list.reverse()
print(my_list)

# appending
my_list.append('orange')
print(my_list)

# extending
my_list.extend([100,200,300])
print(my_list)

length=len(my_list)
print(length)

# indexing
index1=my_list.index('apple')

# counting
count1=my_list.count(3)
print(count1)

# removing and poopig
item1=my_list.remove('banana')
item2=my_list.pop(2)
print(my_list)
print(item1)
print(item2)

# sorting
my_list.sort()
print(my_list)