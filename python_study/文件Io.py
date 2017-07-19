#Io操作只对输入输出流的操作，如读取文本信息，接收网路数据等

with open('多重继承.py','r',encoding='utf8') as f:
    print(f.read(111))
    print(f.readline())
    print(f.readlines())

    #从结果可以看出 读取是有指针标记的


