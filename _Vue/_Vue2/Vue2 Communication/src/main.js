import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false;

import router from "@/router";

// 按需引入
import {Popover, Button} from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(Popover);
Vue.use(Button);

/* 或写为
Vue.component(Popover.name, Popover);
Vue.component(Button.name, Button);
*/

import store from "@/store"


new Vue({
  // 安装总线,关联 Vue 实例
  beforeCreate() {
    Vue["prototype"].$bus = this;
  },
  // 关联 store 状态管理仓库
  store,
  // 关联 router 路由管理
  router,
  render: h => h(App),
}).$mount('#app')

