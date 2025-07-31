import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occurred. You have been disconnected.")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))

recv_thread = threading.Thread(target=receive)
recv_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()