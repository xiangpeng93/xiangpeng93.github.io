<template>
	<div>
		<div>
			<el-menu :default-active="$route.path" class="el-menu-demo" mode="horizontal" @select="handleSelect" router
            background-color="#545c64"
            text-color="#fff"
            active-text-color="#ffd04b">
            <el-menu-item index="/Home" align="center" style="width: 200px"><i class="el-icon-document" ></i><b>彭梦瑶的人事系统
            </b></el-menu-item>
            <el-menu-item index="/EmployeeInfos" :class="displayOrganization">组织人员信息</el-menu-item>
            <el-menu-item index="/QueryEmployeeInfo" :class="displayEmployee">雇员信息查询</el-menu-item>
            <el-menu-item index="/WorkOverTimeAnalyze" :class="displayWorkOver">加班统计</el-menu-item>
            <el-menu-item index="/RewardAnalyze" :class="displayReward">奖励统计</el-menu-item>
            <el-menu-item index="/ClothingManger" :class="displayClothing">服装管理</el-menu-item>
            <el-menu-item index="/TaxManger" :class="displayTax">个人所得税</el-menu-item>
            <!--  <el-menu-item index="/About">其他信息</el-menu-item> -->
            <el-submenu index="#" style="float:right;">
               <template slot="title"><i class="el-icon-service"></i>{{userName}}</template>
               <div :class="displayConfig">
                <el-menu-item index="/ConfigInfo">配置信息</el-menu-item>
                <el-menu-item index="#updateVersion">更新版本</el-menu-item>
               </div>
               <el-menu-item index="#changePasswd">修改密码</el-menu-item>               
               <el-menu-item index='/'>退出登录</el-menu-item>
           </el-submenu>
       </el-menu>

       <el-dialog title="修改密码" :visible.sync="dialogFormVisible" width="30%">
        <el-form>
           <el-form-item label="用户名称：" :label-width="formLabelWidth">
              <el-input v-model="userName" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="新密码：" :label-width="formLabelWidth">
              <el-input v-model="userPasswd" autocomplete="off"></el-input>
          </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
       <el-button @click="dialogFormVisible = false">取 消</el-button>
       <el-button type="primary" @click="changePasswd">确 定</el-button>
   </div>
</el-dialog>
</div>
<slot></slot>
</div>
</template>
<style type="text/css">
    .displayHidden{
        display: none;
    }
    .displayView{
        display: none;
    }
</style>
<script>
	import linkUrl from "../link.js"
	export default {
		data() {
			return {
				userName: "",
				userPasswd: '',
				userSession: '',
				dialogFormVisible: false,
				formLabelWidth: '100px',
				host:linkUrl["host"] ,
                displayOrganization:'displayHidden',
                displayConfig:'displayHidden',
                displayTax:'displayHidden',
                displayEmployee:'displayHidden',
                displayReward:'displayHidden',
                displayClothing:'displayHidden',
                displayWorkOver:'displayHidden'
			};
		},
		beforeMount: function() {
			this.userName = this.getCookie('name')
			this.userSession = this.getCookie('session')
			this.getUserControl() 
		},
		methods: {
			handleSelect(key, keyPath) {
				console.log(key, keyPath);
				if (key === '/') {
					this.logout()
				}
				if (key == '#changePasswd') {
					this.dialogFormVisible = true
				}
				if (key == '#updateVersion')
				{
					this.updateVersion()
				}
                //this.getUserControl() 
            },
            updateVersion(){
            //发送get请求
            this.$http.jsonp(this.host+"/updateVersion", {
            	params: {
            		"name": this.userName,
            		'session': this.userSession
            	}
            }).then(function(res) {
            	console.log(res.data);
            	if (res.data["result"] === "OK") {
            		this.$message({
            			message: '版本正在更新，请稍后刷新查看',
            			type: 'success'
            		});
            		this.logout();
            	}
            	else
            	{
            		this.$message.error('版本更新失败');
            	}
            }, function(res) {
            	console.warn(res);
            })
        },
        getUserControl() {
            this.$http.jsonp(this.host + "/getUserControl", {
                params: {
                    "name": this.userName,
                    "session": this.userSession
                }
            }).then(function(res) {
                console.log(res.data);
                if (res.data["userControl"] == "all") {
                    this.displayOrganization=''
                    this.displayConfig=''
                    this.displayTax=''
                    this.displayEmployee=''
                    this.displayReward=''
                    this.displayClothing=''
                    this.displayWorkOver=''
                };
                if (res.data["userControl"].indexOf("tax") >=0 ) {
                    this.displayTax = ''
                };
                
            }, function(res) {
            	this.logout()
                console.warn(res);
            })
        },
        changePasswd() {
            //发送get请求
            this.$http.jsonp(this.host+"/changePaswwd", {
            	params: {
            		"name": this.userName,
            		"passwd": this.userPasswd,
            		'session': this.userSession
            	}
            }).then(function(res) {
            	console.log(res.data);
            	if (res.data["result"] === "OK") {
            		this.$message({
            			message: '密码修改成功，请重新登陆。',
            			type: 'success'
            		});
            		this.logout();
            	}
            	else
            	{
            		this.$message.error('密码修改失败！');
            	}
            }, function(res) {
            	console.warn(res);
            })
        },
        logout() {
        	this.setCookie('name', '');
        	this.setCookie('session', '');
        	window.location.href = '#/'
            //window.location.reload();
        },
        setCookie(c_name, value, expiredays) {
        	var exdate = new Date()
        	exdate.setDate(exdate.getDate())
        	document.cookie = c_name + "=" + escape(value) +
        	((expiredays == null) ? "" : ";expires=0")
        },
        getCookie(c_name) {
        	if (document.cookie.length > 0) {
        		var c_start = document.cookie.indexOf(c_name + "=")
        		if (c_start != -1) {
        			c_start = c_start + c_name.length + 1
        			var c_end = document.cookie.indexOf(";", c_start)
        			if (c_end == -1) c_end = document.cookie.length
        				return unescape(document.cookie.substring(c_start, c_end))
        		}
        	}
        	return ""
        },
    }
}
</script>