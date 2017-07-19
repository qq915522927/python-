#对数据v库的操作进行简单封装

from pymysql import *

class MysqlHelper(object):
    def __init__(self,host,db,user,passwd,charset='utf8',port=3306,):
        self.host = host
        self.db = db
        self.user =user
        self.passwd = passwd
        self.charset = charset
        self.port = port

    def open(self):
        '''打开连接和创建cusor'''
        self.conn = Connect(host=self.host,
                            database=self.db,
                            user=self.user,
                            passwd=self.passwd,
                            charset=self.charset,
                            port=self.port)
        self.cusor = self.conn.cursor()

    def close(self):
        self.cusor.close()
        self.conn.close()

    def cud(self,sql,params):
        '''增 删 改 需要提交事务的操作'''
        self.open()
        self.cusor.execute(sql,params)
        self.conn.commit()
        self.close()

    def all(self,sql,params=[]):
        '''返回所有结果'''
        self.open()
        self.cusor.execute(sql,params)
        result = self.cusor.fetchall()
        self.close()
        return result

    def first(self):
        pass