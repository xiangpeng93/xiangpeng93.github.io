# -*- coding: cp936 -*-
from operateSqlite import *
import time
def AddClothingNum(clothingType,size,num):
    ConnectSqlite()
    num = int(num)
    strRet = "OK"
    args = (size,clothingType)
    print u"·þ×°²É¹º £º",args
    clothingSizes = g_dict["cursor"].execute("select %s from ClothingTypes where  clothingType = '%s' "%args).fetchall()
    print clothingSizes
    for info in clothingSizes:
        currentNum = int(info[0])
        sqlInfo = "update ClothingTypes set %s = '%d' where clothingType = '%s' "\
                  %(size,currentNum + num,clothingType)
        g_dict["cursor"].execute(sqlInfo)    
    CloseSqlite()
    return strRet

def RemoveClothing(clothingType,size,num):
    ConnectSqlite()
    num = int(num)
    strRet = "OK"
    args = (size,clothingType)
    print u"·þ×°ÁìÓÃ £º",args
    clothingSizes = g_dict["cursor"].execute("select %s from ClothingTypes where  clothingType = '%s' "%args).fetchall()
    print clothingSizes
    for info in clothingSizes:
        currentNum = int(info[0])
        if (currentNum <= 0) or ((currentNum - num) < 0):
            print u"¿â´æ²»×ã"
            strRet = "LESS"
        else:
            sqlInfo = "update ClothingTypes set %s = '%d' where clothingType = '%s' "\
                  %(size,currentNum - num,clothingType)
            g_dict["cursor"].execute(sqlInfo)    
    CloseSqlite()
    return strRet
def BackClothing(clothingType,sizeType,num):
    ConnectSqlite()
    num = int(num)
    strRet = "OK"
    args = (sizeType,clothingType)
    print u"·þ×°¹é»¹ £º",args
    clothingSizes = g_dict["cursor"].execute("select %s from ClothingTypes where  clothingType = '%s' "%args).fetchall()
    print clothingSizes
    for info in clothingSizes:
        currentNum = int(info[0])
        sqlInfo = "update ClothingTypes set %s = '%d' where clothingType = '%s' "\
                  %(sizeType,currentNum + num,clothingType)
        g_dict["cursor"].execute(sqlInfo)
    CloseSqlite()
    return strRet
def GetClothingInfo():
    print u"»ñÈ¡·þ×°ÐÅÏ¢"
    resArray = []
    ConnectSqlite()
    g_dict["cursor"].execute("select * from ClothingTypes order by id")
    clothingInfos = g_dict["cursor"].fetchall();
    if len(clothingInfos) == 0:
        pass
    for info in clothingInfos:
        tDict = {};
        tDict['id'] = info[0]
        tDict['name'] = info[1]
        tDict['type'] = info[2]
        tDict['pic'] = info[3]
        tDict['S'] = info[4]
        tDict['M'] = info[5]
        tDict['L'] = info[6]
        tDict['XL'] = info[7]
        tDict['XXL'] = info[8]
        tDict['XXXL'] = info[9]
        tDict['XXXXL'] = info[10]
        tDict['rmb'] = info[11]
        tDict['AllCount'] = int(info[4]) + int(info[5]) \
                            +int(info[6]) +int(info[7]) \
                            +int(info[8]) +int(info[9]) \
                            +int(info[10]) 
        resArray.append(tDict)
    CloseSqlite()
    return resArray

def DelClothingInfo(name,clothingType):
    ConnectSqlite()
    strRet ="OK"
    args = (name,clothingType)
    print u"É¾³ý·þ×° £º",args
    g_dict["cursor"].execute("delete from ClothingTypes where clothingName = ?\
and clothingType = ? ",args)
    g_dict["conn"].commit()
    CloseSqlite()
    return strRet

def CheckClothingInfo(name,clothingType):
    ConnectSqlite()
    strRet = "OK"
    args = (clothingType,)
    print u"¼ì²é·þ×°Ãû³Æ £º",args
    clothingInfos = g_dict["cursor"].execute("select * from ClothingTypes where  clothingType = ? ",args).fetchall()
    CloseSqlite()
    if len(clothingInfos) == 0:
        return False
    return True

def ModClothingInfo(name,type,pic,s,m,l,xl,xxl,xxxl,xxxxl,rmb):
    if (CheckClothingInfo(name,type)) != True:
        return 'FAILED'
    ConnectSqlite()
    args = (name,type,pic,s,m,l,xl,xxl,xxxl,xxxxl,rmb)
    print u"¸üÐÂ·þ×°ÐÅÏ¢£º",args
    g_dict["cursor"].execute("delete from ClothingTypes where clothingName = ? and clothingType = ? ",(name,type))
    g_dict["cursor"].execute("insert into ClothingTypes(clothingName, clothingType, picPath,S,\
                             M, L, XL, XXL, XXXL, XXXXL,rmb) VALUES (?, ?, ?, ?, ?,\
                             ?, ?, ?, ?, ?,?)",args)
    g_dict["conn"].commit()
    CloseSqlite()
    return 'OK'
def AddClothingUseInfo(name,proj,department,clothingType,sizeType,count,rmb,date):
    if RemoveClothing(clothingType,sizeType,count) != "OK":
        return "LESS"
    ConnectSqlite()
    if date == "None":
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
    else :
        date = date + " 00:00:00"
    args = (name,proj,department,clothingType,sizeType,count,date,rmb)
    print u"Ìí¼Ó·þ×°Ê¹ÓÃÐÅÏ¢£º",args
    g_dict["cursor"].execute("insert into ClothingUsed(name, userProj, userDepartment,clothingType,\
                             sizeType,clothingCount,date,rmb) VALUES (?, ?, ?, ?, ?,\
                             ?,?,?)",args)
    g_dict["conn"].commit()
    CloseSqlite()
    return 'OK'
def GetClothingUseInfo():
    resArray = []
    ConnectSqlite()
    print u"»ñÈ¡·þ×°Ê¹ÓÃÐÅÏ¢"
    clothingUseInfos = g_dict["cursor"].execute("select * from ClothingUsed  order by id desc limit 50").fetchall()
    CloseSqlite()
    for info in clothingUseInfos:
        tDict = {}
        tDict["id"] = info[0]
        tDict["name"] = info[1]
        tDict["sizeType"] = info[2]
        tDict["clothingType"] = info[3]
        tDict["userProj"] = info[4]
        tDict["userDepartment"] = info[5]
        tDict["clothingCount"] = info[6]
        tDict["date"] = info[7]
        tDict["rmb"] = info[8]
        resArray.append(tDict)
    return resArray

def GetClothingUseInfoByDate(start,end):
    resArray = []
    ConnectSqlite()
    args = (start,end)
    print u"Í¨¹ýÊ±¼ä²éÑ¯·þ×°Ê¹ÓÃÐÅÏ¢",args
    if(start == "None" or end == "None"):
        clothingUseInfos = g_dict["cursor"].execute("select * from ClothingUsed order by id desc").fetchall()
    else:
        clothingUseInfos = g_dict["cursor"].execute("select * from ClothingUsed where date BETWEEN ? AND ? order by id desc",args).fetchall()
    CloseSqlite()
    for info in clothingUseInfos:
        tDict = {}
        tDict["id"] = info[0]
        tDict["name"] = info[1]
        tDict["sizeType"] = info[2]
        tDict["clothingType"] = info[3]
        tDict["userProj"] = info[4]
        tDict["userDepartment"] = info[5]
        tDict["clothingCount"] = info[6]
        tDict["date"] = info[7]
        tDict["rmb"] = info[8]
        resArray.append(tDict)
    return resArray

def AddClothingInfo(name,type,pic,s,m,l,xl,xxl,xxxl,xxxxl,rmb):
    if (CheckClothingInfo(name,type)):
        return 'FAILED'
    ConnectSqlite()
    args = (name,type,pic,s,m,l,xl,xxl,xxxl,xxxxl,rmb)
    print u"Ìí¼Ó·þ×°ÐÅÏ¢£º",args
    g_dict["cursor"].execute("insert into ClothingTypes(clothingName, clothingType, picPath,S,\
                             M, L, XL, XXL, XXXL, XXXXL,rmb) VALUES (?, ?, ?, ?, ?,\
                             ?, ?, ?, ?, ?,?)",args)
    g_dict["conn"].commit()
    CloseSqlite()
    return 'OK'

def DelClothingUseInfo(index,name,type,time):
    ConnectSqlite()
    args = (index,name,type,time)
    print u"É¾³ý·þ×°Ê¹ÓÃÐÅÏ¢£º",args
    g_dict["cursor"].execute("delete from ClothingUsed where id=? and name=? and clothingType=? and date=?",args)
    CloseSqlite()
    return 'OK'

def BackClothingUseInfo(index,name,type,sizeType,time,num):
    print index,name,type,sizeType,time,num
    DelClothingUseInfo(index,name,type,time)
    BackClothing(type,sizeType,num)
    
    return 'OK'
