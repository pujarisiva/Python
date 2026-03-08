def update_server_config(filepath, key, value):
    # Read the existing content from the server configuration file
    with open(filepath, 'r') as file:
        lines = file.readlines()


    #update the file configuration key value
    with open(filepath, 'w') as file:
        for line in lines:
            # check the line start with specific key
            if key in line:
                #update the line new value 
                file.write(key + "=" + value + "\n")
            else:
                #keep the existing line as it is
                file.write(line)  

server_config_file = "server.config"
key_up_to_date = "TIMEOUT"
new_value = "60"

update_server_config(server_config_file, key_up_to_date, new_value)