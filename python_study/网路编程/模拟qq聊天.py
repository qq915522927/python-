from threading import Thread
from socket import *
#1. 接收消息
def recvMsg():
    while True:
        msg = udpSocket.recvfrom(1024)
        print('\r>>%s::%s'%(str(msg[1]),msg[0].decode('gb2312'))+'\n'+'<<',end='')

#2. 发送消息
def sendMsg():
    while True:
        sendInfo = input('<<')
        udpSocket.sendto(sendInfo.encode('gb2312'),disAdr)

udpSocket = None
disAdr = ()

def main():
    global udpSocket
    global disAdr
    udpSocket = socket(AF_INET,SOCK_DGRAM)
    udpSocket.bind(('',3344))

    disIp = input('请输入对方ip')
    disPort = int(input('对方端口'))
    disAdr =(disIp,disPort)

    tr = Thread(target=recvMsg)
    ts = Thread(target=sendMsg)

    tr.start()
    ts.start()

    tr.join()
    ts.join()



if __name__ == '__main__':
    main()
