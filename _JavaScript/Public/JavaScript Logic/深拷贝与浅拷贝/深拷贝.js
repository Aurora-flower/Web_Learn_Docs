/**
 * 深拷贝：
 * 会创建一个新对象，精确拷贝数据，数据存储的地址均不相同，
 * 修改新对象的属性，不会影响原对象；
 *
 * Tip: 针对于 Object 与 Array 这样的引用数据类型；
 * */

// 自定义 cloneDeep_Object 深拷贝函数 - 拷贝对象
// Tip: 参数（对象，对象的属性-数组），参数二默认为全部的对象属性
function cloneDeep_Object(obj, keys = Object.keys(obj)) {
    const clone = {};
    keys.forEach((key) => {
        const k = key;
        if (key in obj) {
            clone[k] = obj[k];
        }
    })
    return clone;
}

let obj = {
    id: 1,
    name: "huayin",
    age: 23
}

let res = cloneDeep_Object(obj);
console.log(res);

let result = cloneDeep_Object(obj, ["id", "name"]);
console.log(result);
console.log(">>> 判断-cloneDeep_Object:", res === obj); // false


// JSON 转换
// Tip: 不能拷贝函数，会造成函数丢失


// 自定义深拷贝函数 - 递归

// function cloneDeep =




