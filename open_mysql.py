"""
1、连接数据库
2、执行sql语句
3、获取执行的结果
4、关闭数据库连接
"""
import pymysql
from Common.setting import datas
#建立连接

host = datas["mysql"]["host"]
port = datas["mysql"]["port"]
user = datas["mysql"]["user"]
password = datas["mysql"]["password"]

print(host, port, user, password)

conn = pymysql.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


#创建游标
cur = conn.cursor()

#执行sql语句
sql = "SELECT * FROM dst_maintain.mt_store LIMIT 15"
count = cur.execute(sql)   #返回sql语句执行结果的行数

#获取sql语句执行的结果
one = cur.fetchone()  #获取结果集当中一条数据
print("第一条数据", one)
two = cur.fetchone() #第一条取出后，获取第二条数据
print("获取第二条数据", two)
many = cur.fetchmany(10) #获取任意条数数据（此处获取10条）
print("获取十条数据", many)
all = cur.fetchall() #获取全部数据
print("获取剩余所有数据", all)

#关闭游标，关闭数据库
cur.close()
conn.close()
