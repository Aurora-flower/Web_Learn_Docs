# JavaScript


## 循环体中不同声明变量的区别

在循环中使用 `var` 声明的变量与使用 `let` 声明的变量有着不同的作用域及特点。


使用 `var` 声明的变量在循环中会产生变量提升，即在循环外部也能访问到该变量。
同时，由于 JavaScript 存在函数作用域，
因此在循环内部同样可以访问到在循环外部声明的 `var` 变量。

例如：

```javascript
for (var i = 0; i < 3; i++) {
  setTimeout(function() {
    console.log(i); // 输出 3 3 3
  }, 100);
}
```

上面的代码使用 `var` 声明了变量 `i`，在循环内部使用 `setTimeout` 定时器输出变量 `i` 的值。
但是由于变量提升的原因，实际上输出的结果是 3 3 3，而不是期望的 0 1 2。

相比之下，使用 `let` 声明的变量不存在变量提升，且在循环内部创建了块级作用域。
因此，使用 `let` 声明的变量只能在循环内部访问，而循环外部无法访问。

例如：

```javascript
for (let i = 0; i < 3; i++) {
  setTimeout(function() {
    console.log(i); // 输出 0 1 2
  }, 100);
}
```

上面的代码使用 `let` 声明了变量 `i`，在循环内部使用 `setTimeout` 定时器输出变量 `i` 的值。
由于使用 `let` 声明的变量不存在变量提升，因此输出的结果是 0 1 2。

综上所述，使用 `let` 声明的变量相比于使用 `var` 声明的变量更加安全、可读性更好，
同时也避免了一些潜在的错误。因此，在实际开发中应尽可能使用 `let` 声明变量。

---

## 表现不同的情况

在循环体中，使用 `var` 声明的变量与使用 `let` 声明的变量会在以下情况下展现出明显的区别：

1. 在嵌套作用域中的表现不同

使用 `var` 声明的变量在循环体内创建了函数作用域，而使用 `let` 声明的变量创建块级作用域，因此在嵌套作用域中的表现不同。

例如：

```javascript
for (var i = 0; i < 3; i++) {
  var count = i;
  setTimeout(function() {
    console.log(count); // 输出 2 2 2
  }, 100);
}

for (let i = 0; i < 3; i++) {
  let count = i;
  setTimeout(function() {
    console.log(count); // 输出 0 1 2
  }, 100);
}
```

上面的代码分别使用 `var` 和 `let` 声明了变量 `count`，
并在循环体内使用 `setTimeout` 创建了闭包。
使用 `var` 声明的变量 `count` 在循环体内创建了函数作用域，
因此在循环内部创建的闭包都可以访问到同一个变量 `count`。
相比之下，使用 `let` 声明的变量 `count` 创建了块级作用域，
因此每次循环都会创建一个新的变量 `count`，
闭包也只能访问到当前循环中的变量 `count`。

2. 在 for-in 循环中的表现不同

在 for-in 循环中，使用 `var` 声明的变量会泄露到循环外部，而使用 `let` 声明的变量则不会出现这种情况。

例如：

```javascript
var obj = { a: 1, b: 2, c: 3 };
for (var prop in obj) {
  console.log(prop); // 输出 a b c
}
console.log(prop); // 输出 c

let obj = { a: 1, b: 2, c: 3 };
for (let prop in obj) {
  console.log(prop); // 输出 a b c
}
console.log(prop); // 报错 ReferenceError
```

上面的代码分别使用 `var` 和 `let` 声明了变量 `prop`，
并在 for-in 循环中遍历对象的属性。在使用 `var` 声明的变量 `prop` 时，
最后一次循环执行完毕后，该变量会泄露到循环外部，
因此在循环外部也可以访问到该变量。
相比之下，使用 `let` 声明的变量 `prop` 创建了块级作用域，
因此在循环外部无法访问到该变量，输出时会报错。

综上所述，在嵌套作用域和 for-in 循环等场景中，使用 `var` 和 `let` 声明变量的区别会比较明显。
在实际开发中，应根据具体场景和需求选择合适的声明方式以确保代码的正确性和可维护性。