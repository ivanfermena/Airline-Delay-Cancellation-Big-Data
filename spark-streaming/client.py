import socket
import time
 
def Main():
        host = 'localhost'
        port = 5000
         
        mySocket = socket.socket()
        mySocket.connect((host,port))
         
        while 1:
            with open("/home/ivanfermena/Documents/ucm/bigdata-airline-delay-cancellation/src/data/2018-example.csv") as fp:
                line = fp.readline()
                while line:
                    time.sleep(1)
                    line = fp.readline()
                    #mySocket.send(line.strip().encode())
                    data = mySocket.recv(1024).decode()

                    print ('Data csv: ' + data)

                    
                 
        mySocket.close()
 
if __name__ == '__main__':
    Main()