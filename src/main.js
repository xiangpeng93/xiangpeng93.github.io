import Vue from 'vue/dist/vue.common.js'
import router from './routes'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import Router from 'vue-router'
import Home from "./pages/Home.vue"
import About from "./pages/About.vue"
Vue.use(ElementUI)
Vue.use(Router)
console.log(router)

const app = new Vue({
  el:"#app",
  router
})
