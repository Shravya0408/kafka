
import socket
import threading
import os

PORT = 5017
SERVER = "192.168.27.1"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

producer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
producer.connect(ADDR)


"""def receive():
    while True:
        topic = producer.recv(1024).decode(FORMAT)
        #topics = producer.recv(1024).decode(FORMAT)

        print("Topic chosen: "+ str(topic))
        directory = 'C:/Users/Shravya U/Desktop/PROJECT'
        for root, dirs, files in os.walk(directory):
            for f in files:

        f = open(topic+".txt","r")
        existing=f.read()
        f.close()
        producer.send(existing.encode(FORMAT))
        
        break"""

def receive1():
    topic = producer.recv(1024).decode(FORMAT)
    print("Topic chosen: "+ str(topic))
    message = input("Enter message to publish: ")
        #print(message)
    producer.send(message.encode(FORMAT)) 
    producer.close()

# receive_thread = threading.Thread(target=receive)
# receive_thread.start()
receive_thread1 = threading.Thread(target=receive1)
receive_thread1.start()

#receive()
#receive1()
