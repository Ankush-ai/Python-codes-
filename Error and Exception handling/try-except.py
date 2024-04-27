# the try and except are the statements that are mainly used for dealing with exceptions .They look somthing like this 
x=0
try:
    print(5/x)
except ZeroDivisionError:
    print("something went wrong")