import os

file = "text1.txt"

if os.path.exists(file):
    print(f"{file} File is exists")
else:
    print(f"{file} File not Exists")
