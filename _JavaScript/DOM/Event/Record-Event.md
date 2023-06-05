# Event 事件


## 事件的绑定与解绑

### DOM0


DOM 0 事件的绑定和解绑是通过给元素属性赋值的方式实现的，即将事件名称作为元素对象的属性名，并将函数赋值给该属性。

例如，假设有一个按钮元素，我们可以通过如下代码来为它绑定一个点击事件处理函数:

```javascript
const btn = document.getElementById('myButton');
btn.onclick = function() {
  alert('Hello, world!');
};
```

在这个示例中，我们通过为按钮的 `onclick` 属性赋值来绑定一个点击事件处理函数。当用户单击按钮时，浏览器会执行该函数，并弹出一个消息框。

使用类似的方式可以移除元素上已经绑定的事件处理函数，即将元素属性值设为 null。

示例代码：

```javascript
btn.onclick = null;
```


需要注意的是，DOM 0 级事件绑定只能为元素绑定一个事件处理函数，如果我们想为同一个元素绑定多个事件处理函数，则需要使用 DOM 2 级事件绑定或其他方法来实现。(DOM 0 的事件模型有一些局限性，例如同一个事件类型只能对应一个处理函数（后赋值的处理函数会覆盖前面的），无法指定事件触发的捕获或冒泡阶段等。)

此外，DOM 0 级事件绑定还存在一些兼容性问题。在一些旧的浏览器或特定情况下，修改元素的属性可能会导致之前绑定的事件处理函数被覆盖或失效。因此，在实际开发中，建议使用 DOM 2 级事件绑定或更高级别的方式来实现事件绑定。

---

### DOM2


DOM Level 2 提供了两种方法来进行事件绑定和解绑，分别是 `addEventListener()` 和 `removeEventListener()`。

`addEventListener()` 方法用于给 DOM 元素添加事件监听器，该方法接收三个参数：

- 第一个参数是事件类型，如 "click"、"mouseover" 等。
- 第二个参数是事件处理函数，即将要执行的函数，可以是已定义的函数或者匿名函数。
- 第三个参数是一个布尔值，表示是否在捕获阶段（true）或冒泡阶段（false）触发事件处理函数，默认为 false。

示例代码：

```javascript
const btn = document.getElementById('btn');
function handleClick(event){
    console.log('Button clicked!');
}
btn.addEventListener('click', handleClick);
```

`removeEventListener()` 方法用于移除 DOM 元素上已经存在的事件监听器，该方法也需要三个参数：

- 第一个参数是事件类型，与 `addEventListener()` 方法相同。
- 第二个参数是事件处理函数，与 `addEventListener()` 方法相同。
- 第三个参数是一个布尔值，必须与 `addEventListener()` 调用时传入的值相同，表示是否在捕获阶段或冒泡阶段触发事件处理函数。

示例代码：

```javascript
btn.removeEventListener('click', handleClick);
```

需要注意的是，仅当添加和删除事件监听器的函数相同时，才能正确地移除事件监听器。如果事件监听器是匿名函数，则无法直接移除，需要先将其存储在变量中，然后再调用 `removeEventListener()` 方法移除。

```javascript
const btn = document.getElementById('btn');
const handleClick = function(event){
  console.log('Button clicked!');
};
btn.addEventListener('click', handleClick);
// 稍后...
btn.removeEventListener('click', handleClick);
```

---

### 低版本浏览器的事件

在不支持 DOM Level 2 的浏览器中，可以使用 IE 提供的 `attachEvent()` 和 `detachEvent()` 方法来进行事件绑定和解绑。

- `attachEvent()` 方法用于给 DOM 元素添加事件监听器，该方法接收两个参数：
    - 第一个参数是事件类型，如 "click"、"mouseover" 等。
    - 第二个参数是事件处理函数，即将要执行的函数，可以是已定义的函数或者匿名函数。

- `detachEvent()` 方法用于移除 DOM 元素上已经存在的事件监听器，该方法也需要两个参数：
    - 第一个参数是事件类型，与 `attachEvent()` 方法相同。
    - 第二个参数是事件处理函数，与 `attachEvent()` 方法相同。

需要注意的是，IE 中的事件流模型是基于冒泡模型的，因此 `attachEvent()` 方法默认在冒泡阶段触发事件处理函数。

示例代码：

```javascript
const btn = document.getElementById('btn');
function handleClick(event){
    console.log('Button clicked!');
}
btn.attachEvent('onclick', handleClick);
```

```javascript
btn.detachEvent('onclick', handleClick);
```

需要注意的是，如果同一个事件处理函数被多次绑定到同一个元素上，必须在解绑时指定相同的函数、事件类型和捕获/冒泡阶段，才能正确地移除事件监听器。
