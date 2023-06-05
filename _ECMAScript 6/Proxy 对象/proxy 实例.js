// Proxy 对象
/**
 * new Proxy()是 JavaScript 中的一个内置对象，它允许我们创建一个代理对象，用于拦截并可以自定义目标对象上的各种操作。
 * 在 JavaScript 中，通常使用 Object.defineProperty 或者 Object.defineProperties 来进行数据劫持，但是这些方法限制和局限性比较大。
 * 而使用 new Proxy() 对象可以更加灵活地实现数据劫持、属性拦截、自定义操作等。
 * 通过在 Proxy 对象上定义一些拦截方法，可以实现对代理对象的各种操作进行自定义处理和控制。
 * */
// 目标对象
let target = {};

// Proxy 代理对象
/** 参数:
 * target（必需）：
 *  表示需要代理的目标对象，可以是任何类型的对象，包括原始类型（如字符串、数值等）以及函数。
 *
 * handler（可选）：
 *  一个代理处理程序对象，它定义了代理对象的行为方式，即代理对象的钩子函数或拦截方法。
 *  如果未提供此参数，则该代理对象的钩子函数与目标对象相同。
 * */
let proxy = new Proxy(target,{
    // 定义了 get() 和 set() 方法，用于拦截获取和设置对象属性值的操作
    get(target, prop) {
        // Tip: target - 被代理的目标对象; prop - 需要访问的属性;
        console.log(`Getting property ${prop}`);
        return target[prop];
    },
    set(target, prop, value) {
        // Tip: value - 要修改的值
        console.log(`Setting property ${prop} to ${value}`);
        target[prop] = value;
    }
});

proxy.name = "Tom";

console.log(proxy.name); // Getting property name, Tom
console.log(target); // { name: 'Tom' }


