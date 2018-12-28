<template>
  <div >
<el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect"
router>
  <el-menu-item index="/Home">处理中心</el-menu-item>
  <el-submenu index="2">
    <template slot="title">我的工作台</template>
    <el-menu-item index="/Home">选项1</el-menu-item>
    <el-menu-item index="/Home">选项2</el-menu-item>
    <el-menu-item index="/Home">选项3</el-menu-item>
    <el-submenu index="2-4">
      <template slot="title">选项4</template>
      <el-menu-item index="Home">选项1</el-menu-item>
      <el-menu-item index="Home">选项2</el-menu-item>
      <el-menu-item index="Home">选项3</el-menu-item>
    </el-submenu>
  </el-submenu>
  <el-menu-item index="/About">消息中心</el-menu-item>
</el-menu>
    <slot></slot>
  </div>
</template>

<script>
  import VLink from '../components/VLink.vue'

  export default {
    components: {
      VLink
    },
    data() {
      return {
        activeIndex: '1',
        activeIndex2: '1'
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>

