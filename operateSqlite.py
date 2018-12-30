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
    conn = sqlite3.connect('../chwy3.db')
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
        print org.Id, org.Name.encode("utf-8") ,index
        orgEle["children"] = GetAllOrgFormOrgs(org,index+1)
    ##if orgEles.count > 0:
      ##  print orgEles
    return orgEles
def GetOrgInfos():
    ConnectSqlite()
    c = COrganization(0)

    data = json.dumps(GetAllOrgFormOrgs(c,0),ensure_ascii=False)

    CloseSqlite()
    print data.encode("utf-8")
    return data.encode('utf-8')

from BaseHTTPServer import BaseHTTPRequestHandler
import cgi
import json
import urlparse
 
class TodoHandler(BaseHTTPRequestHandler):
    # Global instance to store todos. You should use a database in reality.
    TODOS = []
 
    def do_GET(self):
        # return all todos
        #if self.path != '/':
        #    self.send_error(404, "File not found.")
        #    return
        print self.path
        if self.path.find('?'):
            print self.path[2:]
            self.path = self.path[2:]
        dictParam = urlparse.parse_qs(self.path)
        #funcname = self.headers['callback']
        #print(funcname)
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        #print data.encode('utf-8')
        content = '%s(%s)'%(dictParam["callback"][0],GetOrgInfos())
        print content
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
