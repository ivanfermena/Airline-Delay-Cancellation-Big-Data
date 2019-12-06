import socket
 
def Main():
    host = "localhost"
    port = 5000
     
    mySocket = socket.socket()
    mySocket.bind((host,port))
     
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while 1:
        data = conn.recv(1024).decode()
        print(data)
        if not data:
            break

        print ("from connected  user: " + str(data))
             
        data = str(data).lower()
        print ("sending: " + str(data))
        conn.send(data.encode())
             
    conn.close()
     
if __name__ == '__main__':
    Main()