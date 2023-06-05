/** implements & extends:
 * 1. implements 用于继承接口或抽象类中的方法和属性。
 *  通过使用 implements 关键字，一个类可以强制实现某个接口中定义的所有方法和属性，
 *  并且这些方法和属性必须在派生类中被重写或者实现。
 *
 * 2. extends 用于继承基类中的方法和属性。
 *  通过使用 extends 关键字，一个子类可以从一个父类继承其所有的方法和属性，
 *  并且还可以添加自己的方法和属性。子类可以重写父类中的方法和属性，以实现自己的特定功能。
 *
 * 简而言之，implements 主要用于规范接口，让实现该接口的类满足一定的要求，而 extends 则主要用于扩展和复用已有的类。
 * */
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
// 实现接口的类
var Dog = /** @class */ (function () {
    function Dog(name) {
        this.name = name;
    }
    Dog.prototype.eat = function (food) {
        console.log("".concat(this.name, " is eating ").concat(food));
    };
    return Dog;
}());
// 继承父类的子类
var Cat = /** @class */ (function (_super) {
    __extends(Cat, _super);
    function Cat(name) {
        return _super.call(this, name) || this;
    }
    Cat.prototype.meow = function () {
        console.log("".concat(this.name, " is meowing"));
    };
    return Cat;
}(Dog));
var dog = new Dog('Bob');
dog.eat('meat'); // 输出 "Bob is eating meat"
var cat = new Cat('Kitty');
cat.eat('fish'); // 输出 "Kitty is eating fish"
cat.meow(); // 输出 "Kitty is meowing"
