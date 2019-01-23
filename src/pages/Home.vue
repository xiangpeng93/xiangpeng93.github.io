<template>
  <main-layout>
  	<div id="logoDiv">
    </div>
  </main-layout>
</template>
<style>
#logoDiv{
 height:100%;
 width:100%;
 position:fixed;
 background: url(/logo.jpg) no-repeat center;
 background-size:auto 100%;
}
</style>
<script>
  import MainLayout from '../layouts/Main.vue'
  export default {
    components: {
      MainLayout
    },
    data(){
      return {
      }
    },
    mounted:function(){
    },
    methods:
    {
    }
  }
</script>
