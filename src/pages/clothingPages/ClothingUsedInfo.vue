<template>
    <div style="height:99%;">
        <el-tabs v-model="activeName" type="border-card" style="height:100%;">
            <el-tab-pane label="服装领用" name="first">
                <el-form :inline="true" label-width="100px">
                    <el-form-item label="人员信息">
                        <el-select v-model="clothingUserName" filterable placeholder="输入人员姓名" @change="userNameChange" allow-create :remote-method="remoteMethod" :loading="loading" remote>
                            <el-option v-for="item in tUserData" :key="item.id" :label="item.name" :value="item.name">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="所属项目">
                        <el-select v-model="clothingUserProj" filterable placeholder="输入项目名称">
                            <el-option v-for="item in tProject"  :label="item " :value="item">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="所属部门">
                        <el-select v-model="clothingUserDepartment" filterable placeholder="输入部门信息">
                            <el-option v-for="item in tDepartment" :label="item " :value="item">
                            </el-option>
                        </el-select>
                    </el-form-item>
                </el-form>
                <el-form :inline="true" label-width="100px">
                    <el-form-item label="物料代码">
                        <el-select v-model="clothingType" filterable placeholder="请选择物料代码" @change="clothTypeChange">
                            <el-option v-for="item in clothingTypeData" :key="item.id" :label="item.type +' （ '+ item.name +' ）'" :value="item.type">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="尺寸类型">
                        <el-select v-model="clothingSize" filterable placeholder="请选择服装尺寸">
                            <el-option v-for="item in sizes" :key="item.id" :label="item.label " :value="item.label">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="领用件数">
                        <el-input v-model="count" placeholder="输入新增数量"></el-input>
                    </el-form-item>
                    <el-form-item label="单价">
                        <el-input v-model="rmb" :disabled="true" placeholder="服装单价"></el-input>
                    </el-form-item>
                    <div align="right">
                        <el-button type="primary" @click='addClothingUsed'>添加领用</el-button>
                    </div>
                </el-form>
                <div>
                    <el-table :data="clothingUseData" style="height: : 100%;" height="620px">
                        <el-table-column label="序号" type="index">
                        </el-table-column>
                        <el-table-column prop="name" label="人员名称">
                        </el-table-column>
                        <el-table-column prop="clothingType" label="物料代码">
                        </el-table-column>
                        <el-table-column prop="userProj" label="所属项目">
                        </el-table-column>
                        <el-table-column prop="userDepartment" label="所属部门">
                        </el-table-column>
                        <el-table-column prop="sizeType" label="领取型号">
                        </el-table-column>
                        <el-table-column prop="clothingCount" label="领取数量">
                        </el-table-column>
                        <el-table-column prop="rmb" label="单价">
                        </el-table-column>
                        <el-table-column prop="date" label="领取时间">
                        </el-table-column>
                        <el-table-column width="200">
                            <template slot-scope="scope">
                                <el-button size="mini" type="primary" @click="handleBack(scope.$index, scope.row)">归还</el-button>
                                <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">报废</el-button>
                            </template>
                        </el-table-column>
                    </el-table>
                </div>
            </el-tab-pane>
            <el-tab-pane label="领用查询" name="second">
                <div>
                    <el-form :inline="true" label-width="100px">
                        <el-form-item label="开始日期">
                            <el-date-picker value-format="yyyy-MM-dd HH:mm:ss" v-model="timeStart" type="date" placeholder="选择日期">
                            </el-date-picker>
                        </el-form-item>
                        <el-form-item label="结束日期">
                            <el-date-picker value-format="yyyy-MM-dd HH:mm:ss" v-model="timeEnd" type="date" placeholder="选择日期">
                            </el-date-picker>
                        </el-form-item>
                        <el-form-item label="">
                            <el-button type="primary" @click="queryUseInfo">开始查询</el-button>
                        </el-form-item>
                    </el-form>
                    <el-form :inline="true" label-width="100px">
                        <el-form-item label="人员名称">
                            <el-input v-model="usedName" placeholder="输入人员名称"></el-input>
                        </el-form-item>
                        <el-form-item label="项目名称">
                            <el-input v-model="projName" placeholder="输入项目名称"></el-input>
                        </el-form-item>
                        <el-form-item label="部门名称">
                            <el-input v-model="departmentName" placeholder="输入部门名称"></el-input>
                        </el-form-item>
                    </el-form>
                    <el-table :data="QueryUseInfoData.filter(data => data.userProj.toLowerCase().includes(projName.toLowerCase()) && data.userDepartment.toLowerCase().includes(departmentName.toLowerCase()) && data.name.toLowerCase().includes(usedName.toLowerCase()))" style="height: : 100%;" height="650px">
                        <el-table-column label="序号" type="index">
                        </el-table-column>
                        <el-table-column prop="name" label="人员名称">
                        </el-table-column>
                        <el-table-column prop="clothingType" label="物料代码">
                        </el-table-column>
                        <el-table-column prop="userProj" label="所属项目">
                        </el-table-column>
                        <el-table-column prop="userDepartment" label="所属部门">
                        </el-table-column>
                        <el-table-column prop="sizeType" label="领取型号">
                        </el-table-column>
                        <el-table-column prop="clothingCount" label="领取数量">
                        </el-table-column>
                        <el-table-column prop="rmb" label="单价">
                        </el-table-column>
                        <el-table-column prop="date" label="领取时间">
                        </el-table-column>
                    </el-table>
                </div>
            </el-tab-pane>
        </el-tabs>
    </div>
</template>
<style type="text/css">
.el-upload {
    width: 200px;
    text-align: left !important;
}
</style>
<script>
import linkUrl from "../../link.js"
export default {
    data() {
        return {
            usedName: '',
            departmentName: '',
            projName: '',
            timeStart: '',
            timeEnd: '',
            clothingUserName: '',
            clothingUserProj: '',
            clothingUserDepartment: '',
            clothingType: '',
            sizes: [{
                id: 1,
                value: 'S',
                label: 'S'
            }, {
                id: 2,
                value: 'M',
                label: 'M'
            }, {
                id: 3,
                value: 'L',
                label: 'L'
            }, {
                id: 4,
                value: 'XL',
                label: 'XL'
            }, {
                id: 5,
                value: 'XXL',
                label: 'XXL'
            }, {
                id: 6,
                value: 'XXXL',
                label: 'XXXL'
            }, {
                id: 7,
                value: 'XXXXL',
                label: 'XXXXL'
            }],
            activeName: 'first',
            clothingUseData: [],
            clothingTypeData: [],
            userData: [],
            QueryUseInfoData: [],
            host: linkUrl["host"],
            count: '1',
            rmb:'0',
            clothingSize: '',
            loading:true,
            tUserData:[],
            tDepartment:[],
            tProject:[]
        }
    },
    mounted: function() {
        this.userName = this.getCookie('name')
        this.userSession = this.getCookie('session')
        this.getClothingInfo()
        this.getUserInfo()
        this.getClothingUseInfo()
    },
    methods: {
        handleBack(rowIndex, row) {
            console.log(row);
            this.$http.jsonp(this.host + "/backClothingUseInfo", {
                params: {
                    "name": this.userName,
                    "session": this.userSession,
                    "index": row.id,
                    "clothingUseName": row.name,
                    "clothingType": row.clothingType,
                    "clothingSize": row.sizeType,
                    "time": row.date,
                    'count': row.clothingCount
                }
            }).then(function(res) {
                console.log(res);
                this.clothingUseData = []
                this.getClothingUseInfo()
            }, function(res) {
                console.warn(res);
            })
        },
        handleDelete(rowIndex, row) {
            console.log(row);
            this.$http.jsonp(this.host + "/delClothingUseInfo", {
                params: {
                    "name": this.userName,
                    "session": this.userSession,
                    "index": row.id,
                    "clothingUseName": row.name,
                    "clothingType": row.clothingType,
                    "time": row.date
                }
            }).then(function(res) {
                console.log(res);
                this.clothingUseData = []
                this.getClothingUseInfo()
            }, function(res) {
                console.warn(res);
            })
        },
        queryUseInfo() {
            console.log(this.timeStart, this.timeEnd)
            this.$http.jsonp(this.host + "/queryClothingUseInfo", {
                params: {
                    "name": this.userName,
                    "session": this.userSession,
                    "start": this.timeStart == ""? "None":this.timeStart ,
                    "end": this.timeEnd == ""? "None":this.timeEnd 
                }
            }).then(function(res) {
                console.log(res);
                this.QueryUseInfoData = res.data;
            }, function(res) {
                console.warn(res);
            })
        },
        clothTypeChange(type)
        {
            console.log("clothing type change" + type)
            for (var item in this.clothingTypeData) {
                console.log(this.clothingTypeData[item].type)
                if (this.clothingTypeData[item].type == type) {
                    this.rmb = this.clothingTypeData[item].rmb
                    break;
                }
            }
        },
        userNameChange(name) {
            console.log(name);
            for (var item in this.userData) {
                var itemValue = this.userData[item]
                if (itemValue.name == name) {
                    this.clothingUserProj = itemValue.projName
                    this.clothingUserDepartment = itemValue.department
                    break;
                }
            }
        },
        getUserInfo() {
            this.$http.jsonp(this.host + "/getSimpleEmployeeInfo", {
                params: {
                    "name": this.userName,
                    "session": this.userSession
                }
            }).then(function(res) {
                console.log(res);
                this.userData = res.data;
                this.GetProjectAndDepartment();
            }, function(res) {
                console.warn(res);
            })
        },
        getClothingUseInfo() {
            this.$http.jsonp(this.host + "/getClothingUseInfo", {
                params: {
                    "name": this.userName,
                    "session": this.userSession
                }
            }).then(function(res) {
                console.log(res);
                this.clothingUseData = res.data;

            }, function(res) {
                console.warn(res);
            })
        },
        addClothingUsed() {
            this.$http.jsonp(this.host + "/addClothingUseInfo", {
                params: {
                    "name": this.userName,
                    "session": this.userSession,
                    "clothingUserName": this.clothingUserName,
                    'clothingUserProj': this.clothingUserProj,
                    'clothingUserDepartment': this.clothingUserDepartment,
                    'clothingType': this.clothingType,
                    'clothingSize': this.clothingSize,
                    'count': this.count,
                    'rmb': this.rmb
                }
            }).then(function(res) {
                console.log(res);
                if (res.data == "\"OK\"") {
                    this.$message({
                        message: '领用记录添加成功',
                        type: 'success'
                    });
                    this.getClothingUseInfo()
                } else {
                    this.$message({
                        message: '库存不足，请补充库存',
                        type: 'error'
                    });
                }

            }, function(res) {
                this.$message({
                    message: '领用记录添加失败',
                    type: 'error'
                });
                console.warn(res);
            })
        },
        getClothingInfo() {
            this.$http.jsonp(this.host + "/getClothingInfo", {
                params: {
                    "name": this.userName,
                    "session": this.userSession
                }
            }).then(function(res) {
                this.clothingTypeData = res.data;
                console.log(res);
            }, function(res) {
                console.warn(res);
            })
        },
        remoteMethod(query) {
            console.log(query)
            if (query !== '') {
                this.loading = true;
                setTimeout(() => {
                    this.loading = false;
                    this.tUserData = this.userData.filter(item => {
                        return item.name.toLowerCase()
                            .indexOf(query.toLowerCase()) > -1;
                    });
                }, 200);
            } else {
                this.tUserData = [];
            }
        },
        GetProjectAndDepartment(){
            var tempDepartment = []; 
            var tempProj = []; 
            for(var item in this.userData){
                if(tempProj.indexOf(this.userData[item].projName) == -1 && this.userData[item].projName!= ""){
                    tempProj.push(this.userData[item].projName);
                }
                if(tempDepartment.indexOf(this.userData[item].department) == -1  && this.userData[item].department!= ""){
                    tempDepartment.push(this.userData[item].department);
                }
            }
            this.tDepartment = tempDepartment;
            this.tProject = tempProj;
            return;
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