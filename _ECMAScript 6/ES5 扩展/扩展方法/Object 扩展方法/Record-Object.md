ES6（ECMAScript 6）中，Object 对象新增了一些扩展方法，包括但不限于：

1. Object.assign()：

    用于将多个对象的属性合并到一个新对象中。可以使用该方法复制一个对象，
    或者将多个对象的属性合并到一个对象中。

2. Object.keys()：

    返回一个由目标对象的所有可枚举属性名组成的数组。

3. Object.values()：

    返回一个由目标对象所有可枚举属性的值组成的数组。

4. Object.entries()：

    返回一个由目标对象所有可枚举属性键值对组成的数组，
    每个键值对是一个包含两个元素的数组，
    第一个元素为属性名，第二个元素为属性值。

5. Object.getOwnPropertySymbols()：

    返回一个由目标对象所有 Symbol 类型的属性所组成的数组。

6. Object.getOwnPropertyDescriptor()：

    获取指定对象上一个自有属性对应的属性描述符，
    包括 value、writable、enumerable 和 configurable 等信息。

7. Object.defineProperty()：

    定义一个对象的一个新属性或修改一个对象的现有属性，并返回该对象。

以上是 ES6 中 Object 扩展方法的一部分，这些新方法大大增强了对象操作的能力，帮助开发者更加方便地进行对象的操作和处理。