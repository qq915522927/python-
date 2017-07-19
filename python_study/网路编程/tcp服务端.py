from socket import *

tcpSocket = socket(AF_INET,SOCK_STREAM)
tcpSocket.bind(('192.168.99.147',8899))
tcpSocket.listen(5)
print('等待链接')
newSocket,adr = tcpSocket.accept()

print('链接完成，等待数据')
recvData = newSocket.recv(1024)
print(recvData.decode('utf8'))
print('数据接受完成')

newSocket.send(recvData)
newSocket.close()
tcpSocket.close()

