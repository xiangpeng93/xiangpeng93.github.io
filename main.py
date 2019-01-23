# -*- coding: UTF-8 -*-

from BaseHTTPServer import BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer
import cgi
import json
import urlparse
import uuid
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.dont_write_bytecode = True

from operateSqlite import *
from organizationManger import *
from employeesManger import *
from userManger import *
import operateEmployeeXls
import operateWorkOverTimeXls
import operateRewardXls
import clothingManger
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
        
        #print urlResult,dictParam
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        ## 用户登录
        if urlResult.path == "/login":
            userName = dictParam["name"][0].decode('utf-8')
            userPasswd = dictParam["passwd"][0].decode('utf-8')
            session = LoginUserInfo(userName,userPasswd)
            retDict = {};
            retDict["session"] = session;
            data = json.dumps(retDict,ensure_ascii=False)
            content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
            return
        
        try:
            if CheckUserSession(dictParam["name"][0].decode('utf-8'),dictParam["session"][0]) != "OK":
                content = '%s(%s)'%(dictParam["callback"][0],"")
                print u"校验用户失败，检查输入信息",dictParam["name"][0].decode('utf-8'),dictParam["session"][0]
                return
        except Exception,error:
            print "check user error: ",error
            return;
        ## 获取组织
        if urlResult.path == "/getOrgs":
            content = '%s(%s)'%(dictParam["callback"][0],GetOrgInfos())
            self.wfile.write(content)
        ## 获取雇员
        elif urlResult.path == "/getEmployees":
            departmentName = dictParam["department"][0].decode('utf-8')
            projName = dictParam["proj"][0].decode('utf-8')
            data = json.dumps(GetEmployeeInfos(projName,departmentName),ensure_ascii=False)
            if data == '[]':
                print u"尝试通过项目组织获取资源"
                data = json.dumps(GetEmployeeInfosByProj(departmentName),ensure_ascii=False)
            content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
        ## 通过雇员名称获取信息
        elif urlResult.path == "/getEmployeeByName":            
            employeeName = dictParam["employeeName"][0].decode('utf-8')
            data = json.dumps(GetEmployeeInfosByName(employeeName),ensure_ascii=False)
            content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
        ## 分页获取雇员信息
        elif urlResult.path == "/getEmployeeByPage":
            pageNum = dictParam["pageNum"][0].decode('utf-8')
            PageSize = dictParam["PageSize"][0].decode('utf-8')
            dataResult= {};
            dataResult["data"]=GetEmployeeByPage(pageNum,PageSize)
            dataResult["size"]=GetAllEmployeeNumber();
            data = json.dumps(dataResult,ensure_ascii=False)
            content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
        ## 获取雇员的简单信息
        elif urlResult.path == "/getSimpleEmployeeInfo":            
            data = json.dumps(GetSimpleEmployeeInfo(),ensure_ascii=False)
            content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
        ## 查询雇员信息    
        elif urlResult.path == "/queryEmployeeInfo":
            key = dictParam["key"][0].decode('utf-8')
            value = dictParam["value"][0].decode('utf-8')
            data = json.dumps(QueryEmployeeInfo(key,value),ensure_ascii=False)
            content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
        
        ## 修改密码
        elif urlResult.path == "/changePaswwd":
            userName = dictParam["name"][0].decode('utf-8')
            userPasswd = dictParam["passwd"][0].decode('utf-8')
            ChangePasswd(userName,userPasswd)
            retDict = {};
            retDict["result"] = "OK";
            data = json.dumps(retDict,ensure_ascii=False)
            content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
        ## 添加组织
        elif urlResult.path == "/addOrgInfo":
            nRet = AddOrgInfo(dictParam["orgName"][0].decode('utf-8'),dictParam["parentOrgId"][0].decode('utf-8'))
            retDict = {};
            retDict["result"] = "OK"
            retDict["id"] = nRet
            data = json.dumps(retDict,ensure_ascii=False)
            content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
        ## 删除组织
        elif urlResult.path == "/delOrgInfo":
            DelOrgInfo(dictParam["orgId"][0].decode('utf-8'))
            retDict = {};
            retDict["result"] = "OK";
            data = json.dumps(retDict,ensure_ascii=False)
            content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
        ## 获取加班信息
        elif urlResult.path == "/getWorkOvertimeData":     
            data = json.dumps(operateWorkOverTimeXls.GetWorkoverData(),ensure_ascii=False)
            content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
        ## 获取奖励信息
        elif urlResult.path == "/getRewardData":
            data = json.dumps(operateRewardXls.GetRewardData(),ensure_ascii=False)
            content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
        ## 更新版本
        elif urlResult.path == "/updateVersion":
            os.system("git pull")
            retDict = {};
            retDict["result"] = "OK";
            data = json.dumps(retDict,ensure_ascii=False)
            content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
            os._exit(1)
        ## 添加服装信息
        elif urlResult.path == "/addClothingType":
            data = json.dumps(clothingManger.AddClothingInfo(dictParam["clothingName"][0].decode('utf-8'),
                                                           dictParam["clothingType"][0].decode('utf-8'),
                                                           dictParam["fileName"][0].decode('utf-8'),
                                                           dictParam["S"][0].decode('utf-8'),
                                                           dictParam["M"][0].decode('utf-8'),
                                                           dictParam["L"][0].decode('utf-8'),
                                                           dictParam["XL"][0].decode('utf-8'),
                                                           dictParam["XXL"][0].decode('utf-8'),
                                                           dictParam["XXXL"][0].decode('utf-8'),
                                                           dictParam["XXXXL"][0].decode('utf-8'),
                                                                                                                       dictParam["rmb"][0].decode('utf-8')
                                                           ),ensure_ascii=False)
            content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
        ## 更新服装信息
        elif urlResult.path == "/updateClothing":
            data = json.dumps(clothingManger.ModClothingInfo(dictParam["clothingName"][0].decode('utf-8'),
                                                           dictParam["clothingType"][0].decode('utf-8'),
                                                           dictParam["fileName"][0].decode('utf-8'),
                                                           dictParam["S"][0].decode('utf-8'),
                                                           dictParam["M"][0].decode('utf-8'),
                                                           dictParam["L"][0].decode('utf-8'),
                                                           dictParam["XL"][0].decode('utf-8'),
                                                           dictParam["XXL"][0].decode('utf-8'),
                                                           dictParam["XXXL"][0].decode('utf-8'),
                                                           dictParam["XXXXL"][0].decode('utf-8'),
                                                                                                                       dictParam["rmb"][0].decode('utf-8')
                                                           ),ensure_ascii=False)
            content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
        ## 添加服装领用
        elif urlResult.path == "/addClothingUseInfo":
            data = json.dumps(clothingManger.AddClothingUseInfo(dictParam["clothingUserName"][0].decode('utf-8'),
                                                               dictParam["clothingUserProj"][0].decode('utf-8'),
                                                               dictParam["clothingUserDepartment"][0].decode('utf-8'),
                                                               dictParam["clothingType"][0].decode('utf-8'),
                                                               dictParam["clothingSize"][0].decode('utf-8'),
                                                               dictParam["count"][0].decode('utf-8')
                                                               ),ensure_ascii=False)
            content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
        ## 获取服装领用信息
        elif urlResult.path == "/getClothingUseInfo":
            data = json.dumps(clothingManger.GetClothingUseInfo(),ensure_ascii=False)
            content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
        ## 获取服装信息
        elif urlResult.path == "/getClothingInfo":            
            data = json.dumps(clothingManger.GetClothingInfo(),ensure_ascii=False)
            content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
        ## 删除服装
        elif urlResult.path == "/delClothingInfo":
            data = json.dumps(clothingManger.DelClothingInfo(dictParam["clothingName"][0].decode('utf-8'),
                                                           dictParam["clothingType"][0].decode('utf-8')),ensure_ascii=False)
            content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
        ## 领用服装
        elif urlResult.path == "/removeClothing":
            data = json.dumps(clothingManger.RemoveClothing(dictParam["clothingType"][0].decode('utf-8'),
                                                                dictParam["size"][0].decode('utf-8'),
                                                                dictParam["num"][0].decode('utf-8')),ensure_ascii=False)
            content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
        ## 添加服装数量
        elif urlResult.path == "/addClothingNum":
            data = json.dumps(clothingManger.AddClothingNum(dictParam["clothingType"][0].decode('utf-8'),
                                                                dictParam["size"][0].decode('utf-8'),
                                                                dictParam["num"][0].decode('utf-8')),ensure_ascii=False)
            content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
        ## 查询服装使用
        elif urlResult.path == "/queryClothingUseInfo":
            data = json.dumps(clothingManger.GetClothingUseInfoByDate(dictParam["start"][0].decode('utf-8'),
                                                                dictParam["end"][0].decode('utf-8')),ensure_ascii=False)
            content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
        ## 删除服装使用
        elif urlResult.path == "/delClothingUseInfo":
            data = json.dumps(clothingManger.DelClothingUseInfo(dictParam["clothingUseName"][0].decode('utf-8'),
                                                                    dictParam["clothingType"][0].decode('utf-8'),
                                                                    dictParam["time"][0].decode('utf-8')),ensure_ascii=False)
            content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
        ## 归还服装使用
        elif urlResult.path == "/backClothingUseInfo":
            data = json.dumps(clothingManger.BackClothingUseInfo(dictParam["clothingUseName"][0].decode('utf-8'),
                                                                    dictParam["clothingType"][0].decode('utf-8'),
                                                                    dictParam["clothingSize"][0].decode('utf-8'),
                                                                    dictParam["time"][0].decode('utf-8'),
                                                                    dictParam["count"][0].decode('utf-8')),ensure_ascii=False)
            content = '%s(%s)'%(dictParam["callback"][0],data.encode('utf-8'))
            self.wfile.write(content)
            
    def do_POST(self):
        print u"新POST请求进入','路径为：",self.path
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
        ## 上传主页图片
        if self.path == "/uploadHomePic":        
            for field in form.keys():
                field_item = form[field]
                filename = field_item.filename
                filevalue  = field_item.value
                filesize = len(filevalue)
                print u"更新新的主页图片:",(filename),len(filevalue)
                with open("logo.jpg",'wb') as f:
                    f.write(filevalue)
                    f.close()
        ## 更新雇员信息
        if self.path == "/updateEmployeesInfo":
            for field in form.keys():
                field_item = form[field]
                filename = field_item.filename
                filevalue  = field_item.value
                filesize = len(filevalue)
                print u"更新雇员信息:",(filename),len(filevalue)
                with open("employeesInfo.xlsx",'wb') as f:
                    f.write(filevalue)
                    f.close()
                    operateEmployeeXls.AddEmployeesInfoByFileName("employeesInfo.xlsx")
        ## 上传加班表格
        if self.path == "/UploadWorkOvertime":
            for field in form.keys():
                field_item = form[field]
                filename = field_item.filename
                filevalue  = field_item.value
                filesize = len(filevalue)
                print u"更新加班信息:",(filename),len(filevalue)
                with open("overtime.xlsx",'wb') as f:
                    f.write(filevalue)
                    f.close()
                    operateWorkOverTimeXls.ProcessWorkOvertimeXLS("overtime.xlsx")
        ## 上传奖励表格
        if self.path == "/UploadReward":
            for field in form.keys():
                field_item = form[field]
                filename = field_item.filename
                filevalue  = field_item.value
                filesize = len(filevalue)
                print u"更新奖励信息:",(filename),len(filevalue)
                with open("reward.xlsx",'wb') as f:
                    f.write(filevalue)
                    f.close()
                    operateRewardXls.ProcessRewardXLS("reward.xlsx")
        ## 上传服装信息
        if self.path == "/uploadClothingPicUrl":
            
            for field in form.keys():
                field_item = form[field]
                filename = field_item.filename.decode("utf-8")
                filevalue  = field_item.value
                filesize = len(filevalue)
                print u"更新服装信息:",(filename),len(filevalue)
                with open("./Img/Clothing/"+filename,'wb') as f:
                    f.write(filevalue)
                    f.close()

        return
    
if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 9608), ProcessHandler)
    print("Starting Http Server Success")
    server.serve_forever()

