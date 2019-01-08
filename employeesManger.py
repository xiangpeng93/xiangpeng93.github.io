# -*- coding: cp936 -*-
from operateSqlite import *

#### 获取组织中的人数
def GetEmployeeNumber(projName,departmentName):
    args = (departmentName,projName)
    g_dict["cursor"].execute("select * from Employees where department = ? and projName = ?",args)
    employeeInfos = g_dict["cursor"].fetchall();
    return len(employeeInfos)

def GetAllEmployeeNumber():
    ConnectSqlite()
    g_dict["cursor"].execute("select * from Employees;")
    employeeInfos = g_dict["cursor"].fetchall();
    CloseSqlite()
    return len(employeeInfos)

def GetEmployeeInfosByName(employeeName):
    employeeInfosArray = []
    ConnectSqlite()
    args = (employeeName,);
    print u"通过名字查询雇员信息：",args
    g_dict["cursor"].execute("select * from Employees where name like ?",args)
    employeeInfos = g_dict["cursor"].fetchall();
    id = 0
    for info in employeeInfos:
        id += 1;
        employeeInfo = {}
        employeeInfo["id"] = id
        employeeInfo["companyName"] = info[1]
        employeeInfo["projName"] = info[2]
        employeeInfo["department"] = info[3]
        employeeInfo["job"] = info[4]
        employeeInfo["name"] = info[5]
        employeeInfo["enterTime"] = info[6]
        employeeInfo["salaryBegin"] = info[7]
        employeeInfo["salaryStart"] = info[8]
        employeeInfo["salaryChange"] = info[9]
        employeeInfo["salaryCurrent"] = info[10]
        employeeInfo["phoneNum"] = info[11]
        employeeInfo["nation"] = info[12]
        employeeInfo["marry"] = info[13]
        employeeInfo["education"] = info[14]
        employeeInfo["demobilized"] = info[15]
        employeeInfo["bornTime"] = info[16]
        employeeInfo["sex"] = info[17]
        employeeInfo["age"] = info[18]
        employeeInfo["zodiac"] = info[19]
        employeeInfo["constellation"] = info[20]
        employeeInfo["jobYear"] = info[21]
        employeeInfo["household"] = info[22]
        employeeInfo["personCard"] = info[23]
        employeeInfo["housebase"] = info[24]

        employeeInfo["personAddr"] = info[25]
        employeeInfo["personCardUsed"] = info[26]
        employeeInfo["isHouse"] = info[27]
        employeeInfo["nowHouse"] = info[28]
        employeeInfo["urgentName"] = info[29]
        employeeInfo["urgentPhone"] = info[30]
        employeeInfo["introductName"] = info[31]
        employeeInfo["introductProj"] = info[32]
        employeeInfo["leaveTime"] = info[33]
        employeeInfo["leaveReason"] = info[34]
        employeeInfo["contractBegin"] = info[35]
        employeeInfo["contractYear"] = info[36]
        employeeInfo["contractEnd"] = info[37]
        employeeInfo["isSecurity"] = info[38]
        employeeInfo["securitySituation"] = info[39]
        employeeInfo["remarks"] = info[40]
        employeeInfosArray.append(employeeInfo)
    CloseSqlite()
    return employeeInfosArray

def GetEmployeeInfosByProj(projName):
    employeeInfosArray = []
    ConnectSqlite()
    args = (projName,);
    print u"通过项目组织查询雇员信息：",args
    g_dict["cursor"].execute("select * from Employees where projName = ?",args)
    employeeInfos = g_dict["cursor"].fetchall();
    id = 0
    for info in employeeInfos:
        id += 1;
        employeeInfo = {}
        employeeInfo["id"] = id
        employeeInfo["companyName"] = info[1]
        employeeInfo["projName"] = info[2]
        employeeInfo["department"] = info[3]
        employeeInfo["job"] = info[4]
        employeeInfo["name"] = info[5]
        employeeInfo["enterTime"] = info[6]
        employeeInfo["salaryBegin"] = info[7]
        employeeInfo["salaryStart"] = info[8]
        employeeInfo["salaryChange"] = info[9]
        employeeInfo["salaryCurrent"] = info[10]
        employeeInfo["phoneNum"] = info[11]
        employeeInfo["nation"] = info[12]
        employeeInfo["marry"] = info[13]
        employeeInfo["education"] = info[14]
        employeeInfo["demobilized"] = info[15]
        employeeInfo["bornTime"] = info[16]
        employeeInfo["sex"] = info[17]
        employeeInfo["age"] = info[18]
        employeeInfo["zodiac"] = info[19]
        employeeInfo["constellation"] = info[20]
        employeeInfo["jobYear"] = info[21]
        employeeInfo["household"] = info[22]
        employeeInfo["personCard"] = info[23]
        employeeInfo["housebase"] = info[24]

        employeeInfo["personAddr"] = info[25]
        employeeInfo["personCardUsed"] = info[26]
        employeeInfo["isHouse"] = info[27]
        employeeInfo["nowHouse"] = info[28]
        employeeInfo["urgentName"] = info[29]
        employeeInfo["urgentPhone"] = info[30]
        employeeInfo["introductName"] = info[31]
        employeeInfo["introductProj"] = info[32]
        employeeInfo["leaveTime"] = info[33]
        employeeInfo["leaveReason"] = info[34]
        employeeInfo["contractBegin"] = info[35]
        employeeInfo["contractYear"] = info[36]
        employeeInfo["contractEnd"] = info[37]
        employeeInfo["isSecurity"] = info[38]
        employeeInfo["securitySituation"] = info[39]
        employeeInfo["remarks"] = info[40]
        employeeInfosArray.append(employeeInfo)
    CloseSqlite()
    return employeeInfosArray

def GetEmployeeInfos(projName,departmentName):
    employeeInfosArray = []
    ConnectSqlite()
    args = (departmentName,projName)
    print u"通过部门和组织查询雇员信息：",departmentName,projName
    g_dict["cursor"].execute("select * from Employees where department = ? and projName = ?",args)
    employeeInfos = g_dict["cursor"].fetchall();
    id = 0;
    for info in employeeInfos:
        id += 1;
        employeeInfo = {}
        employeeInfo["id"] = id
        employeeInfo["companyName"] = info[1]
        employeeInfo["projName"] = info[2]
        employeeInfo["department"] = info[3]
        employeeInfo["job"] = info[4]
        employeeInfo["name"] = info[5]
        employeeInfo["enterTime"] = info[6]
        employeeInfo["salaryBegin"] = info[7]
        employeeInfo["salaryStart"] = info[8]
        employeeInfo["salaryChange"] = info[9]
        employeeInfo["salaryCurrent"] = info[10]
        employeeInfo["phoneNum"] = info[11]
        employeeInfo["nation"] = info[12]
        employeeInfo["marry"] = info[13]
        employeeInfo["education"] = info[14]
        employeeInfo["demobilized"] = info[15]
        employeeInfo["bornTime"] = info[16]
        employeeInfo["sex"] = info[17]
        employeeInfo["age"] = info[18]
        employeeInfo["zodiac"] = info[19]
        employeeInfo["constellation"] = info[20]
        employeeInfo["jobYear"] = info[21]
        employeeInfo["household"] = info[22]
        employeeInfo["personCard"] = info[23]
        employeeInfo["housebase"] = info[24]

        employeeInfo["personAddr"] = info[25]
        employeeInfo["personCardUsed"] = info[26]
        employeeInfo["isHouse"] = info[27]
        employeeInfo["nowHouse"] = info[28]
        employeeInfo["urgentName"] = info[29]
        employeeInfo["urgentPhone"] = info[30]
        employeeInfo["introductName"] = info[31]
        employeeInfo["introductProj"] = info[32]
        employeeInfo["leaveTime"] = info[33]
        employeeInfo["leaveReason"] = info[34]
        employeeInfo["contractBegin"] = info[35]
        employeeInfo["contractYear"] = info[36]
        employeeInfo["contractEnd"] = info[37]
        employeeInfo["isSecurity"] = info[38]
        employeeInfo["securitySituation"] = info[39]
        employeeInfo["remarks"] = info[40]
        employeeInfosArray.append(employeeInfo)
    CloseSqlite()
    return employeeInfosArray


def QueryEmployeeInfo(key,value):
    employeeInfosArray = []
    ConnectSqlite()
    value = "%" + value + "%"
    args = (key,value)
    print u"通过关键字和类型查找雇员信息：",key,value
    g_dict["cursor"].execute("select * from Employees where %s like '%s'"%(key,value))
    employeeInfos = g_dict["cursor"].fetchall();
    id = 0;
    for info in employeeInfos:
        id += 1;
        employeeInfo = {}
        employeeInfo["id"] = id
        employeeInfo["companyName"] = info[1]
        employeeInfo["projName"] = info[2]
        employeeInfo["department"] = info[3]
        employeeInfo["job"] = info[4]
        employeeInfo["name"] = info[5]
        employeeInfo["enterTime"] = info[6]
        employeeInfo["salaryBegin"] = info[7]
        employeeInfo["salaryStart"] = info[8]
        employeeInfo["salaryChange"] = info[9]
        employeeInfo["salaryCurrent"] = info[10]
        employeeInfo["phoneNum"] = info[11]
        employeeInfo["nation"] = info[12]
        employeeInfo["marry"] = info[13]
        employeeInfo["education"] = info[14]
        employeeInfo["demobilized"] = info[15]
        employeeInfo["bornTime"] = info[16]
        employeeInfo["sex"] = info[17]
        employeeInfo["age"] = info[18]
        employeeInfo["zodiac"] = info[19]
        employeeInfo["constellation"] = info[20]
        employeeInfo["jobYear"] = info[21]
        employeeInfo["household"] = info[22]
        employeeInfo["personCard"] = info[23]
        employeeInfo["housebase"] = info[24]

        employeeInfo["personAddr"] = info[25]
        employeeInfo["personCardUsed"] = info[26]
        employeeInfo["isHouse"] = info[27]
        employeeInfo["nowHouse"] = info[28]
        employeeInfo["urgentName"] = info[29]
        employeeInfo["urgentPhone"] = info[30]
        employeeInfo["introductName"] = info[31]
        employeeInfo["introductProj"] = info[32]
        employeeInfo["leaveTime"] = info[33]
        employeeInfo["leaveReason"] = info[34]
        employeeInfo["contractBegin"] = info[35]
        employeeInfo["contractYear"] = info[36]
        employeeInfo["contractEnd"] = info[37]
        employeeInfo["isSecurity"] = info[38]
        employeeInfo["securitySituation"] = info[39]
        employeeInfo["remarks"] = info[40]
        employeeInfosArray.append(employeeInfo)
    CloseSqlite()
    return employeeInfosArray

def GetEmployeeByPage(pageNum,pageSize):
    employeeInfosArray = []
    ConnectSqlite()
    args = (str((int(pageNum)-1)*int(pageSize)),pageSize)
    print u"通过分页查找雇员信息：",pageNum,pageSize
    g_dict["cursor"].execute("select * from Employees limit ?,?",args)
    employeeInfos = g_dict["cursor"].fetchall();
    id = 0;
    for info in employeeInfos:
        id += 1;
        employeeInfo = {}
        employeeInfo["id"] = id
        employeeInfo["companyName"] = info[1]
        employeeInfo["projName"] = info[2]
        employeeInfo["department"] = info[3]
        employeeInfo["job"] = info[4]
        employeeInfo["name"] = info[5]
        employeeInfo["enterTime"] = info[6]
        employeeInfo["salaryBegin"] = info[7]
        employeeInfo["salaryStart"] = info[8]
        employeeInfo["salaryChange"] = info[9]
        employeeInfo["salaryCurrent"] = info[10]
        employeeInfo["phoneNum"] = info[11]
        employeeInfo["nation"] = info[12]
        employeeInfo["marry"] = info[13]
        employeeInfo["education"] = info[14]
        employeeInfo["demobilized"] = info[15]
        employeeInfo["bornTime"] = info[16]
        employeeInfo["sex"] = info[17]
        employeeInfo["age"] = info[18]
        employeeInfo["zodiac"] = info[19]
        employeeInfo["constellation"] = info[20]
        employeeInfo["jobYear"] = info[21]
        employeeInfo["household"] = info[22]
        employeeInfo["personCard"] = info[23]
        employeeInfo["housebase"] = info[24]

        employeeInfo["personAddr"] = info[25]
        employeeInfo["personCardUsed"] = info[26]
        employeeInfo["isHouse"] = info[27]
        employeeInfo["nowHouse"] = info[28]
        employeeInfo["urgentName"] = info[29]
        employeeInfo["urgentPhone"] = info[30]
        employeeInfo["introductName"] = info[31]
        employeeInfo["introductProj"] = info[32]
        employeeInfo["leaveTime"] = info[33]
        employeeInfo["leaveReason"] = info[34]
        employeeInfo["contractBegin"] = info[35]
        employeeInfo["contractYear"] = info[36]
        employeeInfo["contractEnd"] = info[37]
        employeeInfo["isSecurity"] = info[38]
        employeeInfo["securitySituation"] = info[39]
        employeeInfo["remarks"] = info[40]
        employeeInfosArray.append(employeeInfo)
    CloseSqlite()
    return employeeInfosArray
