import psutil

memory = psutil.virtual_memory()

print("Total Memory:",memory.total)
print("Used Memory:",memory.used)