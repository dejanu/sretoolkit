#!/bin/bash
## #####################################################################
## run concurrently command passed as argv on multiple remote servers ##
## UPDATE: servers array and user variable                            ##
########################################################################
# define an array of remote servers
servers=("server1.fqdn" "server2.fqdn" "server3.fqdn")
# Function to execute command on a remote server
execute_command() {
    server=$1
    command=$2
    # define user for the ssh connection 
    ssh user@"$server" "$command"
}

for server in "${servers[@]}"
do
    # exec arg command as background process
    execute_command "$server" "$1" &
done
# wait for all background processes to complete
wait