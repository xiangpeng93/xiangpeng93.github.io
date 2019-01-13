# -*- coding: cp936 -*-
from operateSqlite import *
import time
def AddClothingNum(clothingType,size,num):
    ConnectSqlite()
    num = int(num)
    strRet = "OK"
    args = (size,clothingType)
    print u"服装采购 ：",args
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
    print u"服装领用 ：",args
    clothingSizes = g_dict["cursor"].execute("select %s from ClothingTypes where  clothingType = '%s' "%args).fetchall()
    print clothingSizes
    for info in clothingSizes:
        currentNum = int(info[0])
        if (currentNum <= 0) or ((currentNum - num) < 0):
            print u"库存不足"
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
    print u"服装归还 ：",args
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
    print u"获取服装信息"
    resArray = []
    ConnectSqlite()
    g_dict["cursor"].execute("select * from ClothingTypes order by id desc")
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
    print u"删除服装 ：",args
    g_dict["cursor"].execute("delete from ClothingTypes where clothingName = ?\
and clothingType = ? ",args)
    g_dict["conn"].commit()
    CloseSqlite()
    return strRet

def CheckClothingInfo(name,clothingType):
    ConnectSqlite()
    strRet = "OK"
    args = (clothingType,)
    print u"检查服装名称 ：",args
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
    print u"更新服装信息：",args
    g_dict["cursor"].execute("delete from ClothingTypes where clothingName = ? and clothingType = ? ",(name,type))
    g_dict["cursor"].execute("insert into ClothingTypes(clothingName, clothingType, picPath,S,\
                             M, L, XL, XXL, XXXL, XXXXL,rmb) VALUES (?, ?, ?, ?, ?,\
                             ?, ?, ?, ?, ?,?)",args)
    g_dict["conn"].commit()
    CloseSqlite()
    return 'OK'
def AddClothingUseInfo(name,proj,department,clothingType,sizeType,count):
    if RemoveClothing(clothingType,sizeType,count) != "OK":
        return "LESS"
    ConnectSqlite()
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
    args = (name,proj,department,clothingType,sizeType,count,date)
    print u"添加服装使用信息：",args
    g_dict["cursor"].execute("insert into ClothingUsed(name, userProj, userDepartment,clothingType,\
                             sizeType,clothingCount,date ) VALUES (?, ?, ?, ?, ?,\
                             ?,?)",args)
    g_dict["conn"].commit()
    CloseSqlite()
    return 'OK'
def GetClothingUseInfo():
    resArray = []
    ConnectSqlite()
    print u"获取服装使用信息"
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
        resArray.append(tDict)
    return resArray

def GetClothingUseInfoByDate(start,end):
    resArray = []
    ConnectSqlite()
    args = (start,end)
    print u"通过时间查询服装使用信息",args
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
        resArray.append(tDict)
    return resArray

def AddClothingInfo(name,type,pic,s,m,l,xl,xxl,xxxl,xxxxl,rmb):
    if (CheckClothingInfo(name,type)):
        return 'FAILED'
    ConnectSqlite()
    args = (name,type,pic,s,m,l,xl,xxl,xxxl,xxxxl,rmb)
    print u"添加服装信息：",args
    g_dict["cursor"].execute("insert into ClothingTypes(clothingName, clothingType, picPath,S,\
                             M, L, XL, XXL, XXXL, XXXXL,rmb) VALUES (?, ?, ?, ?, ?,\
                             ?, ?, ?, ?, ?,?)",args)
    g_dict["conn"].commit()
    CloseSqlite()
    return 'OK'

def DelClothingUseInfo(name,type,time):
    ConnectSqlite()
    args = (name,type,time)
    print u"删除服装使用信息：",args
    g_dict["cursor"].execute("delete from ClothingUsed where name=? and clothingType=? and date=?",args)
    CloseSqlite()
    return 'OK'

def BackClothingUseInfo(name,type,sizeType,time,num):
    print name,type,sizeType,time,num
    DelClothingUseInfo(name,type,time)
    BackClothing(type,sizeType,num)
    
    return 'OK'
