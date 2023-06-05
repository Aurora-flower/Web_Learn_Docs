/**
 * 在 JavaScript 中，类成员修饰符是指可以用来限制和控制类成员（包括属性和方法）访问权限的关键词。
 *
 * 常见的类成员修饰符包括:
 * 1. public：公共访问修饰符，表示该成员可以被该类的所有实例对象、继承该类的子类、以及外部代码访问；
 * 2. private：私有访问修饰符，表示该成员只能被该类的实例对象访问，不能被子类或外部代码访问；
 * 3. protected：受保护的访问修饰符，表示该成员只能被该类的实例对象和继承该类的子类访问，不能被外部代码访问；
 * 4. static：静态修饰符，表示该成员属于类本身而不是类的实例对象，可以用类名直接调用；
 * 5. readonly：只读修饰符，表示该成员只能在声明时或构造函数中初始化，初始化后不能再修改。
 *
 * Tip: 其中，public 为默认访问修饰符，如果没有显式地指定访问修饰符，则成员默认为 public 类型。
 * */

class Person {
    public name; // 公共属性
    private age; // 私有属性
    protected gender; // 受保护的属性

    static country = 'China'; // 静态属性

    constructor(name, age, gender) {
        this.name = name;
        this.age = age;
        this.gender = gender;
    }

    public sayHello() { // 公共方法
        console.log(`Hello, my name is ${this.name}.`);
    }

    private getAge() { // 私有方法
        return this.age;
    }

    protected getGender() { // 受保护的方法
        return this.gender;
    }

    static getCountry() { // 静态方法
        return Person.country;
    }

    readonly id = Math.random(); // 只读属性
}

const p = new Person('Tom', 20, 'male');
// console.log(p.name); // Tom
// console.log(p.age); // undefined，私有属性无法在实例对象外部访问
// console.log(p.gender); // undefined，受保护属性无法在实例对象外部访问
console.log(Person.country); // China，静态属性可以通过类名直接访问
p.sayHello(); // Hello, my name is Tom.
// console.log(p.getAge()); // TypeError: p.getAge is not a function，私有方法无法在实例对象外部调用
// console.log(p.getGender()); // TypeError: p.getGender is not a function，受保护方法无法在实例对象外部调用
console.log(p.id); // 一个随机数值，只读属性可以读取但无法修改
// p.id = 123; // TypeError: Cannot assign to read only property 'id' of object '#<Person>'
