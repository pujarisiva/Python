import shutil

total, used, free = shutil.disk_usage("/")

print("total:",total // (2**30), "GB")
print("used:",used // (2**30), "GB")
print("free:",free // (2**30), "GB")