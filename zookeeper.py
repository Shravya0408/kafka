
from subprocess import *
import subprocess
import time
import socket
import threading
import sys 
import random

def zookeeper():
    host = 'localhost'
    port = 5070  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together
    server_socket.listen()
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if data !='':
            print("from connected broker: " + str(data))
        elif data =='':
            print("BROKER IS DEAD")
            conn.close()
            sys.exit()  
            break
        # receive data stream. it won't accept data packet greater than 1024 bytes
        """
        x = conn.recv(1024).decode()
        if x==KeyboardInterrupt:
            print("BROKER IS DEAD")
            break
        if data==KeyboardInterrupt:
            print("BROKER IS DEAD")
            break
        print("from connected broker: " + str(data))
    conn.close()  # close the connection"""



if __name__ == '__main__':
    zookeeper()














'''''
def handle_client(client):
    while True:
        try:
            heartbeat = serverSocket.recv(1024).decode()
            print(heartbeat)
        except:
            serverSocket.remove(client)
            serverSocket.close()
            break

def receive():
    while True:
        print('Server is running and listening ...')
        client,address = serverSocket.accept()
        print(f'connection is established with {str(address)}')
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


if __name__ == "__main__":
    receive()
'''
'''
p= subprocess.Popen('python3 broker1.py')
time.sleep(3)
p.kill()
print("killed")
time.sleep(3)
#pick random
if 'broker2.py':
    q = Popen('python3 broker2.py')
else:
    r = Popen('python3 broker3.py')
    

'''


