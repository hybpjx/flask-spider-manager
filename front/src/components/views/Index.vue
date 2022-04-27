<template>

  <nav class="navbar" role="navigation" aria-label="main navigation">
  <div class="navbar-brand">
    <a class="navbar-item" href="https://bulma.io">
      <img src="https://bulma.io/images/bulma-logo.png" alt="Bulma: Free, open source, and modern CSS framework based on Flexbox" width="112" height="28">
    </a>

    <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false">
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
    </a>
  </div>
</nav>

  <div class="table-container">

    <table class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth">
      <thead>
      <tr>
        <th><abbr title="Position"><strong>帖子标题</strong></abbr></th>
        <th>帖子链接</th>
        <th><abbr title="Played">作者</abbr></th>
        <th><abbr title="Won">点击数</abbr></th>
        <th><abbr title="Drawn">回复数</abbr></th>
        <th><abbr title="Lost">发布时间</abbr></th>
        <th>帖子简介</th>
      </tr>
      </thead>
      <tfoot>
      <tr>
        <th><abbr title="Position">帖子标题</abbr></th>
        <th>帖子链接</th>
        <th><abbr title="Played">作者</abbr></th>
        <th><abbr title="Won">点击数</abbr></th>
        <th><abbr title="Drawn">回复数</abbr></th>
        <th><abbr title="Lost">发布时间</abbr></th>
        <th>帖子简介</th>
      </tr>
      </tfoot>
      <tbody>
      <tr v-for="(data,key) in data_list" :key="key">
        <th>{{data.title}}</th>
        <td>
          <a :href="data.title_url" title="Leicester City F.C.">{{data.title_url}}</a>

        </td>
        <td>{{ data.author }}</td>
        <td>{{data.click_number}}</td>
        <td>{{data.replies_number}}</td>
        <td>{{ data.publish_date }}</td>
        <td>{{data.description}}</td>
      </tr>
      </tbody>
    </table>

  </div>


</template>

<script>

import {Index} from "@/utils/request";

export default {
  name: "Index",
  data() {
    return {
      data_list:[]
    }
  },
  created() {
    this.get_data()
  },
  methods:{
    get_data(){
      Index().then(res=>{
        if (res.status===200){
          console.log(res.data)
          this.data_list = res.data
        }else {
          console.log(res.status)
        }
      }).catch(error=>{
        console.log(error.response)
      })
    }
  }
}
</script>

<style scoped>

</style>