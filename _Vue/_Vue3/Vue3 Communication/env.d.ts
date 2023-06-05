
// 解决 ts 无法正确解析第三方插件-飘红问题
declare module "pubsub-js";

// 另一种解决方法：使用类型说明包
// npm i --save-dev @type/pubsub-js;

// Tip:
// <reference types="vite/client" />
