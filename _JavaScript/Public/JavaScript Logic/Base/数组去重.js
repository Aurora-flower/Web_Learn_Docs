// 定义数组去重函数
function removeArrayDuplicate(Array) {
    let newArray = [];
    // 从盒子内先拿出元素，放进新盒子
    for (let i = 0; i < Array.length; i++) {
        // 标记
        let flag = true;

        // 每次拿出的元素都要与新盒子内的元素进行比较；
        for (let j = 0; j < newArray.length; j++) {
            // 判断是否相同 若是相同则扔掉且不继续
            if (Array[i] === newArray[j]) {
                flag = false;
                break;
            }
        }
        // 经过筛选满足条件，则允许放进新盒子
        if (flag) {
            newArray[newArray.length] = Array[i];
        }
    }
    return newArray;
}

// 测试
let arr = [1, 2, 3, 3, 5, 7, 8, 8]
let result = removeArrayDuplicate(arr);
console.log(result)