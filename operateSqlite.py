# -*- coding: UTF-8 -*-
import sqlite3
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

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
    print "通过项目组织查询雇员信息：",sqlStr
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
    print "通过部门和组织查询雇员信息：",sqlStr
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
    if len(userInfos) == 0:
        strRet = ""
    for info in userInfos:
        sqlUpdate = "update UserInfos set session = '%s'  where name = '%s' "%(strRet,name)
        sqlUpdate = sqlUpdate.encode('utf-8')
        g_dict["cursor"].execute(sqlUpdate)
        g_dict["conn"].commit()
        print "登陆用户 ：",sqlUpdate,name,passwd
    CloseSqlite()
    return strRet

def CheckUserSession(name,session):
    ConnectSqlite()
    sqlStr = "select * from UserInfos where name = '%s' and session = '%s' "%(name,session)
    sqlStr = sqlStr.encode('utf-8')
    print "校验用户 ：",sqlStr
    g_dict["cursor"].execute(sqlStr)
    userInfos = g_dict["cursor"].fetchall();
    if len(userInfos) == 0:
        strRet = "FAILED"
        print "校验失败",name,session
    CloseSqlite()
    print "校验成功",name,session
    return 'OK'

def ChangePasswd(name,passwd):
    ConnectSqlite()
    sqlUpdate = "update UserInfos set passwd = '%s' ,session = 'XXXX' where name = '%s' "%(passwd,name)
    sqlUpdate = sqlUpdate.encode('utf-8')
    print "修改密码",sqlUpdate,name,passwd
    g_dict["cursor"].execute(sqlUpdate)
    g_dict["conn"].commit()
    CloseSqlite()
    return 'OK'


from BaseHTTPServer import BaseHTTPRequestHandler
import cgi
import json
import urlparse
 
class TodoHandler(BaseHTTPRequestHandler):
    TODOS = []
    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS, POST')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
    def do_GET(self):
        try:
            print "新Get请求进入:','路径为：",self.path
            urlResult = urlparse.urlparse(self.path)
            dictParam = urlparse.parse_qs(urlResult.query)
            
            print urlResult,dictParam
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            #print data.encode('utf-8')
            if urlResult.path == "/getOrgs":
                content = "";
                if CheckUserSession(dictParam["name"][0].decode('utf-8'),dictParam["session"][0]) != "OK":
                    content = '%s(%s)'%(dictParam["callback"][0],"")
                    print "校验用户失败，检查输入信息",dictParam["name"][0].decode('utf-8'),dictParam["session"][0]
                else:
                    content = '%s(%s)'%(dictParam["callback"][0],GetOrgInfos())
                    
                self.wfile.write(content)
            elif urlResult.path == "/getEmployees":
                content = "";
                if CheckUserSession(dictParam["name"][0].decode('utf-8'),dictParam["session"][0]) != "OK":
                    content = '%s(%s)'%(dictParam["callback"][0],"")
                    print "校验用户失败，检查输入信息",dictParam["name"][0].decode('utf-8'),dictParam["session"][0]
                else:
                    departmentName = dictParam["department"][0].decode('utf-8')
                    projName = dictParam["proj"][0].decode('utf-8')
                    data = json.dumps(GetEmployeeInfos(projName,departmentName),ensure_ascii=False)
                    if data == '[]':
                        print "尝试通过项目组织获取资源"
                        data = json.dumps(GetEmployeeInfosByProj(departmentName),ensure_ascii=False)
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
                if CheckUserSession(dictParam["name"][0].decode('utf-8'),dictParam["session"][0]) != "OK":
                    content = '%s(%s)'%(dictParam["callback"][0],"")
                    print "校验用户失败，检查输入信息",dictParam["name"][0].decode('utf-8'),dictParam["session"][0]
                else:
                    userName = dictParam["name"][0].decode('utf-8')
                    userPasswd = dictParam["passwd"][0].decode('utf-8')
                    ChangePasswd(userName,userPasswd)
                    retDict = {};
                    retDict["result"] = "OK";
                    data = json.dumps(retDict,ensure_ascii=False)
                    content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
                self.wfile.write(content)
            elif urlResult.path == "/updateVersion":
                content = "";
                if CheckUserSession(dictParam["name"][0].decode('utf-8'),dictParam["session"][0]) != "OK":
                    content = '%s(%s)'%(dictParam["callback"][0],"")
                    print "校验用户失败，检查输入信息",dictParam["name"][0].decode('utf-8'),dictParam["session"][0]
                else:
                    os.system("sh updateVersion.sh")
                    retDict = {};
                    retDict["result"] = "OK";
                    data = json.dumps(retDict,ensure_ascii=False)
                    content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
                self.wfile.write(content)
        except Exception,error:
            print error
            
    def do_POST(self):
        print "新POST请求进入:','路径为：",self.path
        if self.path == "/uploadHomePic":
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD':'POST',
                         'CONTENT_TYPE':self.headers['Content-Type']
                         })
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            self.wfile.write('Client: %sn ' % str(self.client_address) )
            self.wfile.write('User-agent: %sn' % str(self.headers['user-agent']))
            self.wfile.write('Path: %sn'%self.path)
            self.wfile.write('Form data:n')
            for field in form.keys():
                field_item = form[field]
                filename = field_item.filename
                filevalue  = field_item.value
                filesize = len(filevalue)
                print u"更新新的主页图片:",(filename),len(filevalue)
                with open("logo.jpg",'wb') as f:
                    f.write(filevalue)
                    f.close()
        return 
 
if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('0.0.0.0', 9608), TodoHandler)
    print("Starting server, use <Ctrl-C> to stop")
    server.serve_forever()
