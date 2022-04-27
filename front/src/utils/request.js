import  request from '@/utils/http'

//这里配置URI地质
//什么请求  get 还是post

export function login(data){
    return request({
        url:'/user/login',
        method:"post",
        data
    })
}

export function Index(){
    return request({
        url:'/ty/ty',
        method:"post",
    })
}