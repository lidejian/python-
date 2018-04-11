# -*- coding:utf-8 -*-
import sqlite3


# 进行数据库的连接
def connect(database = "test.db"):
    conn = sqlite3.connect(database)
    try:
        # 初次建立comments数据表
        c = conn.cursor()
        c.execute('''
                    CREATE TABLE COMMENTS
                       (ID INT PRIMARY KEY     NOT NULL,
                       NAME           TEXT    NOT NULL,
                       COMMENT        TEXT    NOT NULL,
                       TIME           TEXT    NOT NULL);
                  ''')
        print("表COMMENTS建立成功")
        conn.commit()
    except:
        print("数据库连接成功")
    return conn


# 查询数据库COMMENTS表的所有成员
def get_all_data():
    res = []

    conn = connect()
    c = conn.cursor()

    sql = "SELECT ID,NAME,COMMENT,TIME FROM COMMENTS ORDER BY ID DESC;"
    result = c.execute(sql).fetchall()

    for c in result:
        # print(c)
        res.append({'name':c[1],'comment':c[2], 'time':c[3]})

    return res

# 查询数据库COMMENTS表中指定name成员
def get_data_byname(name):
    res = []

    conn = connect()
    c = conn.cursor()

    print(name)
    sql = "SELECT ID,NAME,COMMENT,TIME FROM COMMENTS WHERE NAME = '%s' ORDER BY ID DESC;" % name
    # print(sql)
    result = c.execute(sql).fetchall()

    for c in result:
        print(c)
        res.append({'name':c[1],'comment':c[2], 'time':c[3]})

    if len(res) == 0:
        res.append({'name': '我尽力了，但还是没有搜索到%s相关的内容'%name, 'comment': '检查下名字重新输入吧', 'time': '祝你好运'})

    return res

# 将name,comment插入表中
def insert(name,comment,nowTime):
    conn = connect()
    c = conn.cursor()

    # 获取当前数据库个数
    sql = "SELECT COUNT(*) FROM COMMENTS;"
    result = c.execute(sql).fetchall()
    cnt = result[0][0] + 1

    # 进行插入
    print(cnt, name, comment, nowTime)
    c.execute("INSERT INTO COMMENTS (ID,NAME,COMMENT,TIME) \
          VALUES (%d, '%s', '%s', '%s')" % (cnt, name, comment, nowTime));
    conn.commit()
    print('插入数据库成功!');

    # 进行查询
    # print(get_all_data())

    conn.close()




