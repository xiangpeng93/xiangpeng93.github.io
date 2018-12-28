import Home from "./pages/Home.vue"
import About from "./pages/About.vue"
import Router from 'vue-router'
export default new Router({
  mode: 'history',
  routes:[
    {    
      path: '/',
      component: Home
    },
    {
      path: '/Home',
      component: Home
    },
    {
      path: '/About',
      component: About
    }
  ]
})
  