#!/bin/bash

configure_monitor_agent() {
    echo "Installing monitoring agent on $1"
}
servers=("server1" "server2" "server3")

for server in "${servers[@]}"; do
    configure_monitor_agent "$server"
done