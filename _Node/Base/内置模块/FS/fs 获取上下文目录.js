// 1. 引入 fs 模块
const fs = require('fs');

// 2. 使用 fs.readdir() 方法读取目录结构
/*
Tip: fs.readdir() 方法接受两个参数：
    要读取的目录路径和一个回调函数。
    回调函数的第一个参数是可能出错的错误对象，第二个参数是包含目录中所有文件名称的数组。
*/
fs.readdir(
    process.cwd(), // // 当前工作目录
    (err, files) => {
        if (err) {
            throw err;
        }

        console.log(files);
    }
);

// 3. 使用递归算法遍历子目录
/**
 * Tip: 使用 fs.readdirSync() 方法同步地读取目录结构，
 *  并使用 fs.statSync() 方法判断每一个文件或目录是否是一个目录。
 *  如果是目录，则递归调用 listFiles() 方法，否则打印出文件路径。
 * */
function listFiles(path) {

    fs.readdirSync(path).forEach((file) => {
        const fullPath = path + '/' + file;

        // 判断是否为目录
        if (fs.statSync(fullPath).isDirectory()) {
            console.log(fullPath);
            listFiles(fullPath);
        } else {
            console.log(fullPath);
        }
    });
}

listFiles(process.cwd());

