<template>
    <main-layout>
        <el-container style="margin: 5px">
            <el-container >
                <el-header style="height: auto">
                    <el-form :inline="true" >
                        <el-form-item label="人员姓名：">
                            <el-input v-model="searchName" placeholder="输入姓名"></el-input>
                        </el-form-item>
                        <el-form-item label="项目部门：">
                            <el-input v-model="searchDepartment" placeholder="输入项目部门">
                            </el-input>
                        </el-form-item>
                        <el-form-item label="时间：">
                            <el-input v-model="searchMonth" placeholder="输入月份">
                            </el-input>
                        </el-form-item>
                    </el-form>
                    <el-form :inline="true" >
                        <el-form-item label="开始日期：">
                            <el-date-picker
                            v-model="taxMonthBegin"
                            type="month"
                            placeholder="选择开始月份"
                            value-format="yyyy-MM">
                        </el-date-picker>
                    </el-form-item>
                    <el-form-item label="结束日期：">
                     <el-date-picker
                     v-model="taxMonthEnd"
                     type="month"
                     placeholder="选择结束月份"
                     value-format="yyyy-MM">
                 </el-date-picker>
             </el-form-item>
             <el-form-item >
                <el-button type="primary" @click="getTaxDataByMonths">查找所得税记录</el-button>
            </el-form-item>
            <el-form-item >
                <el-button type="primary" @click="getTaxFile">导出所得税记录</el-button>
            </el-form-item>
        </el-form>
    </el-header>
    <el-main style="height: 80vh">
        <el-table :data="SalarydData.filter(data => data.name.toLowerCase().includes(searchName.toLowerCase()) &&data.comp.toLowerCase().includes(searchDepartment.toLowerCase()))"  border v-loading="loading" height="100%" >
            <el-table-column type="index" label="序号" width="60"/>
            <el-table-column prop="name" label="姓名">
            </el-table-column>
            <el-table-column prop="comp" label="项目">
            </el-table-column>
            <el-table-column prop="department" label="部门">
            </el-table-column>
            <el-table-column prop="job" label="职务">
            </el-table-column>
            <el-table-column prop="currentSalary" label="当月收入">
            </el-table-column>
            <el-table-column prop="comunicationCost" label="通信费">
            </el-table-column>
            <el-table-column prop="socialSecurity" label="社保缴纳">
            </el-table-column>
            <el-table-column prop="customCutout" label="专项扣除">
            </el-table-column>
            <el-table-column prop="currentNeedTaxNumber" label="当月应缴纳所得额" width="150">
            </el-table-column>
            <el-table-column prop="yearTaxNumber" label="累计应缴纳所得额" width="140">
            </el-table-column>
            
            <el-table-column prop="currentTax" label="当月税金">
            </el-table-column>
            <el-table-column prop="yearTax" label="累计税金">
            </el-table-column>
            <el-table-column prop="rate" label="税率">
            </el-table-column>
            <el-table-column prop="date" label="时间" >
            </el-table-column>
        </el-table>
    </el-main>
</el-container>
<el-aside width="auto" >
    <el-date-picker
    v-model="taxMonth"
    type="month"
    placeholder="选择月"
    value-format="yyyy-MM">
</el-date-picker>
<p/>
<el-upload :action="uploadUrl" multiple :before-upload="updateUrl"  :on-success="getTaxData">
    <el-button style="width: 100%!important;" type="primary">上传所得税信息信息</el-button>
</el-upload>
</el-aside>
</el-container>
</main-layout>
</template>
<style>
.el-upload {
    width: 100% !important;
}

.el-table .warning-row {
    background: oldlace;
}

.el-table .success-row {
    background: #f0f9eb;
}
</style>
<script>
    import MainLayout from '../layouts/Main.vue'
    import linkUrl from "../link.js"
    export default {
        components: {
            MainLayout
        },
        watch:{
            taxMonth(){
                this.uploadUrl = this.baseUrl + "?taxMonth=" + this.taxMonth + "&name="+this.userName
            }
        },
        data() {
            return {
                host: linkUrl["host"],
                SalarydData: [],
                searchName: '',
                searchDepartment: '',
                loading: false,
                taxMonth:"",
                baseUrl: linkUrl["host"] + "/UploadCurrentSalary",
                uploadUrl: '',
                searchMonth:"",
                taxMonthBegin:"",
                taxMonthEnd:"",

            }
        },
        mounted: function() {
            this.userName = this.getCookie('name')
            this.userSession = this.getCookie('session')
            //this.getTaxData()
        },
        methods: {
            getTaxData() {
             this.loading = true
             this.$http.jsonp(this.host + "/getTaxByMonth", {
                params: {
                    "name": this.userName,
                    "session": this.userSession,
                    "month":this.taxMonth
                }
            }).then(function(res) {
            	this.loading = false
                console.log(res);
                this.SalarydData = res.data;
            }, function(res) {
            	this.loading = false
                console.warn(res);
            })
        },
        getTaxDataByMonths() {
         this.loading = true
         this.$http.jsonp(this.host + "/getTaxByMonths", {
            params: {
                "name": this.userName,
                "session": this.userSession,
                "dateStart":this.taxMonthBegin,
                "dateEnd":this.taxMonthEnd,
            }
        }).then(function(res) {
            this.loading = false
            console.log(res);
            this.SalarydData = res.data;
        }, function(res) {
            this.loading = false
            console.warn(res);
        })
    },
    updateUrl(file){
        console.log(this.uploadUrl)
        if (this.taxMonth == "") {
            this.$message({
                message: '未选择月份，请选择月份后重新上传',
                type: 'error'
            });
            return false
        }
        return true
    }
    ,
    getTaxFile(){
        this.$http.jsonp(this.host + "/getTaxFile", {
            params: {
                "name": this.userName,
                "session": this.userSession
            }
        }).then(function(res) {
            var filePath = res.data["result"]
            console.log(filePath)
            if (filePath != "") {
               window.location= "/" + filePath
           }
       }, function(res) {
        console.warn(res);
    })
    }
    ,getCookie(c_name) {
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
    }
}
}
</script>