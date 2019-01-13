<template>
    <div style="height:99%;">
        <el-tabs v-model="activeName" type="border-card" style="height:100%;">
            <el-tab-pane label="库存查询" name="first">
                <div>
                    <el-form :inline="true" label-width="100px">
                        <el-form-item label="服装名称">
                            <el-input v-model="searchName" placeholder="输入服装名称"></el-input>
                        </el-form-item>
                        <el-form-item label="物料代码">
                            <el-input v-model="searchType" placeholder="输入物料代码"></el-input>
                        </el-form-item>
                    </el-form>
                </div>
                <div>
                    <el-table :data="tableData.filter(data => data.name.toLowerCase().includes(searchName.toLowerCase()) && data.type.toLowerCase().includes(searchType.toLowerCase()))" height="700px">
                        <el-table-column prop="name" label="服装名称">
                        </el-table-column>
                        <el-table-column prop="type" label="物料代码">
                        </el-table-column>
                        <el-table-column prop="pic" label="服装图片" width="120px">
                            <template slot-scope="scope">
                                <img width="100px" height="100px" :src="scope.row.pic"></img>
                            </template>
                        </el-table-column>
                        <el-table-column prop="S" label="S码数量">
                        </el-table-column>
                        <el-table-column prop="M" label="M码数量">
                        </el-table-column>
                        <el-table-column prop="L" label="L码数量">
                        </el-table-column>
                        <el-table-column prop="XL" label="XL码数量">
                        </el-table-column>
                        <el-table-column prop="XXL" label="XXL码数量">
                        </el-table-column>
                        <el-table-column prop="XXXL" label="3XL码数量">
                        </el-table-column>
                        <el-table-column prop="XXXXL" label="4XL码数量">
                        </el-table-column>
                        <el-table-column prop="AllCount" label="服装总数量">
                        </el-table-column>
                        <el-table-column prop="rmb" label="单价">
                        </el-table-column>
                    </el-table>
                </div>
            </el-tab-pane>
            <el-tab-pane label="库存管理" name="second">
                <el-form :inline="true" label-width="100px">
                    <el-form-item label="物料代码">
                        <el-select v-model="clothingType" filterable placeholder="请选择物料代码">
                            <el-option v-for="item in tableData" :key="item.id" :label="item.type +' （ '+ item.name +' ）'" :value="item.type">
                            </el-option>
                        </el-select>
                    </el-form-item>
                </el-form>
                <el-form :inline="true" label-width="100px">
                    <el-form-item label="尺寸类型">
                        <el-select v-model="clothingSize" filterable placeholder="请选择服装尺寸">
                            <el-option v-for="item in sizes" :key="item.id" :label="item.label " :value="item.label">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="新增件数">
                        <el-input v-model="num" placeholder="输入新增数量"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button style="width: 100%" type="primary" @click='updateClothingInfo'>更新服装信息</el-button>
                    </el-form-item>
                </el-form>
                <div>
                    <el-table :data="tableData.filter(data => data.name.toLowerCase().includes(searchName.toLowerCase()) && data.type.toLowerCase().includes(searchType.toLowerCase()))" style="height: : 100%;" height="620px">
                        <el-table-column prop="name" label="服装名称">
                        </el-table-column>
                        <el-table-column prop="type" label="物料代码">
                        </el-table-column>
                        <el-table-column prop="pic" label="服装图片" width="120px">
                            <template slot-scope="scope">
                                <img width="100px" height="100px" :src="scope.row.pic"></img>
                            </template>
                        </el-table-column>
                        <el-table-column prop="S" label="S码数量">
                        </el-table-column>
                        <el-table-column prop="M" label="M码数量">
                        </el-table-column>
                        <el-table-column prop="L" label="L码数量">
                        </el-table-column>
                        <el-table-column prop="XL" label="XL码数量">
                        </el-table-column>
                        <el-table-column prop="XXL" label="XXL码数量">
                        </el-table-column>
                        <el-table-column prop="XXXL" label="3XL码数量">
                        </el-table-column>
                        <el-table-column prop="XXXXL" label="4XL码数量">
                        </el-table-column>
                        <el-table-column prop="AllCount" label="服装总数量">
                        </el-table-column>
                         <el-table-column prop="rmb" label="单价">
                        </el-table-column>
                        <el-table-column>
                            <template slot-scope="scope">
                                <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
                            </template>
                        </el-table-column>
                    </el-table>
                </div>
            </el-tab-pane>
        </el-tabs>
        <el-dialog title="服装信息" :visible.sync="dialogFormVisible" align="left" width="90%" top="5vh">
            <el-form :inline="true" label-width="100px">
                <el-form-item label="服装名称">
                    <el-input :disabled="true" v-model="clothingModName" placeholder="输入服装名称"></el-input>
                </el-form-item>
                <el-form-item label="物料代码">
                    <el-input :disabled="true" v-model="clothingModType" placeholder="输入物料代码"></el-input>
                </el-form-item>
                <el-form-item label="服装图片">
                    <img width="300" height="300" :src="clothingPic"/>
                    </el-form-item>
            </el-form>
            <el-form :inline="true" label-width="100px">
                <el-form-item label="S码">
                    <el-input v-model="S" placeholder="输入S码数量"></el-input>
                </el-form-item>
                <el-form-item label="M码">
                    <el-input v-model="M" placeholder="输入M码数量"></el-input>
                </el-form-item>
                <el-form-item label="L码">
                    <el-input v-model="L" placeholder="输入L码数量"></el-input>
                </el-form-item>
                <el-form-item label="XL码">
                    <el-input v-model="XL" placeholder="输入XL码数量"></el-input>
                </el-form-item>
                <el-form-item label="XXL码">
                    <el-input v-model="XXL" placeholder="输入XXL码数量"></el-input>
                </el-form-item>
                <el-form-item label="XXXL码">
                    <el-input v-model="XXXL" placeholder="输入XXXL码数量"></el-input>
                </el-form-item>
                <el-form-item label="XXXXL码">
                    <el-input v-model="XXXXL" placeholder="输入XXXXL码数量"></el-input>
                </el-form-item>
                <el-form-item label="单价">
                    <el-input v-model="rmb" placeholder="输入服装单价"></el-input>
                </el-form-item>
            </el-form>
            <div align="right">
                <el-button type="primary" @click='updateClothing'>更新服装信息</el-button>
            </div>
        </el-dialog>
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
        	rmb:'',
            clothingModName: '',
            clothingModType: '',
            clothingPic: '',
            dialogFormVisible: false,
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
            tableData: [],
            searchName: '',
            searchType: '',
            host: linkUrl["host"],
            clothingName: '',
            clothingType: '',
            S: '0',
            M: '0',
            L: '0',
            XL: '0',
            XXL: '0',
            XXXL: '0',
            XXXXL: '0',
            num: '0',
            clothingSize: ''
        }
    },
    mounted: function() {
        this.userName = this.getCookie('name')
        this.userSession = this.getCookie('session')
        this.getClothingInfo()
    },
    methods: {
        updateClothing() {
            this.$http.jsonp(this.host + "/updateClothing", {
                params: {
                    "name": this.userName,
                    "session": this.userSession,
                    'clothingName': this.clothingModName,
                    'clothingType': this.clothingModType,
                    'fileName': this.clothingPic,
                    'S': this.S,
                    'M': this.M,
                    'L': this.L,
                    'XL': this.XL,
                    'XXL': this.XXL,
                    'XXXL': this.XXXL,
                    'XXXXL': this.XXXXL,
                    'rmb':this.rmb
                }
            }).then(function(res) {
                if (res.data == "\"OK\"") {
                    this.$message({
                        message: '服装更新成功',
                        type: 'success'
                    });
                } else {
                    this.$message({
                        message: '更新失败',
                        type: 'warning'
                    });
                }
                console.log(res);
                this.getClothingInfo()
            }, function(res) {
                this.$message({
                    message: '更新失败',
                    type: 'error'
                });
                console.warn(res);
            })
        },
        handleEdit(rowIndex, row) {
            console.log(row)
            this.dialogFormVisible = true
            this.S = row.S
            this.M = row.M
            this.L = row.L
            this.XL = row.XL
            this.XXL = row.XXL
            this.XXXL = row.XXXL
            this.XXXXL = row.XXXXL
            this.clothingModName = row.name
            this.clothingModType = row.type
            this.clothingPic = row.pic
            this.rmb = row.rmb
        },
        updateClothingInfo() {
            this.$http.jsonp(this.host + "/addClothingNum", {
                params: {
                    "name": this.userName,
                    "session": this.userSession,
                    'size': this.clothingSize,
                    'num': this.num,
                    'clothingType': this.clothingType
                }
            }).then(function(res) {
                console.log(res);
                this.$message({
                    message: '库存更新成功',
                    type: 'success'
                });
            }, function(res) {
                console.warn(res);
                this.$message({
                    message: '库存更新失败',
                    type: 'error'
                });
            })
            this.getClothingInfo()
        },
        getClothingInfo() {
            this.$http.jsonp(this.host + "/getClothingInfo", {
                params: {
                    "name": this.userName,
                    "session": this.userSession
                }
            }).then(function(res) {
                console.log(res);
                this.tableData = res.data;
            }, function(res) {
                console.warn(res);
            })
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