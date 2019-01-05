# -*- coding: cp936 -*-
import random
from operateSqlite import *

def LoginUserInfo(name,passwd):
    print u"�û���¼",name,passwd
    ConnectSqlite()
    strRet = str(random.uniform(100000000,1000000000))
    args = (name,passwd)
    g_dict["cursor"].execute("select * from UserInfos where name = ? and passwd = ?",args)
    userInfos = g_dict["cursor"].fetchall();
    if len(userInfos) == 0:
        strRet = ""
    for info in userInfos:
        print u"����session ���"
        args = (strRet,name)
        g_dict["cursor"].execute("update UserInfos set session = ? where name = ? ",args)
        g_dict["conn"].commit()
        print u"��½�û� ��",name,passwd
    CloseSqlite()
    return strRet

def CheckUserSession(name,session):
    ConnectSqlite()
    args = (name,session)
    print u"У���û� ��",name,session
    g_dict["cursor"].execute("select * from UserInfos where name = ? and session = ? ",args)
    userInfos = g_dict["cursor"].fetchall();
    if len(userInfos) == 0:
        strRet = "FAILED"
        print u"У��ʧ��",name,session
    CloseSqlite()
    print u"У��ɹ�",name,session
    return 'OK'

def ChangePasswd(name,passwd):
    ConnectSqlite()
    args = (passwd,name)
    print u"�޸����룺",name,passwd
    g_dict["cursor"].execute("update UserInfos set passwd = ? ,session = 'XXXX' where name = ?",args)
    g_dict["conn"].commit()
    CloseSqlite()
    return 'OK'
