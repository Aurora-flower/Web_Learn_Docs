# MouseEvent对象属性

MouseEvent 对象是指一个鼠标事件的对象，它继承了 UIEvent 对象和 Event 对象的属性，也提供了一些自己的属性。

##  MouseEvent 对象的部分常见属性：

- `MouseEvent.clientX`：表示鼠标事件的发生点在可视区域中的水平坐标。
- `MouseEvent.clientY`：表示鼠标事件的发生点在可视区域中的垂直坐标。
- `MouseEvent.offsetX`：表示点击事件目标元素内部的水平坐标。
- `MouseEvent.offsetY`：表示点击事件目标元素内部的垂直坐标。
- `MouseEvent.screenX`：表示鼠标事件的发生点在屏幕上的水平坐标。
- `MouseEvent.screenY`：表示鼠标事件的发生点在屏幕上的垂直坐标。
- `MouseEvent.target`：表示触发该事件的目标元素。
- `MouseEvent.button`：表示触发事件的鼠标按键，其中 0 表示左键，1 表示中键，2 表示右键。

_以上属性只是 MouseEvent 对象的一部分属性。在实际开发中，
可以根据需要选择使用不同的 MouseEvent 属性来实现特定的功能。_

---

### 鼠标位置相关

    `clientX`、`pageX`、`offsetX` 都是 MouseEvent 对象的属性，表示鼠标事件发生的位置信息。

区别:

- `clientX\Y`：

    表示鼠标事件发生时，鼠标相对于浏览器窗口视口（viewport）的位置。

- `pageX\Y`：

    表示鼠标事件发生时，鼠标相对于整个页面文档的位置。
    如果文档没有滚动，则与 `clientX` 的值相等；
    如果文档有滚动，则需要加上文档滚动的距离。

- `offsetX\Y`：
   
    表示鼠标事件发生时，鼠标相对于事件目标元素的内边距盒子边缘的偏移量（即鼠标在目标元素内的相对位置）。
    如果事件目标元素有内边距，`offsetX` 的值会减去内边距 padding 的宽度。

  
**示例:**
```javascript
const element = document.getElementById("my-element");

element.addEventListener("click", function(event) {
  const clientX = event.clientX;
  const pageX = event.pageX;
  const offsetX = event.offsetX;
  
  console.log(`clientX: ${clientX}, pageX: ${pageX}, offsetX: ${offsetX}`);
});
```

需要注意的是，这些属性的值都是相对于当前事件的目标元素的参考系，而不是整个文档的参考系。
因此如果需要在页面中的任意位置获取鼠标的坐标，
可以使用 `MouseEvent.clientX` 和 `MouseEvent.clientY` 属性，加上当前文档的滚动距离即可。