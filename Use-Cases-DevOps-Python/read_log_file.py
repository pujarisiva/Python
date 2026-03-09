with open ("text1.txt") as f:
    for line in f:
        if "world" in line:
            print(f"{line} is found")
        else:
            print(f"{line} is not found")