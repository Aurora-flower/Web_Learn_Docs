// region >>> 单例模式 （Singleton Pattern）
/*
单例模式（Singleton Pattern）是一种创建型设计模式，其主要目的是确保某个类只有一个实例存在，并且提供全局访问点。它属于经典的GOF设计模式之一。

单例模式在实现时需要注意以下几点：

1. 将构造函数设为私有，以防止类外部直接实例化该类。
2. 提供一个静态成员变量来保存唯一的实例。
3. 提供一个公共的静态访问方法，以便其他对象可以获取该单例实例。

单例模式适用于需要全局访问唯一实例的场景，例如缓存、日志记录、配置管理等。但是，过度使用单例模式会使代码难以理解和维护，因此应该谨慎使用。
*/
// endregion

// 简单示例
function fun(){
    let instance = null;
    return function (name) {
        instance = new Object();
        instance.name = name;
        console.log(instance);
    }
}

let Fn = fun();
Fn("huayin"); // 输出 "{ name: "huayin" }"


// 完整地展示 JavaScript 实现单例模式的主要特征和用法
const Singleton = (function() {
    let instance; //声明变量，保存唯一实例

    function init() { //内部函数，创建单例对象
        // 私有变量和函数
        let privateVariable = "I am a private variable";
        function privateMethod() {
            console.log("I am a private method");
        }

        // 公共变量和函数
        return {
            publicVariable: "I am a public variable",
            publicMethod() {
                console.log("I am a public method");
            },
            getPrivateVariable() {
                return privateVariable;
            }
        };
    }

    return {
        getInstance() {
            if (!instance) { //判断实例是否已经存在
                instance = init();
            }
            return instance; //返回唯一实例
        }
    };
})();

//用法示例
const instance1 = Singleton.getInstance();
const instance2 = Singleton.getInstance();

console.log(instance1 === instance2); //输出 true
console.log(instance1.publicVariable); //输出 "I am a public variable"
console.log(instance1.getPrivateVariable()); //输出 "I am a private variable"


/**代码说明：
 * 在上面的示例代码中，使用了闭包来实现单例模式。
 * Singleton 函数返回一个对象，包括一个内部函数 init 来创建单例对象，
 * 以及一个返回唯一实例的静态方法 getInstance。
 *
 * 在内部函数 init 中，定义了私有变量和函数，以及公共变量和函数。
 * 我们可以通过调用 getInstance 方法来获取单例对象，若该对象还不存在，
 * 则会调用 init 函数创建对象并保存在 instance 变量中，之后返回该实例。
 *
 * */