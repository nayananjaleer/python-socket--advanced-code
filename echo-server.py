import socket 

IP = "127.0.0.1" #loopback
PORT = 8093 #select greater than 1023 - non-privilaged ports > 1023
AMT_DATA = 64

#create socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mySocket:

    #bind the socket with proper IP and a port

    mySocket.bind((IP, PORT)) #bind done

    #listening socket

    mySocket.listen()

    #blocking mode(wait in blocking mode until get a connection from client side)

    conn, addr = mySocket.accept() 

    with conn:
        print("connected by : ", addr)
        while True:
            data = conn.recv(AMT_DATA)
            if not data:
                break
            conn.sendall(data) #echo server

    #send and receive data