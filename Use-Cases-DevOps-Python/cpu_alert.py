import psutil

cpu = psutil.cpu_percent(interval=1)

if cpu > 80:
    print("CPU Usage High:", cpu)
else:
    print("CPU Usage low:", cpu)