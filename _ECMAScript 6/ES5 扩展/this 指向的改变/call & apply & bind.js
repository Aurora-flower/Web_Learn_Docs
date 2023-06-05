// region >>> call & apply & bind (pending)

function fun(name, age) {
    console.log(this, name, age);	// window
}

let obj = {
    name: "HuaYin"
};

// 1.call
// 参数：（this 指向，参数...）
fun.call(obj, "hua", 18);	// this 指向: object
fun.call(null, "null", 19);		// this 指向: window || global
fun.call(undefined, "undefined", 20);	// this 指向: window  || global

// 2.apply
// 参数：（this 指向，[数组-参数...]）
fun.apply(obj, ["hua", 21]);  // this 指向: object
fun.apply(null, ["null", 22]); // this 指向: window || global
fun.apply(undefined, ["null", 22]); // this 指向: window || global

// Tip: call 与 apply



// endregion
