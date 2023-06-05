// mixin 文件的目的是为了复用

/*
Tip:
    将多个组件中具有相同内容的部分提取出来放在 mixin 文件中，进行混入(配置项与 vue 实例相同)；
    当组件内配置项与 mixin 配置项相同时，组件内的配置会覆盖 mixin 中的配置。钩子函数不会覆盖，先执行 mixin ，后执行组件实例的。
*/

export default {
    methods: {
        toDadMoney(num) {
            this.money -= num;
            this.$parent.money += num;
        },
    }
}