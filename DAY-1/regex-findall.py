import re

text = "the quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("pattern found:", search.group())
else:
    print("pattern not found")    

words = "Final tables has been received successfully"
pat = r"tables"

search = re.search(pat,words)
if search:
    print("pat found:", search.group())
else:
    print("pat not found")   
