import random
def gen_password():
    l=["@","$","#","&","/","%"]
    upper = chr(random.randint(65, 90))
    lower = chr(random.randint(97, 122))
    digit = str(random.randint(10000, 99999))
    special = random.choice(l)
    password = upper + lower + special + digit
    return password

result = gen_password()
print(result)
