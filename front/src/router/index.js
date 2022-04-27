import {createRouter, createWebHistory} from "vue-router";
// 要导入 component 的内容 然后注册到路由中
import Home from "@/components/Home";
import Login from "@/components/views/Login";
import Index from "@/components/views/Index";

const routes = [
    {
        path: '/',
        name: "Home",
        component: Home
    },
    // {
    //     path: '/login',
    //     name: 'Login',
    //     component: Login
    // },

    {
        path: '/index',
        name: 'Index',
        component: Index,
        // loginRequest: true
    },


]


export const router = createRouter({
    "history": createWebHistory(),
    "routes": routes
})

router.beforeEach(function (to, from, next) {

    if (to.path !== '/') {
        let ab = sessionStorage.getItem('referrer',) //储存来源路由
        if (ab) {
            next()
        } else {
            alert('请登录')
            next({
                path: '/'
            })
        }

    }else {
        next()
    }

})