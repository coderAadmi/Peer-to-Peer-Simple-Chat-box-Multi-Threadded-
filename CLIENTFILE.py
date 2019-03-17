import socket
from threading import Thread
import time

IP = socket.gethostname()
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP,PORT))
print('Connected to ',IP)

def recv(client):
    run = True
    while True:
        try:
            msg = client.recv(1024)
            if msg:
                msg = msg.decode()
                print('socket: ',msg)
                if '$$QUIT' in msg:
                    run = False
                    print('Closing ....')

            time.sleep(1/40)

        except:
            pass


def start():
    run = True
    while run:
        try:
            msg = input()
            if '$$QUIT' in msg:
                run = False
                print('CLOSING>>>>')

            client.send(msg.encode())

            time.sleep(1/40)
        except:
            pass

t = Thread(target=recv, args=(client,))
t.start()

start()



