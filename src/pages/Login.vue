<template>
    <div>
        <el-container style="height: 100vh">
            <el-header style="height: 30vh">
                <p style="margin-top: 100px;font-size: 30px" align="center"><i class="el-icon-document"></i> 欢迎访问彭梦瑶的人事系统</p>
            </el-header>
            <el-main>
                <el-row :gutter="0">
                    <el-col :span="8">
                        <div class="grid-content bg-purple"></div>
                    </el-col>
                    <el-col :span="8">
                        <div class="grid-content bg-purple">
                            <el-form :label-position="labelPosition" label-width="100px" :model="userInfos">
                                <el-form-item label="用户名称：">
                                    <el-input v-model="userInfos.name"></el-input>
                                </el-form-item>
                                <el-form-item label="用户密码：">
                                    <el-input type="password" v-model="userInfos.password"></el-input>
                                </el-form-item>
                                <el-form-item align="right">
                                    <el-button type="primary" align="center" style="width: 100px" @click="onSubmit"> 登陆 </el-button>
                                </el-form-item>
                            </el-form>
                        </div>
                    </el-col>
                    <el-col :span="8">
                        <div class="grid-content bg-purple"></div>
                    </el-col>
                </el-row>
            </el-main>
            <el-footer>
                <p align="center" style="font-size: 13px">©CopyRight 2018-2028 by XP Inc All Rights Reserved.</p>
            </el-footer>
        </el-container>
    </div>
</template>
<style>
.el-row {
    margin-bottom: 0px;

    &:last-child {
        margin-bottom: 0px;
    }
}

.el-col {
    border-radius: 4px;
    margin: 0px;
}

.grid-content {
    border-radius: 4px;
    min-height: 36px;
}

.row-bg {
    padding: 10px 0;
}
</style>
<script>
export default {
    data() {
        return {
            userName: "",
            labelPosition: "left",
            userInfos: {
                name: '',
                password: '',
                type: ''
            },
            host:'http://47.75.127.61:9608'
        }
    },
    methods: {
        onSubmit() {
            console.log("check user info");
            //发送get请求
            this.$http.jsonp(this.host+"/login", {
                params: {
                    "name": this.userInfos.name,
                    "passwd": this.userInfos.password
                }
            }).then(function(res) {
                //console.log(res.data);
                this.setCookie('name', this.userInfos.name, 1)
                this.setCookie('session', res.data["session"], 1)
                if (res.data["session"] != "") {
                    this.tipLoginSuccess()
                    setTimeout(this.transToDist,1000);
                } else {
                    this.tipLoginError()
                }
            }, function(res) {
                console.warn(res);
            })
        },
        setCookie(c_name, value, expiredays) {
            var exdate = new Date()
            exdate.setDate(exdate.getDate())
            document.cookie = c_name + "=" + escape(value) +
                ((expiredays == null) ? "" : ";expires=0")
        },
        tipLoginError() {
            this.$message.error('密码错误了哦！不是你吗？');
        },
        tipLoginSuccess() {
            this.$message({
                message: '都输入对了呢！即将为你跳转',
                type: 'success'
            });
        },
        transToDist() {
            window.location.href = '#/Home'
            //window.location.reload();
        }
    }
}
</script>