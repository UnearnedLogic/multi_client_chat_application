import socket
import threading

nickname = input("Choose your nickname: ")

host = '127.0.0.1'
port = 9090

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host,port))



def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("Disconnected from the server!")
            client.close()
            break

def write():
    while True:
        text = input("")
        message = f'{nickname}: {text}'
        if text == '/quit':
            client.send('/quit'.encode('ascii'))
            client.close()
            break
        else:
            client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()


write_thread = threading.Thread(target=write)
write_thread.start()