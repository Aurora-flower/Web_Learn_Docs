# 视口（viewport）
    
    指浏览器用来显示网页的区域，是浏览器窗口内网页的可视区域。
    视口相关的属性属于 BOM（Browser Object Model）即浏览器对象模型。

    BOM 是一组 JavaScript API，它表示浏览器窗口和文档对象之间互动的对象模型，
    提供了与浏览器功能相关的属性和方法，例如：控制浏览器的前进和后退按钮、
    获取和设置浏览器窗口的大小和位置、管理浏览器历史记录、控制弹出窗口等等。

## 常用属性和方法:

1. `window.innerWidth` 和 `window.innerHeight`:

    返回浏览器视口的宽度和高度，不包括滚动条和边框。

2. `document.documentElement.clientWidth` 和 `document.documentElement.clientHeight`: 

    返回文档根元素的宽度和高度，不包括滚动条和边框。

3. `document.documentElement.scrollWidth` 和 `document.documentElement.scrollHeight`: 

    返回文档根元素的实际宽度和高度，包括滚动条和边框。

4. `window.scrollX` 和 `window.scrollY`: 

    返回文档在水平和垂直方向上已经滚动的像素值。

5. `window.requestAnimationFrame()`:

    一个用于在每一帧触发回调函数的方法，可以优化动画的性能。

6. `window.matchMedia()`: 

    用于检查当前浏览器窗口是否匹配给定的 CSS 媒体查询，可以用于响应式布局设计。


## 视口相关的 CSS 属性:

1. `width` 和 `height`: 用于设置元素的宽度和高度。

2. `min-width` 和 `min-height`: 

   用于设置元素的最小宽度和最小高度，可以用于响应式布局设计。

3. `max-width` 和 `max-height`: 

   用于设置元素的最大宽度和最大高度，可以用于响应式布局设计。

总之，理解视口相关的属性和方法是前端开发中必不可少的一部分，可以帮助我们更好地处理浏览器窗口大小变化、响应式布局和动


### 元素的宽高

    要获取元素的宽和高，可以使用以下 DOM API 提供的属性：

1. offset 偏移量

    - Element.offsetWidth：

        表示元素的外部宽度，即包括元素的边框、内边距和 CSS 宽度。
        此属性值不包括水平滚动条、边框或外边距。

    - Element.offsetHeight：

        表示元素的外部高度，即包括元素的边框、内边距和 CSS 高度。
        此属性值不包括竖直滚动条、边框或外边距。


2. client 客户端

   - Element.clientWidth：

     表示元素的内部宽度，即不包括边框和滚动条但包括内边距。
     此值可以是小数，因此应用 Math.round() 可以使其四舍五入为最接近的整数。

   - Element.clientHeight：

     表示元素的内部高度，即不包括边框和滚动条但包括内边距。
     此值可以是小数，因此应用 Math.round() 可以使其四舍五入为最接近的整数。