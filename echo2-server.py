#Server Code

import socket
import threading

PORT = 8096

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MSG = " GOT DISCONNECT "

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

#purpose of this function is to serve multiple clients
def incoming_clients(conn, addr):
    print("Client {addr} Connected ")

    condition = True
    while condition:
        length_msg = conn.recv(1024).decode(FORMAT)
        if length_msg:
            length_msg = int(length_msg)
            message = conn.recv(length_msg).decode(FORMAT)
            if message == DISCONNECT_MSG:
                condition = False
            print("{addr} {message}")
            conn.send("Message Received Loud and Clear".encode(FORMAT))

    conn.close()


#the function is to handle the server end
def setupServer():
    server.listen() #listening function
    print("SLIIT Echo Server is now listening : ")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread (target= XXXXXX , arg=(conn, addr))
        thread.start()
        print("[Incoming Connections] {threading.activeCount()-1}")


print("[Evil Server] is starting .....")
setupServer()

#print(socket.gethostname())    #get system name
#print(socket.gethostbyname(socket.gethostname()))  #get system ip address
