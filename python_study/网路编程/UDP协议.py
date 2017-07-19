from socket import*
import time
usocket = socket(AF_INET,SOCK_DGRAM)
while True:
    usocket.sendto(b'hello',('192.168.99.173',8080))
    time.sleep(1)
