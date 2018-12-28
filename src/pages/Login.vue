<template>
	<div>
		<el-container style="height: 100vh">
			<el-header style="height: 30vh">
				<h1 align="center">LoginPage</h1>
			</el-header>
			<el-main >
				<el-row :gutter="0">
					<el-col :span="8"><div class="grid-content bg-purple"></div></el-col>
					<el-col :span="8"><div class="grid-content bg-purple">
						<el-form :label-position="labelPosition"  label-width="100px" :model="formLabelAlign">
							<el-form-item label="UserName：">
								<el-input v-model="userInfos.name"></el-input>
							</el-form-item>
							<el-form-item label="Password：">
								<el-input v-model="userInfos.password"></el-input>
							</el-form-item>
							<el-form-item align="right">
								<el-button type="primary" align="center" style="width: 100px" @click="onSubmit">Login</el-button>
							</el-form-item>
						</el-form>
					</div></el-col>
					<el-col :span="8"><div class="grid-content bg-purple"></div></el-col>
				</el-row>
			</el-main>
			<el-footer>
				<p align="center">Coryright By XXX</p>
			</el-footer>
		</el-container>
	</div>
</template>
<style>
.el-row {
	margin-bottom: 20px;
	&:last-child {
		margin-bottom: 0;
	}
}
.el-col {
	border-radius: 4px;
}
.grid-content {
	border-radius: 4px;
	min-height: 36px;
}
.row-bg {
	padding: 10px 0;
}
</style>
<script>
	export default {
		data(){
			return {
				userName:"",
				labelPosition:"left",
				userInfos: {
					name: '',
					password: '',
					type: ''
				}
			}
		},
		methods:{
			onSubmit()
			{

			}
		}
	}
</script>
