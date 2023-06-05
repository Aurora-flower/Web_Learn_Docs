# Base - 非脚手架创建 Vue应用

要创建一个非脚手架的 Vue 应用，可以按照以下步骤进行：

1. 引入 Vue.js 库文件

    在 HTML 文件中，需要引入 Vue.js 库文件，可以通过 CDN 或者本地文件进行引入，例如：

```html
<!-- 通过 CDN 引入 Vue.js -->
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

<!-- 本地引入 Vue.js 文件 -->
<script src="./vue.js"></script>
```

2. 创建 Vue 实例

    在 JavaScript 文件中，可以使用 Vue 构造函数创建一个 Vue 实例，例如：

```javascript
const app = new Vue({
  el: '#app',
  data: {
    message: 'Hello, Vue!'
  }
});
```

其中，el 属性指定了 Vue 实例挂载的 DOM 元素，data 属性指定了 Vue 实例的数据对象。在模板中可以使用 {{}} 或 v-bind 指令来绑定数据。

3. 编写模板

    在 HTML 文件中，可以编写 Vue 模板，例如：

```html
<div id="app">
  <p>{{ message }}</p>
</div>
```

其中，{{ message }} 表示使用数据对象中的 message 属性来展示文本。

4. 运行应用

可以在浏览器中打开 HTML 文件，即可运行 Vue 应用，观察页面效果。

_Tip: 非脚手架创建的 Vue 应用需要手动管理依赖和打包部署等工作。
因此对于大型项目来说，推荐使用脚手架工具来创建和管理 Vue 应用。_
