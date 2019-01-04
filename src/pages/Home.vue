<template>
  <main-layout>
  	<div id="logoDiv" >
      <div style="position: absolute;left: 1%;right:1%;filter:alpha(opacity=50)" align="center">
        <img id="logoImg" src="/logo.jpg" style="z-index: 10;width: auto;height: 89vh;"  alt="Logo" />
      </div>
    </div>

  </main-layout>
</template>

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
