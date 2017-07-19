from socket import *
udpsocket = socket(AF_INET,SOCK_DGRAM)
sendAdr = ('192.168.99.173',8080)
msg = input('输入信息')
udpsocket.sendto(msg.encode('gb2312'),sendAdr)
