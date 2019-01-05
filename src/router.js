import Home from "./pages/Home.vue"
import About from "./pages/About.vue"
import Login from "./pages/Login.vue"
import ConfigInfo from "./pages/ConfigInfo.vue"
import EmployeeInfos from "./pages/EmployeeInfos.vue"
import QueryEmployeeInfo from "./pages/QueryEmployeeInfo.vue"
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
      path: '/ConfigInfo',
      component: ConfigInfo
    },
    {
      path: '/About',
      component: About
    }
    
  ]
})
  