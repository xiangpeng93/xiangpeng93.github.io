# -*- coding: cp936 -*-
from operateSqlite import *
from employeesManger import *
import json

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
