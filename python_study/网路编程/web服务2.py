#1. 创建socket,绑定,改为被动模式
#2. 使用协程完成多任务，使用gevent模块
#3. 在recv 和send 之间对数据报进行解析，并返回符合http协议的数据报

#使用gevent,socket 需使用gevent 里的，同时需要导入monkey动态修改代码
import gevent
import re
from gevent import monkey,socket

#使用monkey进行动态监控 和修改
#静态文件目录
HTML_ROOT_DIR = './html'
monkey.patch_all()
def mk_reponse_msg(file_name):
    if '/' == file_name:
        file_name = '/index.html'
    try:
        file = open(HTML_ROOT_DIR+file_name,'rb')
    except IOError:
        response_start_line = "HTTP/1.1 404 NOT FOUND\r\n"
        reponse_header = "Sever: My server\r\n"
        reponse_body = bytes(u'文件到天上去了','utf8').decode('utf8')
    else:
        file_data = file.read()
        file.close()

        response_start_line = "HTTP/1.1 200 OK\r\n"
        reponse_header = "Sever: My server\r\n"
        reponse_body = file_data.decode('utf8')
    msg = response_start_line + reponse_header + '\r\n' + reponse_body
    print(msg)
    return msg
def handle_request(newSocket):
    request_data = newSocket.recv(1024).decode('utf8')

    #解析请求头数据
    request_lines = request_data.splitlines()
    request_start_line =request_lines[0]
    print(request_start_line)
    #GET /question/33404792.html HTTP/1.1
    #获取文件路劲
    file_dir = re.match(r'\w+\s(/[^\s]*)\s',request_start_line).group(1)

    print(request_data+'\n'+str(newSocket))
    response_data = mk_reponse_msg(file_dir)
    # newSocket.send(bytes(response_data,'utf8'))
    newSocket.send(response_data.encode('utf8'))
    #客户端链接要立马关闭 否则 浏览器一只刷新 短连接
    newSocket.close()
def main(port):
    sever_socket = socket.socket()

    sever_socket.bind(('',port))
    sever_socket.listen(5)
    print('正在%d端口运行...'%port)
    try:
        while True:
            newSocket,adr = sever_socket.accept()
            #携程切换，当有延时操作时自动切换
            gevent.spawn(handle_request,newSocket)
    finally:
        sever_socket.close()
if __name__=='__main__':
    main(9998)