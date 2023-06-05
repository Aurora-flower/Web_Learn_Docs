// 冒泡排序 - 正向
function sortFBubbleArray(Array) {
    // 外层 - 比较的轮数
    for (let i = 0; i < Array.length - 1; i++) {

        //  内层 - 每轮元素之间比较的次数
        for (let j = 0; j < Array.length - i - 1; j++) {
            if (Array[j] > Array[j + 1]) {
                // 两个变量间的交换
                let temp = Array[j];
                Array[j] = Array[j + 1];
                Array[j + 1] = temp;
            }
        }
    }
    return Array;
}

// 冒泡排序 - 反向
function sortBBubbleArray(Array) {
    for (let i = 0; i < Array.length - 1; i++) {
        for (let j = 0; j < Array.length - i - 1; j++) {
            if (Array[j] < Array[j + 1]) {
                // 两个变量间的交换
                let temp = Array[j];
                Array[j] = Array[j + 1];
                Array[j + 1] = temp;
            }
        }
    }
    return Array;
}

// Tip: 循环中使用 var 声明与 let (ES6)声明是有区别的，let 再。

// 测试
let arr = [1, 5, 9, 10, 20, 3, 7, 19, 8]
let result_f = sortFBubbleArray(arr);
let result_b = sortBBubbleArray(arr);
console.log(">>> 正向冒泡排序:", result_f);
console.log(">>> 反向冒泡排序:", result_b);