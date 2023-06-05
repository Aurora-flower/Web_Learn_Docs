/**
 * 在 TypeScript 中，抽象类和 Java 中的抽象类概念类似，
 * 用于描述一个具体的类所应该拥有的方法和属性，但是并不需要实现这些方法或属性。
 * 通常情况下，抽象类是被设计用来作为其他类的基类，规范子类中应该具有的方法和属性，而不是直接被实例化的。
 * */


// Tip: 抽象类中可以包含抽象方法、普通方法和属性。
// 抽象方法没有具体实现，其语法与普通方法相似，只是方法定义前面多了一个 abstract 关键字
abstract class Animal {
    abstract makeSound(): void;
    move(): void {
        console.log("Animal is moving.");
    }
}


// Tip: 抽象类中的抽象方法必须被子类实现，否则编译器会提示错误。
class Dog extends Animal {
    makeSound(): void {
        console.log("Dog is barking.");
    }
}

let dog = new Dog();
dog.makeSound(); // 输出: "Dog is barking."
dog.move(); // 输出: "Animal is moving."