
import socket

IP = "127.0.0.1" #loopback
PORT = 8093 #select greater than 1023 - non-privilaged ports > 1023
AMT_DATA = 64

#socket() function 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mySocket:
    #connect()
    mySocket.connect((IP, PORT))
    mySocket.sendall(b"Hello from SLIITm -->")
    data = mySocket.recv(AMT_DATA)

print("Received with Thanks : ", repr(data))