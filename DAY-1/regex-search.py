import re

text = "this is aws devops"

pattern = r"aws"

s = re.search(pattern, text)
if s:
    print("pattern found:", s.group())
else:
    print("pattern not found")