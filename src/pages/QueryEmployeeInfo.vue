<template>
    <main-layout>
        <el-container style="height: 90vh">
            <el-container>
                <el-header style="height:auto;margin: 5px;">
                    <el-form :inline="true">
                        <el-form-item label="查询数据：">
                            <el-input v-model="search" size="normal" placeholder="输入关键字" />
                        </el-form-item>
                        <el-form-item label="查询类型：">
                            <el-select v-model="searchType" placeholder="查询类型">
                                <el-option label="合同到期时间" value="contractEnd"></el-option>
                                <el-option label="当前薪资" value="salaryCurrent"></el-option>
                            </el-select>
                        </el-form-item>
                        <el-form-item>
                            <el-button type="primary" @click="queryEmployeeInfo">查询</el-button>
                        </el-form-item>
                    </el-form>
                </el-header>
                <el-main>
                    <el-table :data="employeeInfos" style="width: 100%" :row-class-name="tableRowClassName">
                        <el-table-column prop="id" label="序号" width="auto">
                        </el-table-column>
                        <el-table-column prop="name" label="姓名" width="auto">
                        </el-table-column>
                        <el-table-column prop="age" label="年龄" width="auto">
                        </el-table-column>
                        <el-table-column prop="job" label="职务" width="auto">
                        </el-table-column>
                        <el-table-column prop="phoneNum" label="电话" width="auto">
                        </el-table-column>
                        <el-table-column prop="enterTime" label="入职日期" width="auto">
                        </el-table-column>
                        <el-table-column prop="salaryBegin" label="入职薪资" width="auto">
                        </el-table-column>
                        <el-table-column prop="salaryCurrent" label="当前薪资" width="auto">
                        </el-table-column>
                        <el-table-column prop="isSecurity" label="社保缴纳" width="auto">
                        </el-table-column>
                        <el-table-column prop="contractEnd" label="合同到期" width="auto">
                        </el-table-column>
                        <el-table-column align="right">
                            <template slot="header" slot-scope="scope">
                            </template>
                            <template slot-scope="scope">
                                <el-button size="mini" type="success" @click="handleEdit(scope.$index, scope.row)">查看
                                </el-button>
                            </template>
                        </el-table-column>
                    </el-table>
                </el-main>
            </el-container>
        </el-container>
        <el-dialog title="雇员信息" :visible.sync="dialogFormVisible" align="left" width="90%" top="5vh">
            <el-form :model="employeeForm">
                <el-row :gutter="10">
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="分/总公司：" :labelWidth="labelWidth" style="text-align: left;" align="left">
                                <el-input v-model="employeeForm.companyName"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="项目名称：" style="text-align: left;" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.projName"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="部门：" style="text-align: left;" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.department"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                </el-row>
                <el-row :gutter="10">
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="姓名：" :labelWidth="labelWidth" style="text-align: left;" align="left">
                                <el-input v-model="employeeForm.name"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="年龄：" style="text-align: left;" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.age"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="职务：" style="text-align: left;" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.job"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="入职时间：" style="text-align: left;" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.enterTime"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                </el-row>
                <el-row :gutter="10">
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="入职薪资：" :labelWidth="labelWidth" style="text-align: left;" align="left">
                                <el-input v-model="employeeForm.salaryBegin"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="转正薪资：" style="text-align: left;" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.salaryStart"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="薪资调整：" style="text-align: left;" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.salaryChange"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="当前薪资：" style="text-align: left;" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.salaryCurrent"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                </el-row>
                <el-row :gutter="10">
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="电话号码：" :labelWidth="labelWidth" style="text-align: left;" align="left">
                                <el-input v-model="employeeForm.phoneNum"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="民族：" style="text-align: left;" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.nation"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="是否结婚：" style="text-align: left;" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.marry"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="学历：" style="text-align: left;" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.education"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                </el-row>
                <el-row :gutter="10">
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="是否退伍：" :labelWidth="labelWidth" style="text-align: left;" align="left">
                                <el-input v-model="employeeForm.demobilized"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="出生时间：" style="text-align: left;" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.bornTime"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="性别：" style="text-align: left;" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.sex"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="生肖：" style="text-align: left;" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.zodiac"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                </el-row>
                <el-row :gutter="10">
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="星座：" :labelWidth="labelWidth" style="text-align: left;" align="left">
                                <el-input v-model="employeeForm.constellation"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="工作年限：" style="text-align: left;" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.jobYear"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="户籍：" style="text-align: left;" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.household"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="身份证号：" style="text-align: left;" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.personCard"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                </el-row>
                <el-row :gutter="10">
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="祖籍：" :labelWidth="labelWidth" style="text-align: left;" align="left">
                                <el-input v-model="employeeForm.housebase"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="证件地址：" style="text-align: left;" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.personAddr"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="证件有效：" :labelWidth="labelWidth" style="text-align: left;" align="left">
                                <el-input v-model="employeeForm.personCardUsed"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="是否住宿：" style="text-align: left;" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.isHouse"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                </el-row>
                <el-row :gutter="10">
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="居住地址：" style="text-align: left;" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.nowHouse"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="紧急联系人：" style="text-align: left;" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.urgentName"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="紧急联系号：" :labelWidth="labelWidth" style="text-align: left;" align="left">
                                <el-input v-model="employeeForm.urgentPhone"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="介绍人：" style="text-align: left;" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.introductName"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                </el-row>
                <el-row :gutter="10">
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="介绍人项目：" style="text-align: left;" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.introductProj"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="离职日期：" style="text-align: left;" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.leaveTime"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="离职原因：" :labelWidth="labelWidth" style="text-align: left;" align="left">
                                <el-input v-model="employeeForm.leaveReason"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="合同开始日：" style="text-align: left;" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.contractBegin"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                </el-row>
                <el-row :gutter="10">
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="合同年限：" style="text-align: left;" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.contractYear"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="合同结束日：" style="text-align: left;" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.contractEnd"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="是否缴纳社保：" :labelWidth="labelWidth" style="text-align: left;" align="left">
                                <el-input v-model="employeeForm.isSecurity"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="社保状态：" style="text-align: left;" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.securitySituation"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                </el-row>
                <el-row :gutter="10">
                    <el-col :span="6">
                        <div class="grid-content bg-purple">
                            <el-form-item label="备注：" :labelWidth="labelWidth">
                                <el-input v-model="employeeForm.remarks"></el-input>
                            </el-form-item>
                        </div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple"></div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple"></div>
                    </el-col>
                    <el-col :span="6">
                        <div class="grid-content bg-purple"></div>
                    </el-col>
                </el-row>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="dialogFormVisible = false">取 消</el-button>
                <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
            </div>
        </el-dialog>
    </main-layout>
</template>
<script>
import MainLayout from '../layouts/Main.vue'
import linkUrl from "../link.js"
export default {
    components: {
        MainLayout
    },
    mounted: function() {
        this.userName = this.getCookie('name')
        this.userSession = this.getCookie('session')
        this.searchType = 'contractEnd'
        var CurrentDate = new Date();
        var month = new Number(CurrentDate.getMonth())
        month = month + 2
        if (month < 10) {
            month = "0" + month
        }
        this.search = CurrentDate.getFullYear() + '-' + month;
        this.queryEmployeeInfo()
    },
    methods: {
        queryEmployeeInfo() {
            this.$http.jsonp(this.host + "/queryEmployeeInfo", {
                params: {
                    "name": this.userName,
                    "session": this.userSession,
                    "value": this.search,
                    "key": this.searchType
                }
            }).then(function(res) {
                console.log(res);
                this.employeeInfos = res.data;
                if (this.searchType == "contractEnd") {
                    this.$notify.info({
                        title: '雇员合同到期提醒',
                        message: this.search + ', 合同到期人数为：' + this.employeeInfos.length
                    });
                }
            }, function(res) {
                console.warn(res);
            })
        },
        handleEdit(index, row) {
            console.log(index, row);
            this.dialogFormVisible = true;
            this.employeeForm = row
        },
        tableRowClassName({ row, rowIndex }) {
            if (rowIndex % 2) {
                return 'warning-row';
            }
            return 'success-row';
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
        }
    },
    data() {
        return {
            host: linkUrl["host"],
            userName: "",
            userSession: "",
            search: '',
            searchType: '',
            employeeInfos: [],
            defaultProps: {
                children: 'children',
                label: 'label'
            },
            labelWidth: "120px",
            dialogFormVisible: false,
            employeeForm: {
                companyName: '',
                projName: '',
                department: '',
                job: '',
                name: '',
                enterTime: '',
                salaryBegin: '',
                salaryStart: '',
                salaryChange: '',
                salaryCurrent: '',
                phoneNum: '',
                nation: '',
                marry: '',
                education: '',
                demobilized: '',
                bornTime: '',
                sex: '',
                age: '',
                zodiac: '',
                constellation: '',
                jobYear: '',
                household: '',
                personCard: '',
                housebase: '',
                personAddr: '',
                personCardUsed: '',
                isHouse: '',
                nowHouse: '',
                urgentName: '',
                urgentPhone: '',
                introductName: '',
                introductProj: '',
                leaveTime: '',
                leaveReason: '',
                contractBegin: '',
                contractYear: '',
                contractEnd: '',
                isSecurity: '',
                securitySituation: '',
                remarks: ''
            },
        };
    }
}
</script>
<style>
.el-table .warning-row {
    background: oldlace;
}

.el-table .success-row {
    background: #f0f9eb;
}

.el-form-item__label {
    text-align: left !important;
}
</style>