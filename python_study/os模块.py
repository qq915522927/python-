#os模块提供了操作系统对文件操作的接口调用

import os
a = os.path.join('\\user','login')#拼接路径
print(a)

a = os.path.abspath('.')
print(a)
# os.mkdir('test')#可以是绝对路径和相对路径

a = os.path.split('/user/login/login.html') #拆分路径，返回元组，后一部分为最后级别的文件或目录
print(a)

a = os.path.splitext('/user/login/login.html')#获得扩展名，返回元祖，后一部分为扩展名
print(a)

#os.rename('test.txt','test.py')#重命名
#os.remove('test.txt') 删除

a = os.listdir('.')#列出当前目录下的所有文件目录
print(a)
#配合列表生成式,列出所有py文件
a=[x for x in os.listdir('.') if os.path.splitext(x)[1]=='.py']
print(a)