<template>

  <!--   导航栏     -->
  <div id="app">
    <nav class="navbar is-dark container" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">

        <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false"
           data-target="navbarBasicExample">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navbarBasicExample" class="navbar-menu">
        <div class="navbar-start">
          <a class="navbar-item"><span>爬虫管理系统</span></a>

          <router-link :to="{name:'Index'}" class="navbar-item">进入系统</router-link>

        </div>

        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <a class="button is-primary">
                <strong>登陆</strong>
              </a>
              <a class="button is-light"><span>退出</span></a>
            </div>
          </div>
        </div>
      </div>


    </nav>

    <Login></Login>

    <!--   注释说明     -->
    <div class="box container">
      <article class="media">
        <div class="media-left">
          <figure class="image is-64x64">
            <img src="https://bulma.io/images/placeholders/128x128.png" alt="Image">
          </figure>
        </div>
        <div class="media-content">
          <div class="content">
            <p>
              <strong>账号：</strong> <small>admin</small> <strong>密码：</strong><small>123</small>
              <br>
              本网站只做测试使用
            </p>
          </div>
          <nav class="level is-mobile">
            <div class="level-left">
              <a class="level-item" aria-label="reply">
              <span class="icon is-small">
                <i class="fas fa-reply" aria-hidden="true"></i>
              </span>
              </a>
              <a class="level-item" aria-label="retweet">
              <span class="icon is-small">
                <i class="fas fa-retweet" aria-hidden="true"></i>
              </span>
              </a>
              <a class="level-item" aria-label="like">
              <span class="icon is-small">
                <i class="fas fa-heart" aria-hidden="true"></i>
              </span>
              </a>
            </div>
          </nav>
        </div>
      </article>
    </div>


    <!--随便玩玩的 导航栏-->
    <progress class="progress is-small is-primary" max="100">15%</progress>
    <progress class="progress is-danger" max="100">30%</progress>
    <progress class="progress is-medium is-dark" max="100">45%</progress>
    <progress class="progress is-large is-info" max="100">60%</progress>


  </div>

</template>

<script>
import Login from "@/components/views/Login";
import axios from "axios";


export default {
  name: "Home",

  data() {
    return {}
  },
  components: {
    Login
  },

  methods: {

  }

}
</script>

<style scoped>

</style>