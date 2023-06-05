// region >>> Object.create
// 参数: (prototypeObject || null, newObject)
// Tip: 以一个对象为原型，创建并返回一个新的对象;
let value = "前端开发技能";

let res = Object.create({}, {
    name: {
        value: "New Object",	// 属性值
        writable: false, 		// 是否可修改
        enumerable: true,		// 是否可遍历
        configurable: false	// 是否可删除
    },
    age: {
        value: 23,				// 默认为 undefined
        // writable: true,		// 默认为 false
        enumerable: true,		// 默认为 false
        // configurable : false	// 默认为 true
    },
    skill: {
        // 获取当前属性时的回调函数，等同于 value 配置项
        get: function () {
            return value;
        },
        // 对象简写，设置当前属性时的回调函数，等同于 writable 配置项
        set(v) {
            // Tip: 触发修改的时候，会接收到要修改为的数据；
            return value = v;
        },
        enumerable: true,
        configurable: false
    }
});

// 修改对象属性
res.skill = "hello";  	// skill : "hello"

// 删除对象属性
delete res.name;  		// delete 操作符失效，configurable 配置生效
// res.name = undefined

// 遍历对象属性 && enumerable 默认值: true
for (let i in res) {
    console.log(i);		// 遍历成功
}

// 未配置情况下，writable 默认值: false
res.age = 22;

// 未配置情况下，configurable 默认值: false
delete res.age;

// 测试打印
console.log(res.name, res.age, res.skill);
console.log(res);

// endregion
