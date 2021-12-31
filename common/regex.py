import re

# Find all spaces
re.findall(r"\s+", "Let's write RegEx!")

# Find all the words
re.findall(r"\w+", "Let's write RegEx!")

# Find all the lowercase letters [a-z]
re.findall(r"[a-z]", "Let's write RegEx!")

# Find all the letters
re.findall(r"\w", "Let's write RegEx!")

# Split my_string on sentence endings and print the result
print(re.split(sentence_endings, my_string))

# Find all capitalized words in my_string and print the result
capitalized_words = r"[A-Z]\w+"
print(re.findall(capitalized_words, my_string))

# Split my_string on spaces and print the result
spaces = r"\s+"
print(re.split(spaces, my_string))

# Find all digits in my_string and print the result
digits = r"\d+"
print(re.findall(digits, my_string))
