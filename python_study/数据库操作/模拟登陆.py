from MysqlHelper import  MysqlHelper


name = input('用户名')
pwd = input('密码')
#实际要加密
sql='select * from user where name=%s and passwd=%s'

mysql = MysqlHelper(host='localhost',db='user',user='root',passwd='mysql')
result = mysql.all(sql,(name,pwd))
print(result)
if result:
    print('ok')
else:
    print('false')