const {defineConfig} = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true,
    lintOnSave: false
})

module.exports = {
    publicPath: './',

    lintOnSave: false,
    devServer: {
        proxy: {
            '/api': {
                target: 'http://127.0.0.1:5000', //接口域名
                changeOrigin: true,             //是否跨域
                ws: true,                       //是否代理 websockets
                secure: true,                   //是否https接口
                pathRewrite: {                  //路径重置
                    '^/api': ''
                }
            },
            '/index': {
                target: 'http://127.0.0.1:5000/ty', //接口域名
                changeOrigin: true,             //是否跨域
                ws: true,                       //是否代理 websockets
                secure: true,                   //是否https接口
                pathRewrite: {                  //路径重置
                    '^/index': ''
                }
            }
        }
    }
};