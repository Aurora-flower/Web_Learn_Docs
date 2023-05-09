JavaScript 中，模块化的实现一直是个比较棘手的问题。ES6 引入的新特性里面也包括了完全重新设计的模块系统，它可以帮助开发者更好地组织代码，增强代码重用性，减少命名冲突等问题。

在 ES6 中，我们可以使用 `export` 和 `import` 语句来进行模块化编程。

`export` 关键字用于暴露模块中的内容，在 ES6 中一共有三种暴露方式：

1. 默认导出：使用 `export default` 将一个对象或值作为默认输出。这种方式只能默认导出一个值，而且在导入时可以不加花括号。

   ```javascript
   // 导出
   export default function sayHello() {
     console.log('Hello!');
   }
   
   // 导入
   import sayHello from './module/defaultExport.js';
   sayHello();
   ```

2. 命名导出：使用 `export` 导出多个对象或函数，并为其命名。在导入时必须使用相应的名称。

    ```javascript
       // 导出
       export function add(a, b) {
       return a + b;
       }
    
       export function sub(a, b) {
       return a - b;
       }
    
       // 导入
       import { add, sub } from './module/nameDefined.js';
    ```

3. 混合导出：将默认导出和命名导出混合使用

    ```javascript
       // 导出
       export function multiply(a, b) {
       return a * b;
       }
    
       export function divided(a, b) {
       return a / b;
       }
    
       export default function funny() {
       return "this is funny!"
       }
    
       // 导入
       import sayHello, { sum } from './module/mixinExport.js';
    ```

需要注意的是，`export` 语句只能出现在模块的顶层作用域，不能用于函数或块级作用域内。另外，ES6 的模块化是默认开启严格模式，所以不支持
CommonJS 的一些语法，比如使用 require() 函数动态导入模块。
