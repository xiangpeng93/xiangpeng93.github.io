# -*- coding: UTF-8 -*-

from BaseHTTPServer import BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer
import cgi
import json
import urlparse

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.dont_write_bytecode = True

from operateSqlite import *
from organizationManger import *
from employeesManger import *
from userManger import *

class ProcessHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS, POST')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
    def do_GET(self):
##        try:
        print u"新Get请求进入:','路径为：",self.path
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
                print u"校验用户失败，检查输入信息",dictParam["name"][0].decode('utf-8'),dictParam["session"][0]
            else:
                content = '%s(%s)'%(dictParam["callback"][0],GetOrgInfos())
                
            self.wfile.write(content)
        elif urlResult.path == "/getEmployees":
            content = "";
            if CheckUserSession(dictParam["name"][0].decode('utf-8'),dictParam["session"][0]) != "OK":
                content = '%s(%s)'%(dictParam["callback"][0],"")
                print u"校验用户失败，检查输入信息",dictParam["name"][0].decode('utf-8'),dictParam["session"][0]
            else:
                departmentName = dictParam["department"][0].decode('utf-8')
                projName = dictParam["proj"][0].decode('utf-8')
                data = json.dumps(GetEmployeeInfos(projName,departmentName),ensure_ascii=False)
                if data == '[]':
                    print u"尝试通过项目组织获取资源"
                    data = json.dumps(GetEmployeeInfosByProj(departmentName),ensure_ascii=False)
                content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
        elif urlResult.path == "/queryEmployeeInfo":
            content = "";
            if CheckUserSession(dictParam["name"][0].decode('utf-8'),dictParam["session"][0]) != "OK":
                content = '%s(%s)'%(dictParam["callback"][0],"")
                print u"校验用户失败，检查输入信息",dictParam["name"][0].decode('utf-8'),dictParam["session"][0]
            else:
                key = dictParam["key"][0].decode('utf-8')
                value = dictParam["value"][0].decode('utf-8')
                data = json.dumps(QueryEmployeeInfo(key,value),ensure_ascii=False)
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
                print u"校验用户失败，检查输入信息",dictParam["name"][0].decode('utf-8'),dictParam["session"][0]
            else:
                userName = dictParam["name"][0].decode('utf-8')
                userPasswd = dictParam["passwd"][0].decode('utf-8')
                ChangePasswd(userName,userPasswd)
                retDict = {};
                retDict["result"] = "OK";
                data = json.dumps(retDict,ensure_ascii=False)
                content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
        elif urlResult.path == "/addOrgInfo":
            content = "";
            if CheckUserSession(dictParam["name"][0].decode('utf-8'),dictParam["session"][0]) != "OK":
                content = '%s(%s)'%(dictParam["callback"][0],"")
                print u"校验用户失败，检查输入信息",dictParam["name"][0].decode('utf-8'),dictParam["session"][0]
            else:
                nRet = AddOrgInfo(dictParam["orgName"][0].decode('utf-8'),dictParam["parentOrgId"][0].decode('utf-8'))
                retDict = {};
                retDict["result"] = "OK"
                retDict["id"] = nRet
                data = json.dumps(retDict,ensure_ascii=False)
                content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
        elif urlResult.path == "/delOrgInfo":
            content = "";
            if CheckUserSession(dictParam["name"][0].decode('utf-8'),dictParam["session"][0]) != "OK":
                content = '%s(%s)'%(dictParam["callback"][0],"")
                print u"校验用户失败，检查输入信息",dictParam["name"][0].decode('utf-8'),dictParam["session"][0]
            else:
                DelOrgInfo(dictParam["orgId"][0].decode('utf-8'))
                retDict = {};
                retDict["result"] = "OK";
                data = json.dumps(retDict,ensure_ascii=False)
                content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
        elif urlResult.path == "/updateVersion":
            content = "";
            if CheckUserSession(dictParam["name"][0].decode('utf-8'),dictParam["session"][0]) != "OK":
                content = '%s(%s)'%(dictParam["callback"][0],"")
                print u"校验用户失败，检查输入信息",dictParam["name"][0].decode('utf-8'),dictParam["session"][0]
            else:
                os.system("git pull")
                retDict = {};
                retDict["result"] = "OK";
                data = json.dumps(retDict,ensure_ascii=False)
                content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
            os._exit(1)
##        except Exception,error:
##            print "do get error",error
            
    def do_POST(self):
        print u"新POST请求进入:','路径为：",self.path
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
    server = HTTPServer(('0.0.0.0', 9608), ProcessHandler)
    print("Starting server Success")
    server.serve_forever()

