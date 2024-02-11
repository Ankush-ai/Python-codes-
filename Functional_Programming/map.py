def square_numbers(num):
    sq_num=map(lambda x: x**2,num)
    return (list)(sq_num)

num=[1,2,3,4,5,6,7,8,9,10]
result=square_numbers(num)
print(result)