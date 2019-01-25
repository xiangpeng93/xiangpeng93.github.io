<template>
	
	<el-tabs v-model="activeName" type="border-card" style="height: 98%">
		<el-tab-pane label="雇员查询" name="first">
			<div style="height:85vh;margin: 5px;position: relative;">
				<div>
					<el-input v-model="search"
					placeholder="输入姓名搜索" style="width: 300px;"/>
					<span style="margin: 5px"></span>
					<el-button type="primary" style="width: auto" @click="queryEmployeeByName()">查询雇员信息</el-button>
				</div>
				<div style="height:75vh;overflow-y:auto; ">
					<el-table :data="tableData" style="width: 100%" >
						<el-table-column label="序号" width="auto" type="index"/>
						<el-table-column prop="projName" label="项目" width="auto">
						</el-table-column>
						<el-table-column prop="department" label="部门" width="auto">
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
				</div>
				<div  style="position: absolute;bottom:0px;right: 0px;left: 0px;" 
				align="center">
				<el-pagination
				@size-change="handleSizeChange"
				@current-change="handleCurrentChange"
				:current-page="currentPage"
				:page-sizes="[50, 100, 200, 500, 1000]"
				:page-size="currentPageSize"
				layout=" jumper, prev, pager, next, sizes,total"
				:total="totalSize">
			</el-pagination>
		</div>

	</div>
</el-tab-pane>
<el-tab-pane label="雇员导入" name="second">
	<div style="height:85vh;margin: 5px;position: relative;">
		<el-upload  
		:action="uploadXlsFileUrl"
		:on-success="handleAvatarSuccess"
		:on-error="handleUploadError"
		>
		<el-button type="primary" >选择导入</el-button>
	</el-upload>
</div>
</el-tab-pane>
</el-tabs>
</template>
<style type="text/css">
.el-upload{
	width: 200px;
	text-align: left!important;
}
</style>
<script>
	import linkUrl from "../../link.js"
	export default {
		data() {
			return {
				currentPage:1,
				currentPageSize:50,
				activeName:'first',
				tableData: [],
				search: '',
				host:linkUrl["host"],
				uploadXlsFileUrl:linkUrl["host"]+"/updateEmployeesInfo",
				totalSize:0
			}
		},
		mounted: function() {
			this.userName = this.getCookie('name')
			this.userSession = this.getCookie('session')
			this.getEmployeesInfo()
		},
		methods: {
			handleEdit(index, row) {
				console.log(index, row);
			},
			handleAvatarSuccess()
			{
				this.$message({
					message: '更新雇员成功',
					type: 'success'
				});
			},
			handleUploadError()
			{
				this.$message({
					message: '更新失败，请检查文件',
					type: 'error'
				});
			},
			handleSizeChange(val) {
				console.log(`每页 ${val} 条`);
				this.currentPageSize = val;
				this.getEmployeesInfo();
			},
			handleCurrentChange(val) {
				console.log(`当前页: ${val}`);
				this.currentPage = val;
				this.getEmployeesInfo();
			},
			getEmployeesInfo() {
				this.$http.jsonp(this.host+"/getEmployeeByPage", {
					params: {
						"name": this.userName,
						"session": this.userSession,
						"pageNum": this.currentPage,
						"PageSize": this.currentPageSize
					}
				}).then(function(res) {
					console.log(res);
					this.tableData = res.data.data;
					this.totalSize = res.data.size;
				}, function(res) {
					console.warn(res);
				})
			},
			queryEmployeeByName(){
				this.$http.jsonp(this.host+"/getEmployeeByName", {
					params: {
						"name": this.userName,
						"session": this.userSession,
						"employeeName": "%"+this.search+"%"
					}
				}).then(function(res) {
					console.log(res);
					this.tableData = res.data;
					this.totalSize = res.data.length;
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