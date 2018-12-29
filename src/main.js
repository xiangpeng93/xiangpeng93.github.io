import Vue from 'vue/dist/vue.common.js'
import router from './router'
import routes from './routes'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import VueRouter from 'vue-router'

Vue.use(ElementUI)
Vue.use(VueRouter)
console.log(router)

const app = new Vue({
	el:"#app",
	router,
	data(){
		return{
			currentRoute: window.location.pathname
		}
	},
	computed: {
		ViewComponent () {
			const matchingView = routes[this.currentRoute]
			console.log(matchingView)
			return matchingView
			? require('./pages/' + matchingView + '.vue')
			: require('./pages/404.vue')
		}
	},
	render (h) {
		console.log(this.ViewComponent)
		return h(this.ViewComponent)
	}
})
window.addEventListener('popstate', () => {
  app.currentRoute = window.location.pathname
})
