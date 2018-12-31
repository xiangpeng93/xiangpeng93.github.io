<template>
    <div style="height: 10vh">
        <el-menu :default-active="$route.path" class="el-menu-demo" mode="horizontal" @select="handleSelect" router>
            <el-menu-item index="#" align="center" style="width: 200px"><i class="el-icon-document"></i><b>彭梦瑶的人事系统
		</b></el-menu-item>
            <el-menu-item index="/Home">人员组织信息</el-menu-item>
            <el-menu-item index="/About">其他信息</el-menu-item>
            <el-submenu index="#" style="float:right;">
                <template slot="title"><i class="el-icon-service"></i>{{userName}}</template>
                <el-menu-item index="#changePasswd">修改密码</el-menu-item>
                <el-menu-item index='/'>退出登录</el-menu-item>
            </el-submenu>
        </el-menu>
        <slot></slot>
    </div>
</template>
<script>
export default {
    data() {
        return {
            userName: ""
        };
    },
    mounted: function() {
        this.userName = this.getCookie('name')
    },
    methods: {
        handleSelect(key, keyPath) {
            console.log(key, keyPath);
            if (key === '/')
            {
            	this.logout()
            }
            if (key === '#changePasswd')
            {

            }
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