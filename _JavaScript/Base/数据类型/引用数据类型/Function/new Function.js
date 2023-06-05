// new Function()
/**
 *  new Function() 是 JavaScript 提供的一个构造函数，用于创建一个新的函数对象。
 *
 * 仅有一个参数时，函数无参，参数作为函数体内容;
 * 有多个参数时，最后一个参数作为函数体的内容;
 *
 * */

// 声明定义函数
let add = (a, b) => {
    return a + b
};

// 通过 new Function 创建一个函数
let fun = new Function("a", "b", "return a+b");

setTimeout(() => {
    // console.log(fun);
    let one = add(1, 2)
    let two = fun(1, 2);
    console.log(">>>", one === two); // true
}, 1000);