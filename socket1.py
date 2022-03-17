import socket

##########################################################
#                 Terminal coloring                      #
##########################################################


class BeautifyTerminal:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


##########################################################
#              Server-client for 1 connection            #
##########################################################

# Using AF_INET for TCP/IP connection, SOCK_STREAM for 2 parties connection, aka client and server 
# Using SOL_SOCKET for setting the SOCKET options (it's a socket layer), SO_REUSEADDR - allows duplicate binding 
# Duplicate binding is when the same IP and port could be used on different sockets at the same time  

backend = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
backend.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
backend.bind(('localhost', 1969))
backend.listen()

while True:
    print(f' {BeautifyTerminal.WARNING} \n Awaiting connection from the client \n {BeautifyTerminal.ENDC}')
    client_socket, client_address = backend.accept()
    print(f'{BeautifyTerminal.WARNING} Spotted connection from: {client_address} {BeautifyTerminal.ENDC}')

    while True:
        client_request = client_socket.recv(2048)

        # If no request under the binded address and port, wait for upcoming connection
        if not client_request:
            break

        else:
            response_for_client = f'\n Hey pal, you serving or just hanging out? I want some food 0____0 \n'.encode()
            client_socket.send(response_for_client)
    
    client_socket.close()
