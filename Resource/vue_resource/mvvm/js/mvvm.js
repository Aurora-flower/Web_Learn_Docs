// MVVM 构造函数 - 接收一个配置对象
function MVVM(options) {
    // 为 MVVM 实例添加了 $options 属性 - 对 options 配置对象及它的 data 属性对象进行存储
    this.$options = options || {};
    // 为 MVVM 实例添加了 _data 属性，且将属性值进行存储 (this._data, data)
    var data = this._data = this.$options.data;
    var me = this; // this - 当前 MVVM 实例

    // 数据代理
    // 遍历 data 中的属性，生成一个数组进行遍历，实现 vm.xxx -> vm._data.xxx
    Object.keys(data).forEach(function (key) {
        me._proxyData(key); // 执行原型对象的 proxyData 方法
    });

    // 初始化计算属性
    this._initComputed();

    // observe - 观察 - 数据劫持
    // 传入存储的 data 及 当前 MVVM 实例 - 返回值为一个 Observer 实例
    observe(data, this);

    // 为 MVVM 实例添加了 $compile 属性 - 接收 Compile 的实例 - 传入 el 配置 或 默认位置的 body
    this.$compile = new Compile(options.el || document.body, this)
}

MVVM.prototype = {
    constructor: MVVM,
    $watch: function (key, cb, options) {
        new Watcher(this, key, cb);
    },

    // 数据代理（劫持）- 底层都经过 defineProperty
    // 接收 data 的属性，未设置 setter 与 getter 时，则重写
    _proxyData: function (key, setter, getter) {
        // me 指的是 MVVM 实例(proxyData 调用者)
        var me = this;
        // 为 vm 实例对象添加 data 中的每个属性，并且重写 getter 与 setter 方法，来实现数据代理。
        setter = setter ||
            // 重写 setter 的操作 - 将 data 的属性都代理（劫持）到实例身上
            /*
            {
              "$options": {
                "el": "#app",
                "data": {
                  "message": "hello world"
                }
              },
              "_data": {
                "message": "hello world"
              }
            }
            */
            Object.defineProperty(me, key, {
                configurable: false, // 是否可修改
                enumerable: true,   // 是否可遍历
                get: function proxyGetter() {
                    // 通过 key 去 实例的 _data 属性对象中查找对应的值
                    return me._data[key];
                },
                set: function proxySetter(newVal) {
                    // 通过 key 去 实例的 _data 属性对象中查找对应的值，并进行修改
                    me._data[key] = newVal;
                }
            });
    },


    _initComputed: function () {
        // me - MVVM 实例
        var me = this;
        // 创建计算属性 computed
        var computed = this.$options.computed;

        // 判断计算属性 computed 是否为 object (array \ object)
        if (typeof computed === 'object') {
            // 遍历 computed 对象的属性
            Object.keys(computed).forEach(function (key) {
                // 为计算属性配置对象的属性进行 set 和 get 的重写
                Object.defineProperty(me, key, {
                    // 判断 computed 配置对象下的属性是否为 function - true - 返回此函数\ false - 返回属性值（走 get）
                    get: typeof computed[key] === 'function'
                        ? computed[key]
                        : computed[key].get,
                    set: function () {
                    }
                });
            });
        }
    }
};