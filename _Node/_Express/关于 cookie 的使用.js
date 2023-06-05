// region >>> cookie
// 引入 express, 并创建服务
const express = require("express");
const app = express();

// 导入
const cookieParser = require("cookie-parser")
app.use(cookieParser());

app.get("/", (req, res) => {
    // 设置 cookie(方式一)
    // Tip: 本地浏览器存储 cookie
    // res.cookie("home", "keys", {
    //     maxAge: 60 * 1000, // ms
    // });

    // 设置 cookie(方式二)
    // Tip: 表示只要向服务器发送请求，就会携带 cookie 传递给服务器;
    res.setHeader("Set-Cookie", "username=admin;Path=/");

    console.log(req, res);
    res.end("Home");
});

app.get("/clean", (req, res) => {
    // 清除 cookie
    res.clearCookie("username", {
        maxAge: 60 * 20
    });
    res.end("clean")
})

app.listen(8000, () => {
    console.log(">>> 8000 端口已启动");
});
// endregion