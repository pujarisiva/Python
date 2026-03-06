import re

text = "this is aws learning for the aws scope"

pattern = r"aws"

replace = "azure"

new_text = re.sub(pattern, replace, text)
print("final data:", new_text)
