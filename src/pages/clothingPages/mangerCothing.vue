<template>
    <div style="height: 98%">
        <el-tabs v-model="activeName" type="border-card" style="height: 100%">
            <el-tab-pane label="服装类型添加" name="first" style="height:85%;margin: 5px;">
                <el-form :inline="true" label-width="100px">
                    <el-form-item label="服装名称">
                        <el-input v-model="clothingName" placeholder="输入服装名称"></el-input>
                    </el-form-item>
                    <el-form-item label="物料代码">
                        <el-input v-model="clothingType" placeholder="输入物料代码"></el-input>
                    </el-form-item>
                    <el-form-item label="服装图片">
                        <el-upload :action="uploadClothingPicUrl" :on-success="handleAvatarSuccess" :show-file-list="false">
                            <el-button style="width: 100%">选择服装图片</el-button>
                        </el-upload>
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
                    <el-form-item>
                        <el-button style="width: 100%" type="primary" @click='uploadClothing'>上传服装</el-button>
                    </el-form-item>
                </el-form>
                <div style="overflow-y: scroll;height: 50vh;">
                    <el-table :data="tableData" style="height: : 100%;">
                        <el-table-column prop="name" label="服装名称" width="180">
                        </el-table-column>
                        <el-table-column prop="type" label="物料代码" width="180">
                        </el-table-column>
                        <el-table-column prop="pic" label="服装图片">
                            <template slot-scope="scope">
                                <img width="100px" height="100px" :src="scope.row.pic"></img>
                            </template>
                        </el-table-column>
                        <el-table-column label="操作">
                            <template slot-scope="scope">
                                <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
                            </template>
                        </el-table-column>
                    </el-table>
                </div>
            </el-tab-pane>
        </el-tabs>
    </div>
</template>
<style type="text/css">
.el-upload {
    width: 100%;
}
</style>
<script>
import linkUrl from "../../link.js"
export default {
    data() {
        return {
            host: linkUrl["host"],
            uploadClothingPicUrl: linkUrl["host"] + '/uploadClothingPicUrl',
            activeName: "first",
            fileName: '/Img/Clothing/default.jpg',
            clothingName: '',
            clothingType: '',
            S: '0',
            M: '0',
            L: '0',
            XL: '0',
            XXL: '0',
            XXXL: '0',
            XXXXL: '0',
            tableData: [{ 'name': "test", 'type': '1212', 'pic': '/logo.jpg' }]
        }
    },
    mounted: function() {
        this.userName = this.getCookie('name')
        this.userSession = this.getCookie('session')
        this.getClothingInfo()
    },
    methods: {
        handleDelete(index, row) {
            this.$http.jsonp(this.host + "/delClothingInfo", {
                params: {
                    "name": this.userName,
                    "session": this.userSession,
                    'clothingName': row.name,
                    'clothingType': row.type,
                }
            }).then(function(res) {
            	this.$message({
                        message: '服装删除成功',
                        type: 'success'
                    });
            	this.getClothingInfo()
                console.log(res);
            }, function(res) {
                console.warn(res);
            })
        },
        handleAvatarSuccess(response, file, fileList) {
            this.$message({
                message: '上传成功',
                type: 'success'
            });
            this.fileName = '/Img/Clothing/' + file.name
            console.log(file)
        },
        uploadClothing() {
            this.$http.jsonp(this.host + "/addClothingType", {
                params: {
                    "name": this.userName,
                    "session": this.userSession,
                    'clothingName': this.clothingName,
                    'clothingType': this.clothingType,
                    'fileName': this.fileName,
                    'S': this.S,
                    'M': this.M,
                    'L': this.L,
                    'XL': this.XL,
                    'XXL': this.XXL,
                    'XXXL': this.XXXL,
                    'XXXXL': this.XXXXL,
                }
            }).then(function(res) {
                if (res.data == "\"OK\"") {
                    this.$message({
                        message: '服装添加成功',
                        type: 'success'
                    });
                } else {
                    this.$message({
                        message: '该服装已经存在',
                        type: 'warning'
                    });
                }
                console.log(res);
                this.getClothingInfo()
            }, function(res) {
                this.$message({
                    message: '服装添加失败',
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