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

// 定义一个接口
interface Animal {
    name: string;
    eat(food: string): void;
}

// 实现接口的类
class Dog implements Animal {
    name: string;

    constructor(name: string) {
        this.name = name;
    }

    eat(food: string) {
        console.log(`${this.name} is eating ${food}`);
    }
}

// 继承父类的子类
class Cat extends Dog {
    constructor(name: string) {
        super(name);
    }

    meow() {
        console.log(`${this.name} is meowing`);
    }
}

const dog = new Dog('Bob');
dog.eat('meat'); // 输出 "Bob is eating meat"

const cat = new Cat('Kitty');
cat.eat('fish'); // 输出 "Kitty is eating fish"
cat.meow(); // 输出 "Kitty is meowing"
