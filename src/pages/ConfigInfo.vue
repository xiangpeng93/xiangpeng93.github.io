<template>
  <main-layout>
      <el-row style="width: 100%;height: 90vh;">
        <el-col :span="5" style="height: 100%;">
          <el-menu
          style="height: 100%;"
          default-active="1"
          @select="handleSelect"
          >
          <el-menu-item index="PersonInfo">
            个人信息
          </el-menu-item>
          <el-menu-item index="OrganizationManger">
            组织管理
          </el-menu-item>
          <el-menu-item index="EmployeesManger">
            人员管理
          </el-menu-item>
          <el-menu-item index="SystemConfig">
            系统配置
          </el-menu-item>
        </el-menu>
      </el-col>
       <el-col :span="19" style="height: 100%;">
        <div :is="compoment"> </div>
       </el-col>
    </el-row>
  </div>
</main-layout>
</template>

<script>
  import MainLayout from '../layouts/Main.vue'
  import OrganizationManger from './configPages/OrganizationManger.vue'
  import EmployeesManger from './configPages/EmployeesManger.vue'
  import PersonInfo from './configPages/PersonInfo.vue'
  import SystemConfig from './configPages/SystemConfig.vue'

  export default {
    components: {
      MainLayout,
      'OrganizationManger':OrganizationManger,
      'EmployeesManger':EmployeesManger,
      'PersonInfo':PersonInfo,
      'SystemConfig':SystemConfig
    },
    data(){
      return {
        compoment:null
      }
    },
    mounted:function(){

    },
    methods:
    {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
        this.compoment = key
      },
    }
  }
</script>
