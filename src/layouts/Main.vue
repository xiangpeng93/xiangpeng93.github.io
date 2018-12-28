<template>
	<div style="height: 10vh">
		<el-menu  :default-active="$route.path" class="el-menu-demo" mode="horizontal" @select="handleSelect"
		router>
		<el-menu-item index="/Home">处理中心</el-menu-item>
		<el-menu-item index="/About">消息中心</el-menu-item>
	</el-menu>
	<slot></slot>
</div>
</template>

<script>

	export default {
		data() {
			return {
			};
		},
		methods: {
			handleSelect(key, keyPath) {
				console.log(key,keyPath);
			}
		}
	}
</script>

