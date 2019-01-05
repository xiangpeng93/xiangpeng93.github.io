# -*- coding: UTF-8 -*-
import sqlite3
import json
import sys
import os

###全局变量存储，主要是方便外部调用时关闭sqlite链接
g_dict = {} 
sqlitePath = os.getcwd() #获取当前工作目录路径
if( sqlitePath.rfind('\\') != -1):
    sqlitePath = sqlitePath = sqlitePath[0:sqlitePath.rfind("\\")]
    sqlitePath = sqlitePath + "\\chwy3.db"
if( sqlitePath.rfind('/') != -1):
    sqlitePath = sqlitePath[0:sqlitePath.rfind("/")]
    sqlitePath = sqlitePath + "/chwy3.db"
print sqlitePath
#### 打开数据库链接
def ConnectSqlite():
    if g_dict.has_key("conn"):
        print "connect ready."
        return
    conn = sqlite3.connect(sqlitePath.decode("gbk").encode("utf-8"))
    cursor = conn.cursor()
    g_dict["conn"] = conn
    g_dict["cursor"] = cursor
    
#### 关闭数据库链接
def CloseSqlite():
    if g_dict.has_key("conn"):
        g_dict["conn"].close()
        g_dict.clear()

 

