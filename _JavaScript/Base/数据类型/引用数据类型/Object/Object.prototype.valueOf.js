/**
 * valueOf() 是 JavaScript 中用于返回对象的原始值的方法。
 * 在大多数情况下，当对象需要被强制转换为一个原始类型的时候，JS 引擎会自动调用它。
 * 例如，当我们在对一个对象进行加法运算的时候，JS 引擎会自动调用该对象的 valueOf() 方法，将其转换成一个原始值再进行计算。
 *
 * 对于内置的 JS 对象（比如 String、Number、Date 等），
 * 它们都会有自己的 valueOf() 方法来返回对应的原始值。
 * 而对于自定义的对象，如果没有重写 valueOf() 方法，
 * 则默认返回对象本身，不会进行任何转换。
 * */


// 返回内置 JS 对象对应的原始值
const str = "hello world";
console.log(str.valueOf());


/**
 * JavaScript 中，当我们使用对象作为原始类型时
 * （比如在使用相等运算符 == 比较时，或计算时），
 * 会自动调用对象的 valueOf() 方法来返回该对象对应的原始值。
 *
 * */
// 返回对象的原始值
const obj = {
    value: 42,

    //
    valueOf: function () {
        return this.value;
    }
}

/**
 * 默认情况下，Object.prototype.valueOf() 方法会返回对象本身。
 * 因为在大多数情况下，使用对象本身作为原始值是没有意义的。
 * 但是，可以通过重写对象的 valueOf() 方法来自定义该对象的原始值。
 * */
console.log(obj);
console.log(+obj);
console.log(obj.valueOf());
console.log(obj == 42);  // true
console.log(obj === 42);  // false - 本身仍是对象

