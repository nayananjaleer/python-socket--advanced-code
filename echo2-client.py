#Client Code

import socket

HEADER = 64
PORT = 8092
SERVER = "192.168.56.1"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = " GOT DISCONNECT "

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def Client_send(message):
    message.encode(FORMAT)
    length_msg = len(message)
    length_send = str(length_msg).encode(FORMAT)
    length_send += b' ' * (HEADER - len(length_send) )
    client.send(length_send)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

Client_send("Hello SLIIT Students. How are you?")
Client_send("How is hacking?")
Client_send("Hello SLIIT Students. How is lockeddown?")

Client_send(DISCONNECT_MSG)
