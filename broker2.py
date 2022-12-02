import socket
import threading
import sys
import time
import signal
import schedule

SERVER1 = socket.gethostbyname(socket.gethostname())
PORT1 = 5019
SERVER2 = socket.gethostbyname(socket.gethostname())
PORT2 = 5017
ADDR2 = (SERVER2, PORT2)
ADDR1 = (SERVER1, PORT1)
FORMAT = 'utf-8'
SERVER3 = 'localhost'       #for zookeeper
PORT3 = 5070
ADDR3 = (SERVER3, PORT3)

server1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server1.bind(ADDR1)
server2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server2.bind(ADDR2)

server3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server3.connect(ADDR3)

topics=[]
def heart_beat():
    while True:
        message = 'alive '  
        time.sleep(5)
        server3.send(message.encode())
         
    
thread = threading.Thread(target=heart_beat, daemon=True)
thread.start()

def server_program(conn,addr,conn1,addr1): 
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    
    while connected:
        topic = conn.recv(1024).decode(FORMAT)
        if topic not in topics:
            topics.append(topic)
        conn1.send(topic.encode(FORMAT))
            #conn1.send(topics.encode(FORMAT))
        message = conn1.recv(1024).decode(FORMAT)
        conn.send(message.encode(FORMAT))
        conn.close()
    conn1.close()
            

        # except KeyboardInterrupt:
        #     print("Interrupted")
        #     sys.exit(1)
        #     #quit()

    print("Topic is "+ str(topic))
    input()
    conn.close()
    conn1.close()

def active():

    server1.listen()
    server2.listen()

    print(f"[LISTENING] is listening on consumer {SERVER1}")
    print(f"[LISTENING] is listening on producer {SERVER2}")

    while True:
        conn, addr = server1.accept()
        conn1, addr1 = server2.accept()
            
        thread = threading.Thread(target=server_program, args=(conn, addr, conn1, addr1))
        thread.start()
            
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
        inp = input()
        try:
            server3.send(inp.encode())

        except KeyboardInterrupt:
            print("Interrupted")
            conn.close()
            conn1.close()
            sys.exit(1)
        
print("[STARTING] Broker1 is starting...")
active()

