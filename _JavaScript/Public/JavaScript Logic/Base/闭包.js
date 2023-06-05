function outerFunction() {
    let outerVariable = "Hello";

    function innerFunction() {
        let innerVariable = "World";
        console.log(outerVariable + " " + innerVariable);
    }

    return innerFunction;
}

let closure = outerFunction();
closure(); // 输出 "Hello World"
closure = null;

function fn1() {
    let a = 1;
    let b = 2;

    function fn2() {
        a++;
        console.log(">>>", a, b);
    }

    return fn2;
}

let f = fn1();
f(); // 2
f(); // 3
f = null; // 解决内存泄漏
