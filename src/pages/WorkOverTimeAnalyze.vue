<template>
    <main-layout>
        <el-container>
            <el-aside width="200px">
                <el-upload :action="uploadUrl" multiple style="margin: 5px;" :on-success="getWorkOvertimeData">
                    <el-button style="width: 100%!important;" type="primary">上传加班信息</el-button>
                </el-upload>
            </el-aside>
            <el-container>
                <el-header>
                    <el-form :inline="true" style="margin: 5px">
                        <el-form-item label="人员姓名：">
                            <el-input v-model="searchName" placeholder="输入姓名"></el-input>
                        </el-form-item>
                        <el-form-item label="项目部门：">
                            <el-input v-model="searchDepartment" placeholder="输入项目部门">
                            </el-input>
                        </el-form-item>
                    </el-form>
                </el-header>
                <el-main style="height:85vh">
                    <el-table :data="OvertimeData.filter(data => data.name.toLowerCase().includes(searchName.toLowerCase()) &&data.proj.toLowerCase().includes(searchDepartment.toLowerCase()))" :span-method="arraySpanMethod" :row-class-name="tableRowClassName" border style="width: 100%" v-loading="loading">
                        <el-table-column prop="squene" label="流水号">
                        </el-table-column>
                        <el-table-column prop="status" label="流程状态">
                        </el-table-column>
                        <el-table-column prop="name" label="姓名">
                        </el-table-column>
                        <el-table-column prop="comp" label="公司">
                        </el-table-column>
                        <el-table-column prop="proj" label="项目">
                        </el-table-column>
                        <el-table-column prop="job" label="职务">
                        </el-table-column>
                        <el-table-column prop="startTime" label="开始时间">
                        </el-table-column>
                        <el-table-column prop="endTime" label="结束时间">
                        </el-table-column>
                        <el-table-column prop="days" label="天数">
                        </el-table-column>
                        <el-table-column prop="hours" label="小时数">
                        </el-table-column>
                        <el-table-column prop="leaves" label="是否调休">
                        </el-table-column>
                    </el-table>
                </el-main>
            </el-container>
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
    data() {
        return {
            host: linkUrl["host"],
            uploadUrl: linkUrl["host"] + "/UploadWorkOvertime",
            OvertimeData: [],
            searchName: '',
            searchDepartment: '',
            loading:false
        }
    },
    mounted: function() {
        this.userName = this.getCookie('name')
        this.userSession = this.getCookie('session')
        this.getWorkOvertimeData()
    },
    methods: {
        getWorkOvertimeData() {
        	this.loading = true
            this.$http.jsonp(this.host + "/getWorkOvertimeData", {
                params: {
                    "name": this.userName,
                    "session": this.userSession
                }
            }).then(function(res) {
            	this.loading = false
                console.log(res);
                this.OvertimeData = res.data;
            }, function(res) {
            	this.loading = false
                console.warn(res);
            })
        },
        arraySpanMethod({ row, column, rowIndex, columnIndex }) {
            if (row.name.indexOf("统计") != -1) {
                if (columnIndex === 0) {
                    return [1, 2]
                } else if (columnIndex < 2) {
                    return [0, 0]
                }
            }
        },
        tableRowClassName({ row, rowIndex }) {

            if (row.name.indexOf("统计") != -1) {
                return 'warning-row';
            } else {
                return '';
            }
            return '';
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
    }
}
</script>