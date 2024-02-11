def is_palindrome(s):
    return s == s[::-1]

string_input = input("Enter a string: ")

if is_palindrome(string_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
