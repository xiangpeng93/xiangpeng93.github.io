# -*- coding: UTF-8 -*-
import sqlite3
import json
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

###全局变量存储，主要是方便外部调用时关闭sqlite链接
g_dict = {} 

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
        
#### 获取组织中的人数
def GetEmployeeNumber(projName,departmentName):
    args = (departmentName,projName)
    g_dict["cursor"].execute("select * from Employees where department = ? and projName = ?",args)
    employeeInfos = g_dict["cursor"].fetchall();
    return len(employeeInfos)

#### 组织树解析类
class COrganization:
    Id = 0;
    Name = "";
    Description = "";
    ParentId = 0
    Num = 0
    def __init__(self,id,name):
        self.Name = name
        self.Num = 0
        self.AddSubOrg(id);
        pass
    def AddSubOrg(self,id):
        self.SubOrgs = []
        g_dict["cursor"].execute( str("select * from Organization where parentId = %s"%(id)))
        
        OrganizationInfo = g_dict["cursor"].fetchall();
        if len(OrganizationInfo) > 0:
            pass
        for info in OrganizationInfo:
            tmpOrg = COrganization(info[0],info[1])
            tmpOrg.Id = info[0]
            tmpOrg.Name = info[1]
            tmpOrg.Description = info[2]
            tmpOrg.ParentId = id
            tmpOrg.Num += GetEmployeeNumber(self.Name,tmpOrg.Name)
            self.Num += tmpOrg.Num
            self.SubOrgs.append(tmpOrg)

#### 组织结构化上传
def GetAllOrgFormOrgs(orgs,index):
    orgEles = []
    for org in orgs.SubOrgs:
        orgEle = {}
        orgEle["label"] = org.Name + " (" + str(org.Num) + ")"
        orgEle["id"] = org.Id
        orgEle["label_true"] = org.Name
        orgEles.append(orgEle)
        orgEle["children"] = GetAllOrgFormOrgs(org,index+1)

    return orgEles

#### 获取组织
def GetOrgInfos():
    print u"获取组织结构"
    ConnectSqlite()
    c = COrganization(0,'')

    data = json.dumps(GetAllOrgFormOrgs(c,0),ensure_ascii=False)

    CloseSqlite()
    
    return data.encode('utf-8')

##print GetOrgInfos()

def GetEmployeeInfosByProj(projName):
    employeeInfosArray = []
    ConnectSqlite()
    args = (projName,);
    print u"通过项目组织查询雇员信息：",args
    g_dict["cursor"].execute("select * from Employees where projName = ?",args)
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
    args = (departmentName,projName)
    print u"通过部门和组织查询雇员信息：",departmentName,projName
    g_dict["cursor"].execute("select * from Employees where department = ? and projName = ?",args)
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
    print u"用户登录",name,passwd
    ConnectSqlite()
    strRet = str(random.uniform(100000000,1000000000))
    args = (name,passwd)
    g_dict["cursor"].execute("select * from UserInfos where name = ? and passwd = ?",args)
    userInfos = g_dict["cursor"].fetchall();
    if len(userInfos) == 0:
        strRet = ""
    for info in userInfos:
        print u"更新session 编号"
        args = (strRet,name)
        g_dict["cursor"].execute("update UserInfos set session = ? where name = ? ",args)
        g_dict["conn"].commit()
        print u"登陆用户 ：",name,passwd
    CloseSqlite()
    return strRet

def CheckUserSession(name,session):
    ConnectSqlite()
    args = (name,session)
    print u"校验用户 ：",name,session
    g_dict["cursor"].execute("select * from UserInfos where name = ? and session = ? ",args)
    userInfos = g_dict["cursor"].fetchall();
    if len(userInfos) == 0:
        strRet = "FAILED"
        print u"校验失败",name,session
    CloseSqlite()
    print u"校验成功",name,session
    return 'OK'

def ChangePasswd(name,passwd):
    ConnectSqlite()
    args = (passwd,name)
    print u"修改密码：",name,passwd
    g_dict["cursor"].execute("update UserInfos set passwd = ? ,session = 'XXXX' where name = ?",args)
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
