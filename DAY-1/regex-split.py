import re

text = "apple,banana,grape,chia,flex"

pattern = r","

separate = re.split(pattern, text)
print("final output:", separate)
cd 