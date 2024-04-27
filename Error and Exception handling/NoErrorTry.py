# this code shows that how the code execution continues in normal form as there are no errors in try block and except clause is skipped 
x=1
try:
    print(5/x)
except ZeroDivisionError:
    print("Something went wrong")


print("I am executing after try block")

# Errors in the Try Clause and the Exception is Specified
# If the code in the try clause does throw an exception and the type of exception is specified after any except keyword, the program will:

# Skip the remaining code in the try clause
# Execute any code in the matching except clause
# Continue running as normal

x=0
try:
    print(5/x)

except ZeroDivisionError:
    print("SOmething went wromg")

print("I am executing after try clause")