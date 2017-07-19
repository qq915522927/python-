from socket import *
import struct
import time
sendMsg = struct.pack('!H8sb5sb',1,b'test.jpg',0,b'octet',0)

udpSocket = socket(AF_INET,SOCK_DGRAM)
#发送下载请求
udpSocket.sendto(sendMsg,('192.168.99.173',69))
f = open('test.jpg','wb')

while True:
    filePart = udpSocket.recvfrom(1024)
    print('正在下载...')
    disAdr = filePart[1]
    dataPack = filePart[0]
    f.write(dataPack[4:])
    #n1为操作码，n2为块编码
    n1,n2 = struct.unpack('!2H',dataPack[:4])
    callbackMsg = struct.pack('!2H',4,n2)
    udpSocket.sendto(callbackMsg,disAdr)
    if len(dataPack) == 516:
        pass
    else:
        print('下载完成！')
        break

f.close()
