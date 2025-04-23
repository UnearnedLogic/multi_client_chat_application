import socket
import threading

# Prompt the user to choose a nickname
nickname = input("Choose your nickname: ")

# Server connection settings
host = '127.0.0.1'  # Server's IP address
port = 9090         # Server's port number

# Create and connect the client's socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Socket for TCP connection
client.connect((host, port))  # Connect to the server


# Function to receive messages from the server
def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')  # Receive and decode a message from the server
            if message == 'NICK':  # If the server asks for a nickname
                client.send(nickname.encode('ascii'))  # Send the user's chosen nickname
            else:
                print(message)  # Print any other messages from the server
        except:
            # Handle unexpected disconnection from the server
            print("Disconnected from the server!")
            client.close()  # Close the connection
            break

# Function to send messages to the server
def write():
    while True:
        text = input("")  # Get user input
        message = f'{nickname}: {text}'  # Format the message with the user's nickname
        if text == '/quit':  # If the user types the quit command
            client.send('/quit'.encode('ascii'))  # Notify the server
            client.close()  # Close the connection
            break
        else:
            client.send(message.encode('ascii'))  # Otherwise, send the message to the server

# Start a thread to handle receiving messages
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# Start a thread to handle sending messages
write_thread = threading.Thread(target=write)
write_thread.start()