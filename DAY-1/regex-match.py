import re

text = "This is final warning to stop the deployment"
pattern = r"warning"

word = re.match(pattern, text)
if word:
    print("final word:", word.group())
else:
    print("final word not found")

    