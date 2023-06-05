// region >>> Object.definedProperty

let o = {};


// 1. definedProperty
// 参数: (object, PropertyKey, attributesConfig)
// Tip: 直接对一个对象的操作，定义一个新属性或修改原对象属性，并返回该对象;
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

// Tip: value、writable 属性不能与 set 和 get 属性同时使用;

// 2.definedProperties
// 参数: (object, properties)
// Tip: 可以直接在一个对象上，定义多个新的属性或修改现有属性，并返回该对象;
Object.defineProperties(o, {
    "name": {
        value: "huayin",
		writable : true,
        configurable: true,
        enumerable: true
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
console.log(o);

// Tip: 两者的区别，在于 defineProperties 可以批量处理多个对象属性；
// endregion
