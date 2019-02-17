import pymysql
# 打开数据库连接  安装  pymysql   pip install pymysql
host = 'test.lemonban.com'
user = 'test'
password = 'test'
mysql = pymysql.connect(host=host, user=user, password=password, port=3306)

# 使用cursor()建立查询会话

cursor = mysql.cursor()

# 使用execute()方法执行SQL语句
sql = 'select max(mobilephone) from future.member'
cursor.execute(sql)

# 使用fetchone()获取一条数据
result = cursor.fetchone()

# 打印获取到的数据
print(result[0])

# 关闭查询
cursor.close()

#关闭连接
mysql.close()
