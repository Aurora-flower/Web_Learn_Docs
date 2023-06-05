// 创建一个对象
let o = {};


// 1. definedProperty
/*
参数: (object, PropertyKey, attributesConfig)
Tip: 直接对一个对象的操作，定义一个新属性或修改原对象属性，并规定该属性的一些特性，且返回该对象;
value、writable 属性不能与 set 和 get 属性同时使用;
*/
let value = "Hua";
let res = Object.defineProperty(
    o, 					// 表示要定义属性的对象
    "name", 			// 表示要定义或修改的属性名称

    // 属性描述 Descriptors
    {
        get: function () {
            return value;
        },					// 获取属性的回调，等同于 value 配置项
        set: function (v) {
            return value = v;
        },					// 设置属性的回调，等同于 writeable 配置项
        configurable: true,
        enumerable: true
    }
);
res.name = "HuaYin";
console.log(res);

// 2.definedProperties
/*
参数: (object, properties)
Tip: 可以直接在一个对象上，定义多个新的属性或修改现有属性，并规定属性的一些特性，且返回该对象;
*/
let result = Object.defineProperties(o, {
    "nickname": {
        value: "huayin",  // 属性的值
        writable: true, // 属性是否可写
        configurable: true, // 属性是否可以被删除
        enumerable: true  // 属性是否可枚举
    },
    "age": {
        get: function () {
            return this.value = "age";
        },					// 获取属性的回调，等同于 value 配置项
        set: function (v) {
            return this.value = v;
        },					// 设置属性的回调，等同于 writeable 配置项
        configurable: true,
        enumerable: true
    }
});
console.log(result);
console.log(o);

// Tip: 两者的区别，在于 defineProperties 可以批量处理多个对象属性；
