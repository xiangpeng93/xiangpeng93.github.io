import Home from "./pages/Home.vue"
import About from "./pages/About.vue"
import Login from "./pages/Login.vue"
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
      path: '/About',
      component: About
    }
  ]
})
  