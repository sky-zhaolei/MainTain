import pymysql
from Common.setting import datas

class HandleDB:

    def __init__(self):
        #连接数据库，创建游标
        self.conn = pymysql.connect(
            host=datas["mysql"]["host"],
            port=datas["mysql"]["port"],
            user=datas["mysql"]["user"],
            password=datas["mysql"]["password"],
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cur = self.conn.cursor()

    def get_one_data(self, sql):
        self.conn.get_autocommit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    def get_all_data(self, sql):
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def get_count(self, sql):
        self.conn.commit()
        return self.cur.execute(sql)

    def update(self, sql):
        self.cur.execute(sql)
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()

if __name__ == '__main__':
    # sql = "SELECT * FROM dst_maintain.mt_store LIMIT 15"
    # db = HandleDB()
    # data = db.get_one_data(sql)
    # print("获取的第一条数据",data)
    # all = db.get_all_data(sql)
    # print("获取所有数据", all)
    # cot = db.get_count(sql)
    # print("输出获取的数据量", cot)
    # db.close()
    pass