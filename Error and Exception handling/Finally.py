# Try and except are the main tools in handling errors, but an optional clause that you can use is named finally. The finally clause will always execute, whether there is an error or not.
x=0
try:
    print(5/x)
except ZeroDivisionError:
    print("I am in Except clause")
finally:
    print("I am in finally clause")
print("I am Executing after the try clause")

#  The other optional clause is the else clause. The else clause is simple: if the code in the try clause executes without throwing an error, then the code in the else clause will also execute.
x=1
try:
    print(5/x)
except ZeroDivisionError:
    print("I am in except clause")
else:
    print("I am in else clasue")
finally:
    print("I am in finally clause")

print("I am executing after try block")

