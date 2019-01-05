<template>
	<main-layout>
		<el-container>
			<el-aside width="200px" style="height:90vh" align="center">
				<el-menu
				style="height: 100%;"
				default-active="PersonInfo"
				@select="handleSelect"
				>
				<el-menu-item index="PersonInfo">
					个人信息
				</el-menu-item>
				<el-menu-item index="OrganizationManger">
					组织管理
				</el-menu-item>
				<el-menu-item index="EmployeesManger">
					雇员管理
				</el-menu-item>
				<el-menu-item index="SystemConfig">
					系统配置
				</el-menu-item>
			</el-menu>
		</el-aside>
		<el-main style="padding: 0px;">
			<div :is="compoment"></div>
		</el-main>
	</el-container>
</main-layout>
</template>

<script>
	import MainLayout from '../layouts/Main.vue'
	import OrganizationManger from './configPages/OrganizationManger.vue'
	import EmployeesManger from './configPages/EmployeesManger.vue'
	import PersonInfo from './configPages/PersonInfo.vue'
	import SystemConfig from './configPages/SystemConfig.vue'

	export default {
		components: {
			MainLayout,
			'OrganizationManger':OrganizationManger,
			'EmployeesManger':EmployeesManger,
			'PersonInfo':PersonInfo,
			'SystemConfig':SystemConfig
		},
		data(){
			return {
				compoment:null
			}
		},
		mounted:function(){

		},
		methods:
		{
			handleSelect(key, keyPath) {
				console.log(key, keyPath);
				this.compoment = key
			},
		}
	}
</script>
