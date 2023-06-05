// region >>> 依赖
// 根组件
import App from '@/App.vue';

// vue 相关方法
import {createApp} from 'vue';

// pinia 根 store
import {createPinia} from 'pinia';
export const pinia = createPinia();

// router 路由管理
import router from "@/router"

// 全局样式
import './assets/main.css';

// elementPlus
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css'; // 样式
// endregion

createApp(App)
    .use(pinia)
    .use(router)
    .use(ElementPlus)
    .mount('#app')
