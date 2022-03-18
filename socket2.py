import socket, select

# Select module allows us to access the objects when they are ready. If socket connection was established, system treats it as the object.
# We cant track the changes of the socket connection objects
# If the changes in the socket objects were made, we are going to take action, for example reply on the connection or accept connection.

# The fucntions will be seperated and independent from each other, both of them won't have while loops. Main event_handler fucntion will
# take actions depending of the socket objects and their states.


##########################################################
#                   Terminal coloring                    #
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
#          Server-client for multiple connections        #
#   The following code doesn't have blocking functions   #
##########################################################

# writing down the files into array from sockets
monitoring_sockets = []

backend = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
backend.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
backend.bind(('localhost', 1969))
backend.listen()


def accept_connection(backend):
    # accept method() -  returns new socket >> object << representing the connection 
    client_socket, client_address = backend.accept()
    print(f'{BeautifyTerminal.WARNING} Established connection from: {client_address} {BeautifyTerminal.ENDC}')
    monitoring_sockets.append(client_socket)


def reply_to_client(client_socket):
    client_request = client_socket.recv(2048)

    if client_request:
        response_for_client = f'\n There aren\'t enough love. Love everyone <3, even if they are toxic as hell. \n And yeah, it\'s okay to be stack overflow junkie while learning how to code.'.encode()
        client_socket.send(response_for_client)
    else:
        client_socket.close()
    

def main_event_loop():
    while True:
        # it's okay to leave write and error arrays empty, because we only need to read
        ready_socket_objects, write_sockets, random_errors = select.select(monitoring_sockets, [], [])
        
        for socket_object in ready_socket_objects:
            if socket_object is backend:
                accept_connection(socket_object)
            else:
                reply_to_client(socket_object)

if __name__ == '__main__':
    monitoring_sockets.append(backend)
    main_event_loop()