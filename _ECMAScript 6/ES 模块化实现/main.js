// 在 ES6 中，我们可以使用 export 和 import 语句来进行模块化编程。

// export default  的导入
import sayHello from './module/defaultExport.js';

sayHello();

// export defined 的导入
import {add, sub} from "./module/nameDefined.js";

console.log(add(1, 2));
console.log(sub(4, 3));


// 混合导入
import funny from "./module/mixinExport.js";

console.log(funny());

import {multiply, divided} from "./module/mixinExport.js";

console.log(multiply(1, 2));
console.log(divided(4, 2));
