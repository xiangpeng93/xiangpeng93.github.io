<template>
	<main-layout >
		<el-container style="height: 90vh">
			<el-aside width="200px" style="margin: 2px">
				<el-input
				placeholder="关键字查找"
				v-model="filterText">
			</el-input>
			<el-tree  style="background: transparent;" 
			:data="data" :props="defaultProps" @node-click="handleNodeClick"
			default-expand-all
			class="filter-tree"
			:filter-node-method="filterNode"
			ref="tree2"
			></el-tree>
		</el-aside>
		<el-container>
			<el-header style="height:auto;margin: 5px;">
				<el-form :inline="true" :model="formInline" class="demo-form-inline">
					<el-form-item>
						<el-button type="primary" @click="onSubmit">添加人员</el-button>
					</el-form-item>
				</el-form>
			</el-header>
			<el-main>
				<el-table
				:data="tableData2.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
				style="width: 100%"
				:row-class-name="tableRowClassName">
				<el-table-column
				prop="date"
				label="日期"
				width="180">
			</el-table-column>
			<el-table-column
			prop="name"
			label="姓名"
			width="180">
		</el-table-column>
		<el-table-column
		prop="address"
		label="地址">
	</el-table-column>
	<el-table-column
	align="right">
	<template slot="header" slot-scope="scope">
		<el-input
		v-model="search"
		size="max"
		placeholder="输入关键字搜索"
		style="width: 200px"/>
	</template>
	<template slot-scope="scope">
		<el-button
		size="mini"
		@click="handleEdit(scope.$index, scope.row)">Edit</el-button>
		<el-button
		size="mini"
		type="danger"
		@click="handleDelete(scope.$index, scope.row)">Delete</el-button>
	</template>
</el-table-column>
</el-table>

</el-main>
</el-container>
</el-container>

<el-dialog title="收货地址" :visible.sync="dialogFormVisible">
	<el-form :model="form" >
		<el-form-item label="活动名称"   style="text-align: left;">
			<el-input v-model="form.name" style="width: 300px"></el-input>
		</el-form-item>
		<el-form-item label="活动区域" align="left"   style="text-align: left">
			<el-select v-model="form.region" placeholder="请选择活动区域" style="width: 300px">
				<el-option label="区域一" value="shanghai"></el-option>
				<el-option label="区域二" value="beijing"></el-option>
			</el-select>
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
				this.$refs.tree2.filter(val);
			}
		},
		methods:{
			onSubmit() {
				console.log('submit!');
				this.dialogFormVisible = true
			},
			tableRowClassName({row, rowIndex}) {
				if (rowIndex%2 === 1) {
					return 'warning-row';
				} else if (rowIndex%2 === 0) {
					return 'info-row';
				}
				return '';
			},
			handleNodeClick(data) {
				console.log(data.label);
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
				formLabelWidth: '100px',
				dialogFormVisible:false,
				search:'',
				filterText:'',
				formInline: {
					user: '',
					region: ''
				},
				tableData2: [{
					date: '2016-05-02',
					name: '王小虎1',
					address: '上海市普陀区金沙江路 1518 弄',
				}, {
					date: '2016-05-04',
					name: '王小虎2',
					address: '上海市普陀区金沙江路 1518 弄'
				}, {
					date: '2016-05-01',
					name: '王小虎3',
					address: '上海市普陀区金沙江路 1518 弄',
				}, {
					date: '2016-05-03',
					name: '王小虎4',
					address: '上海市普陀区金沙江路 1518 弄'
				}],
				form: {
					name: '',
					region: '',
					date1: '',
					date2: '',
					delivery: false,
					type: [],
					resource: '',
					desc: ''
				},
				data: [{
					label: '一级 1',
					children: [{
						label: '二级 1-1',
						children: [{
							label: '三级 1-1-1'
						}]
					}]
				}, {
					label: '一级 2',
					children: [{
						label: '二级 2-1',
						children: [{
							label: '三级 2-1-1'
						}]
					}, {
						label: '二级 2-2',
						children: [{
							label: '三级 2-2-1'
						}]
					}]
				}, {
					label: '一级 3',
					children: [{
						label: '二级 3-1',
						children: [{
							label: '三级 3-1-1'
						}]
					}, {
						label: '二级 3-2',
						children: [{
							label: '三级 3-2-1'
						}]
					}]
				}, {
					label: '一级 3',
					children: [{
						label: '二级 3-1',
						children: [{
							label: '三级 3-1-1'
						}]
					}, {
						label: '二级 3-2',
						children: [{
							label: '三级 3-2-1'
						}]
					}]
				}, {
					label: '一级 3',
					children: [{
						label: '二级 3-1',
						children: [{
							label: '三级 3-1-1'
						}]
					}, {
						label: '二级 3-2',
						children: [{
							label: '三级 3-2-1'
						}]
					}]
				}, {
					label: '一级 3',
					children: [{
						label: '二级 3-1',
						children: [{
							label: '三级 3-1-1'
						}]
					}, {
						label: '二级 3-2',
						children: [{
							label: '三级 3-2-1'
						}]
					}]
				}, {
					label: '一级 3',
					children: [{
						label: '二级 3-1',
						children: [{
							label: '三级 3-1-1'
						}]
					}, {
						label: '二级 3-2',
						children: [{
							label: '三级 3-2-1'
						}]
					}]
				}, {
					label: '一级 3',
					children: [{
						label: '二级 3-1',
						children: [{
							label: '三级 3-1-1'
						}]
					}, {
						label: '二级 3-2',
						children: [{
							label: '三级 3-2-1'
						}]
					}]
				}],
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
	background: #f0f1eb;
}
</style>