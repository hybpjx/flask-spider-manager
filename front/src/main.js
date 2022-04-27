import { createApp } from 'vue'
import App from './App.vue'
import 'bulma/css/bulma.css'
import {router} from "@/router";

// 导入 element-ui
import elementPlus from 'element-plus'
import 'element-plus/dist/index.css'


createApp(App).use(router).use(elementPlus).mount("#app")

