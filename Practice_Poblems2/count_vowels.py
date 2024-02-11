def count_vowels(str):
    vowels="aeiouAEIOU"
    return sum(1 for char in str if char in vowels)

word="AnkushSrivastava"
result=count_vowels(word)
print(result)