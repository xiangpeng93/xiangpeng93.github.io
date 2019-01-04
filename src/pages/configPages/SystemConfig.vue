<template>
	<div style="margin: 5px">
		<el-tabs v-model="activeName" >
			<el-tab-pane label="主页图片" name="first">
				<el-row>
					<el-col :span="6">
						<el-upload  
						:action="uploadLogoPicUrl"
						list-type="picture"
						:on-success="handleAvatarSuccess"
						 >
						<el-button style="width: 100%"  type="primary" >选择主页图片</el-button>
					</el-upload>
				</el-col>
			</el-row>
		</el-tab-pane>
		<el-tab-pane label="其他配置" name="fourth">其他配置</el-tab-pane>
	</el-tabs>


</div>
</template>
<style type="text/css">
	.el-upload{
		width: 100%;
	}
</style>
<script>
	import linkUrl from "../../link.js"
	export default {
		data(){
			return{
				uploadLogoPicUrl:linkUrl["host"]+linkUrl["uploadHomePic"],
				activeName:"first"
			}
		},
		methods:{
			handleAvatarSuccess()
			{
				this.$message({
					message: '更新图片成功，请刷新页面查看',
					type: 'success'
				});
			},
		}
	}
</script>
