<template>
	<main-layout>
		<el-container>
			<el-aside width="200px" style="height:90vh" align="center">
				<el-menu
				style="height: 100%;"
				@select="handleSelect"
				>
				<!-- <el-menu-item index="PersonInfo">
					个人信息
				</el-menu-item> -->
				<el-menu-item index="ClothingUsedInfo">
					领用记录
				</el-menu-item>
				<el-menu-item index="ClothingUse">
					服装库存
				</el-menu-item>
				<el-menu-item index="ClothingConfig">
					服装配置
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
	import ClothingUse from './clothingPages/ClothingUse.vue'
	import ClothingUsedInfo from './clothingPages/ClothingUsedInfo.vue'
	import ClothingConfig from './clothingPages/mangerCothing.vue'

	export default {
		components: {
			MainLayout,
			'ClothingUse':ClothingUse,
			'ClothingUsedInfo':ClothingUsedInfo,
			'ClothingConfig':ClothingConfig
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
