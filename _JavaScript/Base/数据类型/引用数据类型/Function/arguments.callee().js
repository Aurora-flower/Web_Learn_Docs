var n = 0;

function fun() {
    if (n >= 10) {
        return;
    }
    console.log('海天酱油' + n);

    n++;

    // 假如在开发的过程中，有人污染了这个命名
    fun = 11111;  // 变量声明，命名污染；
    // f1();  // 报错 Error

    arguments.callee();  // 此方法可以避免可能存在的命名污染问题
}
fun();