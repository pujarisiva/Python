import re

text = "method is a built-in string function used to break a string into a list of substrings based on a specified delimiter"
pattern = r"break"

word = re.search (pattern, text)
if word:
    print("found pattern:", word.group())
else:
    print("Not Found pattern:")