from socket import *
cSocket = socket(AF_INET,SOCK_STREAM)
cSocket.connect(('192.168.99.173',8899))
while True:
    msg = input('输入')
    cSocket.send(msg.encode('gb2312'))
    recvData = cSocket.recv(1024).decode('gb2312')
    print(recvData)
    if recvData == 'end':
        break
    else:
        pass
cSocket.close()
