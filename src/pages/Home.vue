<template>
    <main-layout>
        <el-container style="height: 90vh">
            <el-aside width="150px" style="margin: 2px">
                <el-input
                        placeholder="输入关键字搜索"
                        v-model="filterText">
                </el-input>
                <el-tree
                        style="background: transparent;"
                        :data="data" :props="defaultProps" @node-click="handleNodeClick"
                        default-expand-all
                        class="filter-tree"
                        :filter-node-method="filterNode"
                        ref="treeOrg"
                ></el-tree>
            </el-aside>
            <el-container>
                <el-header style="height:auto;margin: 5px;">
                    <el-form :inline="true" :model="formInline" class="demo-form-inline">
                        <el-form-item>
                            <el-button type="primary" @click="addEmployee">添加人员</el-button>
                        </el-form-item>
                    </el-form>
                </el-header>
                <el-main>
                    <el-input
                            v-model="search"
                            size="min"
                            placeholder="输入关键字搜索"
                    />
                    <el-table
                            :data="employeeInfos.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
                            style="width: 100%"
                            :row-class-name="tableRowClassName">
                        <el-table-column
                                prop="name"
                                label="姓名"
                                width="auto">
                        </el-table-column>
                        <el-table-column
                                prop="age"
                                label="年龄"
                                width="auto">
                        </el-table-column>
                        <el-table-column
                                prop="job"
                                label="职务"
                                width="auto">
                        </el-table-column>
                        <el-table-column
                                prop="enterTime"
                                label="入职日期"
                                width="auto">
                        </el-table-column>

                        <el-table-column
                                prop="enterTime"
                                label="入职薪资"
                                width="auto">
                        </el-table-column>
                        <el-table-column
                                prop="enterTime"
                                label="当前薪资"
                                width="auto">
                        </el-table-column>
                        <el-table-column
                                prop="enterTime"
                                label="社保缴纳"
                                width="auto">
                        </el-table-column>
                        <el-table-column
                                prop="enterTime"
                                label="合同到期"
                                width="auto">
                        </el-table-column>
                        <el-table-column
                                prop="otherInfo"
                                label="其他信息"
                                width="auto">
                        </el-table-column>
                        <el-table-column
                                prop="updateTime"
                                label="更新时间">
                        </el-table-column>
                        <el-table-column
                                align="right">
                            <template slot="header" slot-scope="scope">
                            </template>
                            <template slot-scope="scope">
                                <el-button
                                        size="mini"
                                        type="success"
                                        @click="handleEdit(scope.$index, scope.row)">查看
                                </el-button>
                                <p/>
                                <el-button
                                        size="mini"
                                        @click="handleEdit(scope.$index, scope.row)">编辑
                                </el-button>
                                <p/>
                                <el-button
                                        size="mini"
                                        type="danger"
                                        @click="handleDelete(scope.$index, scope.row)">删除
                                </el-button>
                            </template>
                        </el-table-column>
                    </el-table>

                </el-main>
            </el-container>
        </el-container>

        <el-dialog title="添加雇员" :visible.sync="dialogFormVisible">
            <el-form :model="employeeForm">
                <el-form-item label="人员名称" style="text-align: left;" labelWidth="100px">
                    <el-input v-model="employeeForm.name"></el-input>
                </el-form-item>
                <el-form-item label="年龄" style="text-align: left;" labelWidth="100px">
                    <el-input v-model="employeeForm.age"></el-input>
                </el-form-item>
                <el-form-item label="职务" style="text-align: left;" labelWidth="100px">
                    <el-input v-model="employeeForm.job"></el-input>
                </el-form-item>
                <el-form-item label="入职时间" style="text-align: left;" labelWidth="100px">
                    <el-input v-model="employeeForm.enterTime"></el-input>
                </el-form-item>
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
        mounted: function () {
            //发送get请求
            this.$http.jsonp("http://127.0.0.1:8888/").then(function (res) {
                console.log(res);
                this.data = res.data;
            }, function (res) {
                console.warn(res);
            })
        },
        methods: {
            addEmployee() {
                console.log('addEmployee!');
                this.dialogFormVisible = true;

            },
            tableRowClassName({row, rowIndex}) {
                if (rowIndex % 2 === 1) {
                    return 'warning-row';
                } else if (rowIndex % 2 === 0) {
                    return 'info-row';
                }
                return '';
            },
            handleNodeClick(data) {
                console.log(data);
            },
            handleEdit(index, row) {
                console.log(index, row);
            },
            handleDelete(index, row) {
                console.log(index, row);
            },
            filterNode(value, data) {
                if (!value) return true;
                return data.label.indexOf(value) !== -1;
            }
        },
        data() {
            return {
                dialogFormVisible: false,
                search: '',
                filterText: '',
                formInline: {
                    name: '',
                    age: '',
                    job: '',
                    enterTime: '',
                    leaveTime: '',
                    address: '',
                    identityNum: '',
                    changeJob: '',
                    otherInfo: '',
                    updateTime: ''
                },
                employeeInfos: [{
                    name: '王小虎1',
                    age: '年龄',
                    job: '职务',
                    enterTime: '入职时间',
                    leaveTime: '离职时间',
                    address: '居住地址',
                    identityNum: '身份证信息',
                    changeJob: '职位变动信息',
                    otherInfo: '其他信息其他信息其他信息其他信息其他信息其他信息其他信息其他信息其他信息',
                    updateTime: '更新时间'
                }],
                employeeForm: {
                    name: '',
                    region: '',
                    date1: '',
                    date2: '',
                    delivery: false,
                    type: [],
                    resource: '',
                    desc: ''
                },
                data: [],
                defaultProps: {
                    children: 'children',
                    label:
                        'label'
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
        background: #f0f1eb;
    }
</style>