<template>
	<div class="box">
		<h1>组件间通信: Pinia</h1>
		<div>Count: {{ TestStore.count }}</div>
		<button class="ml-10" @click="addHandle">增加</button>
		<button class="ml-10" @click="subHandle">减少</button>
	</div>
</template>

<script lang="ts">
export default {
    name: "PiniaTest"
}
</script>

<script setup lang="ts">
import {pinia} from "@/main";
import {useTestStore} from "@/pages/09_pinia/index";
import {watch} from "vue";

// PINIA
const TestStore = useTestStore(pinia);
console.log(">>> TestStore:", TestStore);


// 定义函数
const addHandle = () => {
    TestStore.Increase();
};
const subHandle = () => {
    TestStore.Decrease();
};

// watch
</script>

<style scoped>
.ml-10 {
	margin-left: 10px;
}
</style>