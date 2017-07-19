from socket import*
udpSocket = socket(AF_INET,SOCK_DGRAM)
s = ('',7788)
udpSocket.bind(s)
while True:
    data = udpSocket.recvfrom(1024)
    print (str(data[1])+'---:'+data[0].decode('gb2312'))
    udpSocket.sendto(data[0],data[1])
udpSocket.close()

