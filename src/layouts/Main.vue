<template>
	<div style="height: 10vh">
		<el-menu  :default-active="$route.path" class="el-menu-demo" mode="horizontal" @select="handleSelect"
		router>
		<el-menu-item index="#" align="center" style="width: 200px" ><i class="el-icon-edit"></i><b>XXXX系统</b></el-menu-item>
		<el-menu-item index="/Home">人员组织信息</el-menu-item>
		<el-menu-item index="/About">其他信息</el-menu-item>
		
		<el-submenu index="#" style="float:right;">
			<template slot="title" ><i class="el-icon-service"></i>{{userName}}</template>
			<el-menu-item index="#">个人信息</el-menu-item>
			<el-menu-item index="#">修改密码</el-menu-item>
			<el-menu-item index="#">退出登录</el-menu-item>
		</el-submenu>

	</el-menu>
	
	<slot></slot>
</div>
</template>

<script>
	import routes from '../routes'
	export default {
		data() {
			return {
				userName:"测试名称"
			};
		},
		methods: {
			handleSelect(key, keyPath) {
				console.log(key,keyPath);
			}
		}
	}
</script>

