
/**
 * 在 Node.js 的早期版本中，CommonJS 是主要的模块系统，
 * 它使用 module.exports 来暴露一个模块，
 * 使用 require 函数来导入其他模块。
 * */

// CommonJS 导入
const greeter = require('./greeter');

// 调用
greeter.greet();

// 默认情况下，exports 只是一个指向 module.exports 的变量:
console.log(module.exports === exports)