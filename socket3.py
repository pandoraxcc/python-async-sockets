import socket, selectors



# Selectors is the abstract module of selector, allowing us to do the same thing - check the state of the object by it's index and data.
# In order to track the data, we need to register it. After the required actions completed, it's always good to unregister and close the socket as usually.

# The main loop will be shortened thanks to selectors abstraction.

# Deafault alias for selector operations
selector = selectors.DefaultSelector()

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

def server():
    backend = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    backend.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    backend.bind(('localhost', 1969))
    backend.listen()

    selector.register(fileobj=backend, events=selectors.EVENT_READ, data=accept_connection)


def accept_connection(backend):
    client_socket, client_address = backend.accept()
    print(f'{BeautifyTerminal.WARNING} Established connection from: {client_address} {BeautifyTerminal.ENDC}')

    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=reply_to_client)

def reply_to_client(client_socket):
    client_request = client_socket.recv(2048)

    if client_request:
        response_for_client = f'(Urban Dictionary) The fuckening - when your day is going too well and you don\'t trust it and some shit finally goes down...'.encode()
        client_socket.send(response_for_client)
    
    else:

        # If there is no request, we don't track/read changes on client_socket object
        #Unregister  
        selector.unregister(client_socket)

        #Close socket
        client_socket.close()
    

def main_event_loop():

    # Continiously check for events
    while True:

        # Getting events from abstract class select
        # Events include tuples with each registered object key
        events = selector.select()

        # Default approach used from https://docs.python.org/3/library/selectors.html 
        for key, event_mask in events:
            # We are getting the function that is going to be invoked
            callback = key.data

            # Invoke the function with the argument client_socket or backend aka server socket
            callback(key.fileobj)

        # Getting all the 

if __name__ == '__main__':
    server()
    main_event_loop()