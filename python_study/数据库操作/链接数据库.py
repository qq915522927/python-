from pymysql import *

try:
    conn = Connect(host='localhost',port=3306,database='my2',user='root',passwd='mysql',charset='utf8')
    cursor1 = conn.cursor()
    #sql = r'insert into students(name) values("点小二")'
    sql = 'select * from students where id=%s'
    id = 5
    count=cursor1.execute(sql,[id])
    print(count)
    conn.commit()

    cursor1.close()
    conn.close()
except Exception as e:
    print(e.message)
