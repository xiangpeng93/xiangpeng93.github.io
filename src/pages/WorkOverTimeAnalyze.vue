<template>
  <main-layout>
    <el-container>
      <el-aside width="200px">
        <el-upload
        :action="uploadUrl"
        multiple
        style="margin: 5px;"
        :on-success="getEmployeesInfo"
        >
        <el-button style="width: 100%!important;" type="primary">点击上传</el-button>
      </el-upload>
    </el-aside>
    <el-main style="height:90vh">
     <el-table
     :data="OvertimeData"
     :span-method="arraySpanMethod"
     border
     style="width: 100%">
     <el-table-column
     prop="name"
     label="姓名">
   </el-table-column>
   <el-table-column
   prop="comp"
   label="公司">
 </el-table-column>
 <el-table-column
 prop="proj"
 label="项目">
</el-table-column>
<el-table-column
prop="job"
label="职务">
</el-table-column>
<el-table-column
prop="startTime"
label="开始时间">
</el-table-column>
<el-table-column
prop="endTime"
label="结束时间">
</el-table-column>
<el-table-column
prop="days"
label="天数">
</el-table-column>
<el-table-column
prop="hours"
label="小时数">
</el-table-column>
<el-table-column
prop="leaves"
label="是否调休">
</el-table-column>
</el-table>
</el-main>
</el-container>
</main-layout>
</template>
<style>
.el-upload {
  width: 100%!important;
}
</style>
<script>
  import MainLayout from '../layouts/Main.vue'
  import linkUrl from "../link.js"
  export default {
    components: {
      MainLayout
    },
    data(){
      return {
        host:linkUrl["host"],
        uploadUrl:linkUrl["host"]+"/UploadWorkOvertime",
        OvertimeData:[]
      }
    },
    mounted:function(){
      this.userName = this.getCookie('name')
      this.userSession = this.getCookie('session')
    },
    methods:
    {
      getEmployeesInfo() {
        this.$http.jsonp(this.host+"/getWorkOvertimeData", {
          params: {
            "name": this.userName,
            "session": this.userSession
          }
        }).then(function(res) {
          console.log(res);
          this.OvertimeData = res.data;
        }, function(res) {
          console.warn(res);
        })
      },
      arraySpanMethod({ row, column, rowIndex, columnIndex }) {
        if (row.name === "合计") {
          if (columnIndex === 0) {
          // 从第二列开始
          return [1, 6]
        }
        else if (columnIndex < 6)
        {
          return [0, 0];
        }
      }
    },

    getCookie(c_name) {
      if (document.cookie.length > 0) {
        var c_start = document.cookie.indexOf(c_name + "=")
        if (c_start != -1) {
          c_start = c_start + c_name.length + 1
          var c_end = document.cookie.indexOf(";", c_start)
          if (c_end == -1) c_end = document.cookie.length
            return unescape(document.cookie.substring(c_start, c_end))
        }
      }
      return ""
    }
  }
}
</script>
