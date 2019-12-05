import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 9000))
with open("./../src/2018-example.csv") as f:
    for i, line in enumerate(f):  
        time.sleep(1)           
        print "line {0} = {1}".format(i, line.split())
        client.send(line)
from_server = client.recv(4096)
client.close()
print from_server
