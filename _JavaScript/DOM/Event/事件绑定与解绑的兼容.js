// region  (兼容性) DOM 的事件绑定与解绑

/*
DOM 0 - 普通使用 (on) - 获取事件对象，绑定事件回调
DOM 2 -
高级: 绑定-addEventListener \ 解绑-removeEventListener
低级: 绑定-attachEvent \ 绑定-detachEvent (IE 专属)

Tip: 绑定与解绑一定要指向同一个对象;
*/


/** Event
 * 参数: 元素节点对象，事件类型，事件回调
 * */

// DOM 事件绑定
function onBindEvent(node, eventType, handle) {
    if (node.addEventListener) {
        node.addEventListener(`'${eventType}'`, handle);
    } else {
        node["attachEvent"](`'on${eventType}'`, handle);
    }
}

// DOM 事件解绑
function offBindEvent(node, eventType, handle) {
    node.onclick = function () {
        if (node.removeEventListener) {
            node.removeEventListener(eventType, handle);
        } else {
            node["detachEvent"]('on' + eventType, handle);
        }
    }
}

// endregion
