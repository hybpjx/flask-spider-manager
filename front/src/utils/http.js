import axios from "axios"; // 要导入安装的宝 ，直接写包名即可，不需要写路径


// 实例化

const http = axios.create({
    baseURL:'http://127.0.0.1:5000', // 请求的公共路径，一般写服务器默认的api地址，，这个地质在具体使用的时候覆盖
    timeout:8000,                        // 最大的请求超时，超过这个时间就报错，有文件上传的站点 不需要设置
    headers:{
        "X-Custom-Header":"foobar" // 默认的自定义请求头，一般工作中这里填写隐藏了客户端身份的字段
    },
})

// 暴露变量
export default http;