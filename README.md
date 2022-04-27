# 前端部署
安装vue项目
`vue create front`

安装bluma.css
`npm i bulma`
https://bulma.io/
https://www.bulmacss.cn/

在main.js中添加
```
import bulma from "bulma/bulma.sass"
```

安装 element ui-plus
安装 router
安装 axios



# 后端部署
安装flask
`pip install flask`
以及一些常规组件
`pip install flask_session`
`pip install flask_cors`
`pip install flask_login`
`pip install flask-wtf`

简单的settings设置
在backend下面新建settings/dev.py


主程序中设置倒入并且设置

## 设置用户模块
每个模块要设置好跨域
并且 封装好数据交付前端

## 设置数据板块
直接从爬虫数据库获取数据

# 爬虫

- 安装库
`pip install scrapy`

`pip install Pymysql`

`pip install JsonRequest`
其他操作均简单 主要设置好管道 和settings
导入的库
> scrapy pymysql SqlLite3



