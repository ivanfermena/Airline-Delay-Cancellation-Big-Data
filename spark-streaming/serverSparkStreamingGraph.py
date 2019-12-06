from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import socket
from io import StringIO
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import pandas as pd

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

xar = []
yar = []

def proccessSpark(sc, ssc, line):

    names_col = ["FL_DATE","OP_CARRIER","OP_CARRIER_FL_NUM","ORIGIN","DEST","CRS_DEP_TIME","DEP_TIME","DEP_DELAY", \
    "TAXI_OUT","WHEELS_OFF","WHEELS_ON","TAXI_IN","CRS_ARR_TIME","ARR_TIME","ARR_DELAY","CANCELLED","CANCELLATION_CODE", \
        "DIVERTED","CRS_ELAPSED_TIME","ACTUAL_ELAPSED_TIME","AIR_TIME","DISTANCE","CARRIER_DELAY","WEATHER_DELAY","NAS_DELAY", \
        "SECURITY_DELAY","LATE_AIRCRAFT_DELAY", "Unnamed"]
    df = pd.read_csv(StringIO(line), names=names_col)

    xar.append(df['DEP_TIME'])
    yar.append(df['DEP_DELAY'])

    ax1.clear()
    ax1.plot(int(xar), int(yar))

    return df.to_string()

def Main():
    host = "localhost"
    port = 9999
    
    mySocket = socket.socket()
    mySocket.bind((host,port))

    # Create a local StreamingContext with two working thread and batch interval of 1 second
    sc = SparkContext("local[2]", "NetworkWordCount")
    ssc = StreamingContext(sc, 3)
     
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
        data = conn.recv(1024).decode()

        if not data:
            break
            
        #data_process = proccessSpark(sc, ssc, data)

        ani = animation.FuncAnimation(fig, proccessSpark(sc, ssc, data), interval=3000)
        plt.show()

        conn.send(data_process.encode())
             
    conn.close()
     
if __name__ == '__main__':
    Main()




