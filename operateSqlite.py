# -*- coding: UTF-8 -*-
import sqlite3
import json
g_dict = {} 

###全局变量存储，主要是方便外部调用时关闭sqlite链接

#### 打开数据库链接
def ConnectSqlite():
    if g_dict.has_key("conn"):
        print "connect ready."
        return
    conn = sqlite3.connect('chwy3.db')
    cursor = conn.cursor()
    g_dict["conn"] = conn
    g_dict["cursor"] = cursor
#### 关闭数据库链接
def CloseSqlite():
    if g_dict.has_key("conn"):
        g_dict["conn"].close()
        g_dict.clear()
#### 组织树解析类
class COrganization:
    Id = 0;
    Name = "";
    Description = "";
    ParentId = 0
    def __init__(self,id):
        self.AddSubOrg(id);
        pass
    def AddSubOrg(self,id):
        self.SubOrgs = []
        sqlStr = "select * from Organization where parentId = "+str(id)
        g_dict["cursor"].execute(sqlStr)
        OrganizationInfo = g_dict["cursor"].fetchall();
        if len(OrganizationInfo) > 0:
            pass
        for info in OrganizationInfo:
            tmpOrg = COrganization(info[0])
            tmpOrg.Id = info[0]
            tmpOrg.Name = info[1]
            tmpOrg.Description = info[2]
            tmpOrg.ParentId = id
            self.SubOrgs.append(tmpOrg)

def GetAllOrgFormOrgs(orgs,index):
    orgEles = []
    for org in orgs.SubOrgs:
        orgEle = {}
        orgEle["label"] = org.Name
        orgEle["id"] = org.Id
        orgEles.append(orgEle)
##        print org.Id, org.Name.encode("utf-8") ,index
        orgEle["children"] = GetAllOrgFormOrgs(org,index+1)
    ##if orgEles.count > 0:
      ##  print orgEles
    return orgEles

def GetOrgInfos():
    ConnectSqlite()
    c = COrganization(0)

    data = json.dumps(GetAllOrgFormOrgs(c,0),ensure_ascii=False)

    CloseSqlite()
    
    return data.encode('utf-8')
def GetEmployeeInfosByProj(projName):
    employeeInfosArray = []
    ConnectSqlite()
    sqlStr = "select * from Employees where projName = '"+ (projName)+"'"
    sqlStr = sqlStr.encode('utf-8')
##    print sqlStr
    g_dict["cursor"].execute(sqlStr)
    employeeInfos = g_dict["cursor"].fetchall();
    for info in employeeInfos:
        employeeInfo = {}
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
    sqlStr = "select * from Employees where department = '"+  (departmentName)+ "' and projName = '"+ (projName)+"'"
    sqlStr = sqlStr.encode('utf-8')
##    print sqlStr
    g_dict["cursor"].execute(sqlStr)
    employeeInfos = g_dict["cursor"].fetchall();
    for info in employeeInfos:
        employeeInfo = {}
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

import random

def LoginUserInfo(name,passwd):
    ConnectSqlite()
    strRet = str(random.uniform(100000000,1000000000))
    sqlStr = "select * from UserInfos where name = '%s' and passwd = '%s' "%(name,passwd)
    sqlStr = sqlStr.encode('utf-8')
    g_dict["cursor"].execute(sqlStr)
    userInfos = g_dict["cursor"].fetchall();
    print userInfos
    if len(userInfos) == 0:
        strRet = ""
    for info in userInfos:
        sqlUpdate = "update UserInfos set session = '%s'  where name = '%s' "%(strRet,name)
        sqlUpdate = sqlUpdate.encode('utf-8')
        g_dict["cursor"].execute(sqlUpdate)
        g_dict["conn"].commit()
        print sqlUpdate
    CloseSqlite()
    return strRet

def CheckUserSession(name,session):
    ConnectSqlite()
    sqlStr = "select * from UserInfos where name = '%s' and session = '%s' "%(name,session)
    sqlStr = sqlStr.encode('utf-8')
    g_dict["cursor"].execute(sqlStr)
    userInfos = g_dict["cursor"].fetchall();
    if len(userInfos) == 0:
        strRet = "FAILED"
    CloseSqlite()
    return 'OK'

def ChangePasswd(name,passwd):
    ConnectSqlite()
    sqlUpdate = "update UserInfos set passwd = '%s'  where name = '%s' "%(passwd,name)
    sqlUpdate = sqlUpdate.encode('utf-8')
    g_dict["cursor"].execute(sqlUpdate)
    g_dict["conn"].commit()
    CloseSqlite()
    return 'OK'

ChangePasswd('pmy','1234')

from BaseHTTPServer import BaseHTTPRequestHandler
import cgi
import json
import urlparse
 
class TodoHandler(BaseHTTPRequestHandler):
    # Global instance to store todos. You should use a database in reality.
    TODOS = []
    def do_GET(self):
        urlResult = urlparse.urlparse(self.path)
        dictParam = urlparse.parse_qs(urlResult.query)
        print urlResult,dictParam
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        #print data.encode('utf-8')
        if urlResult.path == "/getOrgs":
            content = "";
            if CheckUserSession(dictParam["name"][0],dictParam["session"][0]) != "OK":
                content = '%s(%s)'%(dictParam["callback"][0],"")
                print 'check username and sersseion',dictParam["name"][0],dictParam["session"][0]
            else:
                content = '%s(%s)'%(dictParam["callback"][0],GetOrgInfos())
            self.wfile.write(content)
        elif urlResult.path == "/getEmployees":
            content = "";
            if CheckUserSession(dictParam["name"][0],dictParam["session"][0]) != "OK":
                content = '%s(%s)'%(dictParam["callback"][0],"")
                print 'check username and sersseion',dictParam["name"][0],dictParam["session"][0]
            else:
                departmentName = dictParam["department"][0].decode('utf-8')
                projName = dictParam["proj"][0].decode('utf-8')
                data = json.dumps(GetEmployeeInfos(projName,departmentName),ensure_ascii=False)
                if data == '[]':
                    print "try to get proj employees"
                    data = json.dumps(GetEmployeeInfosByProj(departmentName),ensure_ascii=False)
    ##            print data
                content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
        elif urlResult.path == "/login":
            userName = dictParam["name"][0].decode('utf-8')
            userPasswd = dictParam["passwd"][0].decode('utf-8')
            session = LoginUserInfo(userName,userPasswd)
            retDict = {};
            retDict["session"] = session;
            data = json.dumps(retDict,ensure_ascii=False)
            content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
        elif urlResult.path == "/changePaswwd":
            content = "";
            if CheckUserSession(dictParam["name"][0],dictParam["session"][0]) != "OK":
                content = '%s(%s)'%(dictParam["callback"][0],"")
                print 'check username and sersseion',dictParam["name"][0],dictParam["session"][0]
            else:
                userName = dictParam["name"][0].decode('utf-8')
                userPasswd = dictParam["passwd"][0].decode('utf-8')
                ChangePasswd(userPasswd,userName)
                content = '%s(%s)'%(dictParam["callback"][0],"OK")
            self.wfile.write(content)
            
    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers['content-type'])
        if ctype == 'application/json':
            length = int(self.headers['content-length'])
            post_values = json.loads(self.rfile.read(length))
            self.TODOS.append(post_values)
        else:
            self.send_error(415, "Only json data is supported.")
            return
 
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
 
        self.wfile.write(post_values)
 
if __name__ == '__main__':
    # Start a simple server, and loop forever
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8888), TodoHandler)
    print("Starting server, use <Ctrl-C> to stop")
    server.serve_forever()
