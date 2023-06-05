/**
 * 浅拷贝：
 * 会创建一个新对象，精确拷贝数据，但引用数据存储的地址相同，
 * 修改新对象的属性，会影响原对象；
 * */


// 直接赋值
let pre_obj = {name: "JoJo"};
let clone_assignment = pre_obj;
console.log(">>> 判断-直接赋值:", pre_obj === clone_assignment); // true

// 扩展运算符号
let previous_obj = {name: "小叮当", age: 12};
let clone_extend = {...previous_obj};
console.log(">>> 判断-扩展运算符号:", previous_obj === clone_extend); // false

// Object.assign 合并
let assign_target_object = {
    name: "小白",
    age: 20,
    skill: function () {
        console.log(">>> 吃遍天下美食.");
    }
}
let clone_assign = {};

// Tip: 由 参数2 -> 参数1
Object.assign(clone_assign, assign_target_object);
console.log(">>> 判断-assign:", clone_assign === assign_target_object)

