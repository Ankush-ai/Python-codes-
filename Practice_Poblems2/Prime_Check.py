def is_prime(num):
    if num <2:
        return False
    for i in range(2,int(num **0.5)+1):
        if num % i==0:
            return False
    
    return True

num=11
if is_prime(num):
    print("Prime Number")

else:
    print("Not a Prime Number")
  