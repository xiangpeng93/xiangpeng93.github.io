# -*- coding: utf-8 -*-
import random
from operateSqlite import *

def LoginUserInfo(name,passwd):
    print u"用户登录",name,passwd
    ConnectSqlite()
    strRet = str(random.uniform(100000000,1000000000))
    args = (name,passwd)
    g_dict["cursor"].execute("select * from UserInfos where name = ? and passwd = ?",args)
    userInfos = g_dict["cursor"].fetchall();
    if len(userInfos) == 0:
        print u"登录失败"
        strRet = ""
    for info in userInfos:
        args = (strRet,name)
        g_dict["cursor"].execute("update UserInfos set session = ? where name = ? ",args)
        g_dict["conn"].commit()
        print u"登录成功",name,passwd
    CloseSqlite()
    return strRet


def GetUserControl(name,session):
    print u"获取用户权限",name,session
    dResult = {}
    ConnectSqlite()
    args = (name,session)
    g_dict["cursor"].execute("select * from UserInfos where name = ? and session = ?",args)
    userInfos = g_dict["cursor"].fetchall();
    if len(userInfos) == 0:
        print u"获取失败"
    for info in userInfos:
        dResult["userControl"] = info[4]
        print u"获取成功",name,info
    CloseSqlite()
    return dResult

def CheckUserSession(name,session):
    ConnectSqlite()
    args = (name,session)
    print u"校验登录信息",name,session
    g_dict["cursor"].execute("select * from UserInfos where name = ? and session = ? ",args)
    userInfos = g_dict["cursor"].fetchall();
    CloseSqlite()
    if len(userInfos) == 0:
        strRet = "FAILED"
        print u"校验失败",name,session
        return "FAILED"
    
    print u"校验成功",name,session
    return 'OK'

def ChangePasswd(name,passwd):
    ConnectSqlite()
    args = (passwd,name)
    print u"修改用户密码",name,passwd
    g_dict["cursor"].execute("update UserInfos set passwd = ? ,session = 'XXXX' where name = ?",args)
    g_dict["conn"].commit()
    CloseSqlite()
    return 'OK'
