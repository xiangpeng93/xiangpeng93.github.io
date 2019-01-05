<template>
	<div style="margin: 10px;width:99%;height:87vh;overflow-y:scroll;" >
		<el-tree
		:data="organizationData"
		default-expand-all
		:expand-on-click-node="false"

		>
		<span class="custom-tree-node" slot-scope="{ node, data }">
			<span>{{ node.label }}</span>
			<span>
				<span style="margin-left: 10px" />
				<el-button
				type="text"
				size="mini"
				@click="() => append(data)">
				添加
			</el-button>
			<span style="margin-left: 10px" />
			<el-button
			type="text"
			size="mini"
			@click="() => remove(node, data)"
			style="color: red">
			删除
		</el-button>
	</span>
</span>
</el-tree>
</div>
</template>

<script>
	import linkUrl from "../../link.js"
	export default {

		data() {
			return {
				organizationData: [],
				userName:'',
				userSession:''
			}
		},
		mounted(){
			this.userName = this.getCookie('name')
			this.userSession = this.getCookie('session')
			console.log(this.userName,this.userSession);
			if(this.userName === "")
			{
				//this.transToLogin()
			}
			else
			{
	        	//发送get请求
	        	this.$http.jsonp(linkUrl["host"]+"/getOrgs", {
	        		params: {
	        			"name": this.userName,
	        			"session": this.userSession
	        		}
	        	}).then(function(res) {
	        		console.log(res);
	        		this.organizationData = res.data;
	        	}, function(res) {
		            //this.transToLogin()
		            console.warn(res);
		        })
	        }
	    },
	    methods: {
	    	append(data) {
	    		this.$prompt('请输入组织名称', '添加组织', {
	    			confirmButtonText: '确定',
	    			cancelButtonText: '取消',
	    			inputPattern:"",
	    			inputErrorMessage:""
	    		}).then(({ value }) => {
	    			
	    			this.$http.jsonp(linkUrl["host"]+"/addOrgInfo", {
	    				params: {
	    					"name": this.userName,
	    					"session": this.userSession,
	    					"orgName":value,
	    					"parentOrgId":data.id
	    				}
	    			}).then(function(res) {
	    				console.log(res);
	    				if (res.data["result"] == "OK") {
	    					const newChild = {  label: value, children: [] ,id:res.data["id"]};
	    					if (!data.children) {
	    						this.$set(data, 'children', []);
	    					}
	    					data.children.push(newChild);
	    					this.$message({
	    						type: 'success',
	    						message: '组织添加成功: ' + value
	    					});
	    				}
	    				else
	    				{
	    					this.$message({
	    						type: 'error',
	    						message: '组织添加失败: ' + value
	    					});
	    				}
	    			}, function(res) {
	    				console.warn(res);
	    				this.$message({
	    					type: 'error',
	    					message: '组织添加失败: ' + value
	    				});
	    			})
	    		}).catch(() => {
	    			this.$message({
	    				type: 'info',
	    				message: '取消添加组织'
	    			});       
	    		});
	    	},
	    	remove(node, data) {
	    		this.$confirm('此操作将永久删除该组织, 是否继续?', '提示', {
	    			confirmButtonText: '确定',
	    			cancelButtonText: '取消',
	    			type: 'warning',
	    		}).then(() => {

	    			this.$http.jsonp(linkUrl["host"]+"/delOrgInfo", {
	    				params: {
	    					"name": this.userName,
	    					"session": this.userSession,
	    					"orgId":data.id
	    				}
	    			}).then(function(res) {
	    				console.log(res);
	    				if (res.data["result"] == "OK") {
	    					const parent = node.parent;
	    					const children = parent.data.children || parent.data;
	    					const index = children.findIndex(d => d.id === data.id);
	    					children.splice(index, 1);
	    					this.$message({
	    						type: 'success',
	    						message: '删除成功!'
	    					});
	    				}
	    				else
	    				{
	    					this.$message({
	    						type: 'error',
	    						message: '删除失败!'
	    					});
	    				}
	    			}, function(res) {
	    				console.warn(res);
	    				this.$message({
	    					type: 'error',
	    					message: '删除失败!'
	    				});
	    			})
	    		}).catch(() => {
	    			this.$message({
	    				type: 'info',
	    				message: '已取消删除'
	    			});
	    		});
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
	};
</script>
