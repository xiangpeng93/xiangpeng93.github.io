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
					<el-form-item label="审批人">
						<el-input v-model="formInline.user" placeholder="审批人"></el-input>
					</el-form-item>
					<el-form-item label="活动区域">
						<el-select v-model="formInline.region" placeholder="活动区域">
							<el-option label="区域一" value="shanghai"></el-option>
							<el-option label="区域二" value="beijing"></el-option>
						</el-select>
					</el-form-item>
					<el-form-item>
						<el-button type="primary" @click="onSubmit">查询</el-button>
					</el-form-item>
				</el-form>
			</el-header>
			<el-main>
				<el-table
				:data="tableData2"
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
</el-table>
</el-main>
</el-container>
</el-container>
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
			},
			tableRowClassName({row, rowIndex}) {
				if (rowIndex === 1) {
					return 'warning-row';
				} else if (rowIndex === 3) {
					return 'success-row';
				}
				return '';
			},
			handleNodeClick(data) {
				console.log(data);
			},
			filterNode(value, data) {
				if (!value) return true;
				return data.label.indexOf(value) !== -1;
			}
		},
		data() {
			return {
				filterText:'',
				formInline: {
					user: '',
					region: ''
				},
				tableData2: [{
					date: '2016-05-02',
					name: '王小虎',
					address: '上海市普陀区金沙江路 1518 弄',
				}, {
					date: '2016-05-04',
					name: '王小虎',
					address: '上海市普陀区金沙江路 1518 弄'
				}, {
					date: '2016-05-01',
					name: '王小虎',
					address: '上海市普陀区金沙江路 1518 弄',
				}, {
					date: '2016-05-03',
					name: '王小虎',
					address: '上海市普陀区金沙江路 1518 弄'
				}],
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
    background: #f0f9eb;
  }
</style>