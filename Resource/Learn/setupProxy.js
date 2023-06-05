//http 代理 (包在初始化脚手架的自动安装)
const proxy = require('http-proxy-middleware');
//2、导出一个方法
module.exports = function (app) {
    // 配置请求 API 匹配转发
    // Tip: 对两个 Faker API 分别定义为了 OrderService 、ProductService 在 node 中对其的调用将转发到对应的 target 地址
    app.use(
        // 2.x 以上：proxy.createProxyMiddleware(...)
        // 2.x 以下：proxy(...)
        proxy["createProxyMiddleware"]('/api', {
            //请求的目的地址
            target: 'http://127.0.0.1:5000',
            //控制服务器收到的请求头中 Host 的值
            changeOrigin: true,
            /*
            changeOrigin 设置为 true 时，服务器收到的请求头中的 host 为：localhost:5000
            changeOrigin 设置为 false 时，服务器收到的请求头中的 host 为：localhost:3000
            changeOrigin 默认值为 false，但我们一般将 changeOrigin 值设为 true
            */

            //重写路径
            pathRewrite: {
                // Tip: 去除请求前缀，保证交给后台服务器的是正常请求地址(必须配置)
                '^/api': ''
            }
        }),
        /* proxy.createProxyMiddleware('/api1', {
            //请求的目的地址
            target: 'http://127.0.0.1:7000',
            //控制服务器收到的请求头中Host的值
            changeOrigin: true,
            //重写路径
            pathRewrite: {
                '^/api1': ''
            }
        }), */
        /* proxy.createProxyMiddleware('/api2', {
            //请求的目的地址
            target: 'http://127.0.0.1:9000',
            //控制服务器收到的请求头中Host的值
            changeOrigin: true,
            //重写路径
            pathRewrite: {
                '^/api2': ''
            }
        }) */
    )
}