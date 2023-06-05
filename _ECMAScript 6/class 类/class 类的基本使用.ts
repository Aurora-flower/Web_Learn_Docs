// region >>> Class 类
/**
 * @author: 花楹一间
 * @Description:  class 相关知识
 * */

// 基础路径

// region >>> 关于类
// Tip: 类也是用于创建对象的模板，用代码封装数据以处理该数据。
/*
1. 类的组成：类表达式 & 类声明。 （特殊的函数）

2. 定义类 （class 关键字）
    类声明: class Name {} - 区别于函数声明，函数声明会提升，类声明不会。
    类表达式:
        let name = class {} - 未命名/匿名类
        let name = class name {} - 命名类 - 命名类的表达式的名称是该类体的局部名称，
        - 可通过类的 name 属性检索类体的局部名称。
Tip:
    - 类表达式也同样受到类型提升的限制。
    - 两者定义类的主体都执行在严格模式下。(如：构造函数、静态方法、原型方法、getter & setter)

3. 当调用静态或原型方法时未指定 this 值，那么方法内的 this 未 undefined。（“use strict”）

*/
// endregion

// 创建服务基类 - 父类
class Service {

    // 预先声明字段 （属性）
    // [x: string]: number;
    public name: string | undefined; // 公有属性，可以在任意位置访问和修改
    age: number | undefined; // Tip: 类中的属性和方法，默认为 publish
    protected skill: string | undefined = "code"; // 受保护属性，仅可以在基类与派生类中可以访问和修改

    // 私有字段 (# | private) -仅能在字段声明中预先预先定义，不能在之后赋值来创建。
    // Tip: 类外部引用私有字段是错误的，只允许在类内部中读取或写入。
    readonly secret: string | undefined = "I love you"; // readonly  只读修饰符，仅可以访问不可修改

    // 实例的类必须定义在类的方法内
    // Tip: constructor 方法用于创建和初始化一个由 class 创建的对象。- 每个类只能有一个 constructor
    constructor(name?: string, age?: number) {
        this.name = name;
        this.age = age;
    };

    // getter & setter
    // Tip: 访问器仅在以 ECMAScript 5 及更高版本为目标时可用
    private value: string | undefined = "getter_test"; // 私有属性，仅可以在本类中访问和修改
    get test() {
        return this.value;
    };

    set test(value) {
        this.value = value;
    }

    // Method - 一般方法，存在于原型上 prototype
    fun() {
        console.log(">>> fun");
    };

    // static 关键字用来定义一个类的一个静态方法。
    // Tip:调用静态方法不需要实例化该类，但不能通过一个类实例调用静态方法。- 即只被本身调用。
    static distance() {
        console.log(">>> distance");
    };
}
Service.distance();


// 静态或原型的数据属性必须定义在类定义的外部
(Service.prototype as any).file = "file";
console.log(Service.prototype);


// 创建派生类 - 子类
// extends 关键字 - 扩展子类，在类声明或表达式中用于创建一个类作为另一个类的子类；
class Api extends Service {
    constructor(name?: string, age?: number) {
        // 一个构造函数可以使用 super 关键字调用父类的构造函数
        super(name, age);
    }
}

let instance = new Api("HuaYin", 20);
instance.fun();

// endregion