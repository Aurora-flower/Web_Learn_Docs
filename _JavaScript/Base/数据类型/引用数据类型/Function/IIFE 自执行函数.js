// region >>> IIFE 自执行函数
// 语法：
// (function(){}())  == (function(){})()  ==  [ES6] { }

// 方式 1：
(function () {
    console.log(">>> IIFE 自执行函数_1");
}());

// 方式 2：
(function() {
    console.log(">>> IIFE 自执行函数_2");
})();

// 方式 3：
{
    console.log(">>> IIFE 自执行函数_3");
}

// Tip: 每个自执行函数后都要以 “;” 结尾，以防止解析错误；
// endregion
