import Home from "./pages/Home.vue"
import About from "./pages/About.vue"
import Login from "./pages/Login.vue"
import ConfigInfo from "./pages/ConfigInfo.vue"
import EmployeeInfos from "./pages/EmployeeInfos.vue"
import QueryEmployeeInfo from "./pages/QueryEmployeeInfo.vue"
import WorkOverTimeAnalyze from "./pages/WorkOverTimeAnalyze.vue"
import RewardAnalyze from "./pages/RewardAnalyze.vue"
import ClothingManger from "./pages/ClothingManger.vue"
import TaxManger from "./pages/TaxManger.vue"

import Router from 'vue-router'
export default new Router({
	mode: 'hash',
	base: '/',
	routes:[
	{    
		path: '/',
		component: Login
	},
	{
		path: '/Home',
		component: Home
	},
	{    
		path: '/EmployeeInfos',
		component: EmployeeInfos
	},
	{
		path: '/QueryEmployeeInfo',
		component: QueryEmployeeInfo
	},
	{
		path: '/WorkOverTimeAnalyze',
		component: WorkOverTimeAnalyze
	},
	{
		path: '/ClothingManger',
		component: ClothingManger
	},
	{
		path: '/RewardAnalyze',
		component: RewardAnalyze
	},
	{    
		path: '/ConfigInfo',
		component: ConfigInfo
	},
	{    
		path: '/TaxManger',
		component: TaxManger
	},
	{
		path: '/About',
		component: About
	}
	
	]
})
