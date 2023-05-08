// 斐波那契数列 - 递归方法
function fibonacci(n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

let result = fibonacci(20);
console.log(result)


// 迭代方法
function fibonacci_one(n) {
    let a = 0,
        b = 1,
        next;
    for (let i = 0; i < n; i++) {
        next = a + b;
        a = b;
        b = next;
    }
    return a;
}

let result_one = fibonacci_one(20);
console.log(result_one)
