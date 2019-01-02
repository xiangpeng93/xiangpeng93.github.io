import Vue from 'vue/dist/vue.common.js'
import router from './router'

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'

Vue.use(ElementUI)
Vue.use(VueRouter)
Vue.use(VueResource)

const app = new Vue({
	el:"#app",
	router
})