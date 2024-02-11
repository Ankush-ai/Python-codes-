s1="hello world"
s2='hello world'
print(s1)
print(s2)


# slicing
string="Python is poewerfull"
res=string[7:10]
print(res)

# splitting using split()
str="Python is crazy"
split_res=str.split()
print(split_res)

# stringing
str1="Pythin is wonderfull"
stride_res=str1[::2]
print(stride_res)

# reversing a string
string="hellow python"
result_new=string[::-1]
print(result_new)

# length
length=len("Hello World")

# upper and lower case
text="Python is verstatile language"
res_text=text.upper()
res_text2=text.lower()
print(res_text)
print(res_text2)

def rev_string(str):
    str=input("Enter a string")
    res=str[::-1]
outp=rev_string(res)
print(outp)