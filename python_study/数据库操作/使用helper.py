import sys

#添加模块路径
sys.path.append('./')
import MysqlHelper

mysql = MysqlHelper.MysqlHelper(host='localhost',db='my2',user='root',passwd='mysql')
sql = 'insert into students(name) values(%s)'
params = '赵小六'
mysql.cud(sql,params)


mysql = MysqlHelper.MysqlHelper(host='localhost',db='my2',user='root',passwd='mysql')
sql = 'select * from students'

for n in mysql.all(sql):
    print(n)

