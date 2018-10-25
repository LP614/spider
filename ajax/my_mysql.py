import pymysql
class MyMysql(object):
    def __init__(self, host, port, user, password, db, charset):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset
        # 链接数据
        self.connect()

    def connect(self):
        # 链接数据库和获取游标
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db, charset=self.charset)
        self.cursor = self.conn.cursor()
    
    def run(self, sql):
        # ret = None
        # try:
        ret = self.cursor.execute(sql)
        self.conn.commit()
        # except Exception as e:
        #     self.conn.rollback()
        # finally:
        #     self.close()
        # return ret
            
    # def close(self):
    #     self.cursor.close()
    #     self.db.close()
    
    def insert_info(self, sql):
        return self.run(sql)
    
    def update_info(self, sql):
        return self.run(sql)
    
    def delete(self, sql):
        return self.run(sql)
    
    def read_one(self, sql):
        ret = None
        try:
            self.cursor.execute(sql)
            # 获取得到数据
            ret = self.cursor.fetchone()
        except Exception as e:
            print('查询失败')
        finally:
            self.close()
        return ret
    
    def read_many(self, sql):
        ret = None
        try:
            self.cursor.execute(sql)
            # 获取得到数据
            ret = self.cursor.fetchall()
        except Exception as e:
            print('查询失败')
        finally:
            self.close()
        return ret