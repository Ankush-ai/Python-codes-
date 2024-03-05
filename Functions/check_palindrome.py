def is_palindrome(s):
    s = s.lower()  # Convert to lowercase for case-insensitivity
    return s == s[::-1]
