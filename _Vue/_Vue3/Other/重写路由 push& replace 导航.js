import Vue from 'vue'
import VueRouter from 'vue-router'

// 对 vue-router 的原型进行操作，保存原型的 push 与 replace
const originalPush = VueRouter.prototype.push
const originalReplace = VueRouter.prototype.replace

// 重写 push 方法
VueRouter.prototype.push = function push(location) {
    // 返回保存的 push 方法，传递 location 参数
    return originalPush.call(this, location).catch(err => {
        // error - NavigationDuplicated - 导航重复问题
        if (err.name !== 'NavigationDuplicated') {
            throw err
        }
    })
}

// 重写 replace 方法
VueRouter.prototype.replace = function replace(location) {
    // 返回保存的 replace 方法，传递 location 参数
    return originalReplace.call(this, location).catch(err => {
        if (err.name !== 'NavigationDuplicated') {
            throw err
        }
    })
}

Vue.use(VueRouter)

// 创建路由实例并导出
export default new VueRouter({})
