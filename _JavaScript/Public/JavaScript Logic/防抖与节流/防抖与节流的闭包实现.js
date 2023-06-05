// 防抖函数和节流函数均使用闭包，在内部函数中可以访问外部函数的变量和参数，从而实现了防抖和节流的功能。

// 防抖函数的实现
function debounce(fn, delay) {
    let timer = null;
    return function () {
        const context = this; // 保存调用者的 this 指向;
        const args = arguments; // 接收外部函数的参数
        if (timer) {
            clearTimeout(timer);  // 清除上一次定时器 timer
        }
        timer = setTimeout(function () {
            fn.apply(context, args); // 修改传递进来的函数的 this 指向，并传递外部函数的参数；
        }, delay);
    };
}

// 节流函数的实现
function throttle(fn, delay) {
    let lastTime = 0;
    return function () {
        const context = this;
        const args = arguments;
        const currentTime = new Date().getTime();
        if (currentTime - lastTime >= delay) {
            fn.apply(context, args);
            lastTime = currentTime;
        }
    };
}