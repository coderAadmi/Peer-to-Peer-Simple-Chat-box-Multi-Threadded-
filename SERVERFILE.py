import socket
import time
from threading import Thread

IP = socket.gethostname()
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP,PORT))
server.listen()
client, addr = server.accept()
print('Connected to ',client)
client.setblocking(0)

def recv(client):
    run = True
    while run:
        try:
            msg = client.recv(1024)
            if msg:
                msg = msg.decode()
                print('client: ',msg)
                if '$$QUIT' in msg:
                    run = False
                    print('Closing ....')

            time.sleep(1/40)

        except:
            pass

def start():
    run = True
    while run:
        msg = input()
        if '$$QUIT' in msg:
            run = False
            print('Closing .....')
        client.send(msg.encode())

t = Thread(target=recv, args=(client,))
t.start()

start()


