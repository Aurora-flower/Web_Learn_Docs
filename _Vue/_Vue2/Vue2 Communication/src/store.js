import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

// 数据
const state ={
    one: 1,
    two: 2,
};

// 修改数据 （同步）
const mutations ={};

// 提交修改请求，调用 mutations （可以是异步操作）
const actions ={};

// 计算属性并 return 值
const getters ={};


export default new Vuex.Store({
    state,
    mutations,
    actions,
    getters,
})