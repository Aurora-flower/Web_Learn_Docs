/** 深拷贝:
 * 这个函数接受一个对象作为参数，返回这个对象的深度拷贝。
 * 该实现仅考虑了对象和数组两种情况，并且只考虑了对象的可枚举属性。
 * 对于其他类型（如 Date、RegExp 等），可能需要进行特殊处理。
 * 此外，如果遇到循环引用的情况，该实现也会陷入死循环。
 * */
function deepClone(obj) {
    let clone = Array.isArray(obj) ? [] : {};

    if (obj && typeof obj === 'object') {
        for (let key in obj) {
            if (obj.hasOwnProperty(key)) {
                if (obj[key] && typeof obj[key] === 'object') {
                    clone[key] = deepClone(obj[key]);
                } else {
                    clone[key] = obj[key];
                }
            }
        }
    }

    return clone;
}


function deepClone_one(obj) {
    // 判断 obj 是否为数组或对象
    if (typeof obj !== 'object' || obj === null) {
        return obj;
    }

    // 判断 obj 的类型是数组还是对象
    const target = Array.isArray(obj) ? [] : {};

    // 遍历 obj 的属性并递归调用 deepClone，将结果赋值给 target 对应的属性
    for (const key in obj) {
        if (Object.prototype.hasOwnProperty.call(obj, key)) {
            target[key] = deepClone(obj[key]);
        }
    }

    return target;
}


// Tip: 使用递归来实现深拷贝可能会导致性能问题，尤其是在处理大型嵌套对象时。