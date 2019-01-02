<template>
    <div style="height: 10vh">
        <el-menu :default-active="$route.path" class="el-menu-demo" mode="horizontal" @select="handleSelect" router>
            <el-menu-item index="/Home" align="center" style="width: 200px"><i class="el-icon-document"></i><b>彭梦瑶的人事系统
		</b></el-menu-item>
            <el-menu-item index="/EmployeeInfos">人员组织信息</el-menu-item>
            <!--  <el-menu-item index="/About">其他信息</el-menu-item> -->
            <el-submenu index="#" style="float:right;">
                <template slot="title"><i class="el-icon-service"></i>{{userName}}</template>
                <el-menu-item index='#' style="height: auto;margin: 0px"> 
                <el-upload
                :action="uploadLogoPicUrl"
                :show-file-list="false"
                :on-success="handleAvatarSuccess"
                >
                <el-button style="margin: 0px"  type="small">更改主页图片</el-button>
                </el-upload>
                </el-menu-item>

                <el-menu-item index="#changePasswd">修改密码</el-menu-item>
                <el-menu-item index='/'>退出登录</el-menu-item>
                <el-menu-item index="#updateVersion">更新版本</el-menu-item>
            </el-submenu>
        </el-menu>
        <slot></slot>
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
</template>
<script>
export default {
    data() {
        return {
            userName: "",
            userPasswd: '',
            userSession: '',
            dialogFormVisible: false,
            formLabelWidth: '100px',
            host:'http://58.101.21.189:9608',
            uploadLogoPicUrl:'http://127.0.0.1:9608/uploadHomePic'
        };
    },
    mounted: function() {
        this.userName = this.getCookie('name')
        this.userSession = this.getCookie('session')
    },
    methods: {
        handleAvatarSuccess()
        {
            this.$message({
                message: '更新图片成功，请刷新页面查看',
                type: 'success'
            });
        },
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