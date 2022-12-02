import socket
import threading

PORT = 5019
SERVER = "192.168.27.1"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


topic = input("Enter your topic: ")
client.send(topic.encode(FORMAT)) 

"""def receive():
    while True:
        existing= client.recv(1024).decode(FORMAT)
        print("Message already published by the producer: "+str(existing))
        break"""
     

def receive1():
    message = client.recv(1024).decode(FORMAT)
            #print(message)
    print("Message received from the producer: "+str(message))
    f = open(topic+".txt","a+")
    f.write(message+"\n")
    f.close()
    client.close()
        

receive_thread = threading.Thread(target=receive1)
receive_thread.start()
# receive_thread1 = threading.Thread(target=receive1)
# receive_thread1.start()
#receive()
#receive1() 
