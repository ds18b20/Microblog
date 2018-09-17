#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
import sqlite3

# 连接到db文件
conn = sqlite3.connect('app.db')
# 创建一个Cursor:
cursor = conn.cursor()

# 查询所有表名：
cursor.execute("select name from sqlite_master where type = 'table' order by name")
print("Tables name:", cursor.fetchall())

# 查询表user的结构：
cursor.execute('PRAGMA table_info(user)')
print("Table structure:", cursor.fetchall())

# 执行查询表user内的所有记录:
cursor.execute('select * from user')
print("Table record:", cursor.fetchall())

cursor.close()
conn.close()
