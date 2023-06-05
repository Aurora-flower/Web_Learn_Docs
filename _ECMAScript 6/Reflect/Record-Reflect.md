在 ES6 中，`Reflect` 是一个内置Object对象，提供了一组用于操作对象的方法。

`Reflect` 的存在主要是为了将某些 Object 对象上原本属于语言内部的方法放到 Reflect 上，使得这些方法成为语言内部的普通函数。这样，我们就可以在方法执行前、执行后对其进行拦截和修改，更好地管理对象的行为。

`Reflect` 提供的方法包括：

- `Reflect.apply()`：调用一个函数，并传递一个给定的 this 值和一组参数。
- `Reflect.construct()`：使用给定的构造函数创建一个对象。
- `Reflect.defineProperty()`：为指定的对象定义一个新属性或修改已有属性，并返回一个 Boolean 值，表示是否操作成功。
- `Reflect.deleteProperty()`：从对象中删除一个属性，并返回一个 Boolean 值，表示是否操作成功。
- `Reflect.get()`：获取对象的某个属性的值。
- `Reflect.getOwnPropertyDescriptor()`：返回指定对象上一个自有属性对应的属性描述符
   （自有属性是指直接赋予该对象的属性，而非从原型链上继承的）。
- `Reflect.getPrototypeOf()`：返回给定对象的原型。
- `Reflect.has()`：判断一个对象是否存在某个属性。
- `Reflect.isExtensible()`：判断一个对象是否可扩展。
- `Reflect.ownKeys()`：返回一个由目标对象自身的属性键组成的数组。
- `Reflect.preventExtensions()`：防止一个对象被扩展。
- `Reflect.set()`：将属性设置为指定的值。
- `Reflect.setPrototypeOf()`：设置一个对象的原型。

使用 `Reflect` 可以更好地管理和控制对象的行为，同时也可以方便地实现一些元编程的需求。