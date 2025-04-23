import socket
import threading

# Server setup
host = '127.0.0.1'  # Localhost IP address
port = 9090         # Port number to listen on

# Create and configure the server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Socket for TCP connection
server.bind((host, port))  # Bind the server to the specified host and port
server.listen()  # Start listening for incoming connections

# Lists to store connected clients and their nicknames
clients = []
nicknames = []

# Function to broadcast messages to all connected clients
def broadcast(message):
    for client in clients:  # Iterate through all connected clients
        client.send(message)  # Send the message to each client

# Function to handle communication with a specific client
def handle(client):
    while True:
        try:
            message = client.recv(1024)  # Receive a message from the client
            decoded_message = message.decode('ascii')  # Decode the message
            if decoded_message == '/quit':  # Check if the client wants to disconnect
                index = clients.index(client)  # Get the index of the client
                nickname = nicknames[index]  # Retrieve the client's nickname
                
                # Remove the client and their nickname from the lists
                clients.remove(client)
                nicknames.remove(nickname)

                # Notify everyone about the client's disconnection
                broadcast(f'{nickname} left the chat!'.encode('ascii'))
                client.close()  # Close the client's connection
                break
            else:
                # Broadcast the message to all connected clients
                broadcast(message)  # Send bytes directly
        except:
            # Handle unexpected disconnection
            pass

# Function to accept and manage incoming connections
def receive():
    while True:
        client, address = server.accept()  # Accept a new client connection
        print(f"Connected with {str(address)}")  # Print the client's address

        # Request the client's nickname
        client.send('NICK'.encode('ascii'))  # Send 'NICK' to request a nickname
        nickname = client.recv(1024).decode('ascii')  # Receive and decode the nickname
        nicknames.append(nickname)  # Add the client's nickname to the list
        clients.append(client)  # Add the client's socket to the list

        # Notify all users about the new connection
        print(f"Nickname of the client is {nickname}")  # Print the client's nickname
        broadcast(f'{nickname} joined the chat!'.encode('ascii'))  # Notify all about the new user
        client.send('Connected to the server!'.encode('ascii'))  # Send a welcome message to the client

        # Start a thread to handle the new client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()  # Run the server's receive function