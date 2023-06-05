// CommonJS 导出
/**
 * Tip: 在 CommonJS 中，一个模块的输出由 module.exports 和 exports 两个变量组成。
 *
 * module.exports 是真正地输出，表示模块对外暴露的对象或函数；
 * 而 exports 只是 module.exports 的一个辅助工具。
 *
 * 用 exports 覆盖了 module.exports，
 * 那么 exports 就不再指向 module.exports，而是指向另一个对象。
 * 这会导致当前模块的输出与预期不符。
 *
 * 虽然 exports 只是 module.exports 的一个引用，
 * 但是不能直接将 exports 赋值为一个新对象，
 * 否则会导致 exports 不再指向 module.exports。
 * 正确的做法是直接修改 exports 所指向的对象。
 *
 * */
module.exports = {
    greet: function() {
        console.log('Hello World');
    }
};


// exports 错误做法
/*
exports = {
  greet: function() {
     console.log('Hello World');
  }
};
*/

// exports 正确使用
exports.greet = function() {
    console.log('Hello World');
};


// Tip: 推荐只使用 module.exports 来进行模块导出，或者只使用 exports 来进行模块导出。