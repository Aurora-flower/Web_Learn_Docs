// Observer - 劫持数据的构造函数 - 接收 data - 即 observer 的形参 value
function Observer(data) {
    // this - Observer - 劫持（实例）对象
    // 将 data 对象进行存储 - 存储到劫持对象的 data 上
    this.data = data;
    // 开始数据劫持 - 调用原型对象上的 walk 方法，并传入 data
    this.walk(data); // 此时 this 是自身（或调用者）
}

// Observer 构造函数的原型对象
Observer.prototype = {
    // 当给一个函数对象的原型对象的 constructor 属性赋值时，实际上是在修改原型对象中的 constructor 属性。
    constructor: Observer, // 原型对象构造器 - Observer 构造函数

    // walk - 步行 - 接收一个 data 对象
    walk: function(data) {
        // me - this -  Observer - 劫持对象
        var me = this;
        // 得到 data 中的每个属性，并进行遍历
        Object.keys(data).forEach(function(key) {
            // 执行 convert（转换） 方法 - 传入 data 的每一个属性，和对应的属性值
            me.convert(key, data[key]);
        });
    },

    // 接收 data 对象的 key-value 键值对 - 把数据进行转换
    convert: function(key, val) {
        // defineReactive - 定义响应数据
        this.defineReactive(this.data, key, val); // this - Observer - 劫持对象
    },

    // 观察 defineReactive - 形成闭包 - 数据响应式的定义
    defineReactive: function(data, key, val) {
        var dep = new Dep();  // 创建一个 Dep 实例对象：{id, subs}

        // 深度递归数据劫持
        // val - 属性值 - 注意属性值的类型 - 根据属性的值，来决定是否要进行深度递归数据劫持。
        // 当 val 为 object (array\object) 类型，此时返回一个 Observer 实例
        var childObj = observe(val);

        // 为劫持对象的 data 添加 MVVM 实例 data 配置对象中的每个属性,并重写 get 与 set 方法
        Object.defineProperty(data, key, {
            enumerable: true, // 可枚举
            configurable: false, // 不能再 define
            get: function() {
                // 判断 Dep.target - watcher 对象是否 存在
                if (Dep.target) {

                    // 执行 dep 实例的原型对象的 depend 方法 - addDep
                    dep.depend();
                }
                return val; // 返回 val
            },
            // 外部修改值时，会为劫持对象进行数据代理劫持操作
            set: function(newVal) {
                // 判断新旧值是否相同
                if (newVal === val) {
                    return;
                }
                val = newVal;
                // 新的值是 object 的话，进行监听
                childObj = observe(newVal);
                // 通知订阅者 - 执行 dep 实例的原型对象的 notify 方法
                dep.notify();
            }
        });
    }
};

// 观察数据 - 接收一个 value 值，以及 vm 实例
function observe(value, vm) {
    // 当 value（即 data）不存在，或者 data 不为 object (array | object)时，不执行此函数
    if (!value || typeof value !== 'object') {
        return;
    }
    // 若是不满足，则返回 Observer 的实例（new），并传入 value - data
    return new Observer(value);  // 此时 this 是 window 全局对象
}


var uid = 0; // 用来标识 watcher 对象的 id 值？？？

// Dep 对象构造函数
function Dep() {
    // this - Dep - dep 实例
    this.id = uid++; // dep 对象的 id
    this.subs = []; // subs - 用来存储 watcher 对象
}

// Dep 构造函数对象的原型对象
Dep.prototype = {
    addSub: function(sub) {
        // this - Dep.target
        this.subs.push(sub);
    },

    // depend - 依赖 - Dep 对象与 Watcher 对象关系的建立
    depend: function() {
        // Dep.target 调用执行 addDep 方法-  传入 this - dep 实例
        Dep.target.addDep(this);
    },

    removeSub: function(sub) {
        var index = this.subs.indexOf(sub);
        if (index !== -1) {
            this.subs.splice(index, 1);
        }
    },

    notify: function() {
        // 将 subs 数组
        this.subs.forEach(function(sub) {
            sub.update();
        });
    }
};

Dep.target = null;  // Dep.target - null - watcher 对象