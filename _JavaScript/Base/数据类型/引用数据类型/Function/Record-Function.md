# Function 


## new Function

`new Function()` 是 JavaScript 提供的一个构造函数，用于创建一个新的函数对象。它的

语法如下：

```
new Function([arg1, arg2, ..., argn], funcBody)
```

其中 `arg1, arg2, ..., argn` 是新函数的形参名，`funcBody` 是新函数的函数体，可以是一段字符串。当我们使用 `new Function()` 创建一个新函数时，JavaScript 引擎会将 `funcBody` 的内容解析为函数体，并在当前作用域中创建一个新的函数对象。

`new Function()` 的作用有以下几个方面：

1. 动态生成函数：

    由于它接受字符串作为函数体，因此可以动态地创建函数。
    这在实际开发中比较有用，例如根据用户输入的代码动态生成并执行相应的函数等。

2. 支持动态变量名：

    在函数体中使用 `eval()` 可以动态创建变量，但是变量名必须是在运行时确定的。
    而使用 `new Function()` 则可以动态生成变量名，从而更加灵活。

3. 父子作用域分离：

    在使用 `new Function()` 创建函数时，该函数将在全局作用域中创建，而不是当前作用域中。
    因此，可以通过在函数体中引用全局变量来保证父子作用域的正确分离。

需要注意的是，使用 `new Function()` 创建函数可能会带来一些潜在的安全隐患，
因为它允许在运行时动态创建代码并执行。
在实际使用中，应该谨慎使用，并避免使用不可信地输入来动态生成函数。


## arguments.callee()

`arguments.callee`是一个指向当前正在执行的函数的指针，它可以用来实现递归等一些高级的应用场景。

在函数内部，使用`arguments.callee`可以调用函数本身。例如：

```javascript
function factorial(n) {
  if (n === 1) {
    return 1;
  } else {
    return n * arguments.callee(n - 1);
  }
}
```

上面的代码定义了一个`factorial`函数，用来计算一个正整数的阶乘。函数内部使用`arguments.callee`来递归地调用自己，实现计算阶乘的功能。

需要注意的是，由于严格模式下不允许使用`arguments.callee`，
因此在严格模式下，使用`arguments.callee`会导致错误。
此时，可以使用函数名来替代`arguments.callee`。例如：

```javascript
"use strict";
function factorial(n) {
  if (n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
```

上面的代码是在严格模式下定义的阶乘函数，使用函数名来递归调用自己，
避免了使用`arguments.callee`引发的错误。