import os

def check_server(host):
    response = os.system(f"ping -c 1 {host}")

    if response == 0:
        print(f"{host} is Reachable")
    else:
        print(f"{host} is Not Reachable") 

check_server("google.com")           