<template>
    <main-layout>
        <el-container style="height: 90vh">
            <el-aside width="250px" style="margin: 2px">
                <el-input placeholder="输入关键字搜索" v-model="filterText">
                </el-input>
                <el-tree style="background: transparent;" :data="data" :props="defaultProps" @node-click="handleNodeClick" default-expand-all class="filter-tree" :filter-node-method="filterNode" ref="treeOrg"></el-tree>
            </el-aside>
            <el-container>
                <el-header style="height:auto;margin: 5px;">
                    <!--      <el-form :inline="true" :model="formInline" class="demo-form-inline">
                        <el-form-item>
                            <el-button type="primary" @click="addEmployee">添加人员</el-button>
                        </el-form-item>
                    </el-form> -->
                </el-header>
                <el-main>
                    <el-input v-model="search" size="min" placeholder="输入关键字搜索" />
                    <el-table :data="employeeInfos.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))" style="width: 100%" :row-class-name="tableRowClassName">
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

export default {
    components: {
        MainLayout
    },
    watch: {
        filterText(val) {
            this.$refs.treeOrg.filter(val);
        }
    },
    mounted: function() {
        this.userName = this.getCookie('name')
        this.userSession = this.getCookie('session')
        console.log(this.userName,this.userSession);
        //发送get请求
        this.$http.jsonp(this.host+"/getOrgs", {
                params: {
                    "name": this.userName,
                    "session": this.userSession
                }
            }).then(function(res) {
            console.log(res);
            this.data = res.data;
        }, function(res) {
            this.transToLogin()
            console.warn(res);
        })
    },
    methods: {
        getEmployeesInfo() {
            this.$http.jsonp(this.host+"/getEmployees", {
                params: {
                    "department": this.currentDepartment,
                    "proj": this.currentProj,
                    "name": this.userName,
                    "session": this.userSession
                }
            }).then(function(res) {
                console.log(res);
                this.employeeInfos = res.data;
            }, function(res) {
                this.transToLogin()
                console.warn(res);
            })
        },
        addEmployee() {
            console.log('addEmployee!');
            this.dialogFormVisible = true;

        },
        tableRowClassName({ row, rowIndex }) {
            if (rowIndex % 2) {
                return 'warning-row';
            }
            return 'success-row';
        },
        handleNodeClick(data) {
            console.log(data);
            console.log(this.$refs.treeOrg.getNode(this.$refs.treeOrg.currentNode.node).parent.data)
            this.currentDepartment = data.label
            this.currentProj = this.$refs.treeOrg.getNode(this.$refs.treeOrg.currentNode.node).parent.data.label
            this.getEmployeesInfo()
        },
        handleEdit(index, row) {
            console.log(index, row);
            this.dialogFormVisible = true;
            this.employeeForm = row
        },
        handleDelete(index, row) {
            console.log(index, row);
        },
        filterNode(value, data) {
            if (!value) return true;
            return data.label.indexOf(value) !== -1;
        },
        transToLogin() {
            window.location.href = '#/'
            window.location.reload();
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
            host:'http://58.101.21.189:9608',
            userName:"",
            userSession:"",
            labelWidth: "120px",
            currentDepartment: '',
            currentProj: '',
            dialogFormVisible: false,
            search: '',
            filterText: '',
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
            employeeInfos: [],
            // employeeInfos: [{
            //     companyName: '',
            //     projName: '',
            //     department: '',
            //     job: '',
            //     name: '',
            //     enterTime:'',
            //     salaryBegin: '',
            //     salaryStart: '',
            //     salaryChange: '',
            //     salaryCurrent: '',
            //     phoneNum: '',
            //     nation:'',
            //     marry:'',
            //     education:'',
            //     demobilized:'',
            //     bornTime:'',
            //     sex:'',
            //     age:'',
            //     zodiac:'',
            //     constellation:'',
            //     jobYear:'',
            //     household:'',
            //     personCard:'',
            //     housebase:'',
            //     personAddr:'',
            //     personCardUsed:'',
            //     isHouse:'',
            //     nowHouse:'',
            //     urgentName:'',
            //     urgentPhone:'',
            //     introductName:'',
            //     introductProj:'',
            //     leaveTime:'',
            //     leaveReason:'',
            //     contractBegin:'',
            //     contractYear:'',
            //     contractEnd:'',
            //     isSecurity:'',
            //     securitySituation:'',
            //     remarks:''
            // }],
            data: [],
            defaultProps: {
                children: 'children',
                label: 'label'
            }
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
    margin: 0px;
}

.row-bg {
    padding: 5px 0;
    margin: 0px;
}
</style>