from socket import *
from threading import Thread



def sendMsg(clientSocket):
    while True:
        msg = input('>>')
        clientSocket.send(msg.encode('utf8'))

def recvMsg(clientSocket):
    while True:
        msg = clientSocket.recv(1024)
        print('\r>>%s'%msg.decode('utf8'))

def main():

    clientSocket = socket(AF_INET,SOCK_STREAM)

    clientSocket.connect(('192.168.99.173',9999))

    tr = Thread(target=recvMsg,args=(clientSocket,))
    ts = Thread(target=sendMsg,args=(clientSocket,))

    tr.start()
    ts.start()

if __name__ == '__main__':
    main()
