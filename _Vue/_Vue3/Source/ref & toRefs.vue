<template>
  <div class="container">
    <div> name: {{ refs.name }}</div>
    <div> count: {{ refs.count }}</div>
    <button ref="btn" @click="changeState">Click me</button>
  </div>
</template>

<script setup>
import {ref, reactive, toRefs, onMounted} from 'vue';

// 用来获取元素
const btn = ref(null);
console.log(btn.value); // undefined

/// 在组件实例创建之后，btn 将指向 div 元素的 DOM 引用
/**
 * 获取页面中的元素， ref 标识元素。
 * 在 setup 中，定义一个 ref 对象，以一个变量接收并返回此变量，
 * 作为 元素的 ref 名称。（focus 聚焦 ）
 * */
onMounted(() => {
  console.log(btn.value);
  console.log(btn.value.focus());
})

const state = reactive({
  count: 0,
  name: 'HuaYin'
});


/**
 * @author 花楹一间
 * @description toRefs() 接收一个响应式对象（通常是由 reactive() 创建的响应式数据），
 * 并将其转换成一个由多个独立的响应式引用对象组成的对象。
 * @note 在 Vue 3 中，ref() 和 toRefs() 都是用来创建响应式数据的 API。
 * ref() 接收一个参数，并返回一个包含该参数的响应式引用对象。
 * toRefs() 只会将对象中的属性转换成独立的响应式引用对象，而不会将整个对象转换成响应式引用对象。
 * 因此，如果你需要使用整个对象作为响应式数据，并且同时保证对象中的属性也能够被独立地使用或传递，
 * 可以先使用 reactive() 创建响应式对象，然后再使用 toRefs() 将其转换成引用对象。
 * */

// Tip: 可以转普通对象，但失去响应式。
const refs = toRefs(state);
console.log(refs); // 返回一个普通对象，属性值具有响应式。

const changeState = () => {
  refs.count.value++;
}

console.log(refs.count.value); // 0
console.log(refs.name.value); // 'HuaYin'

</script>

<style lang="less" scoped>

</style>