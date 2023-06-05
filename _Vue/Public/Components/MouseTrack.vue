<template>
	<div class="mouse_track">
		Mouse position is at: {{ x }}, {{ y }}
	</div>
</template>

<script>
export default {
    name: "MouseTrack"
}
</script>

<script setup>

// 普通写法
import {ref, onMounted, onUnmounted} from 'vue'

// 鼠标坐标变量
const x = ref(0)
const y = ref(0)

function update(event) {
    x.value = event.pageX
    y.value = event.pageY
}

onMounted(() => window.addEventListener('mousemove', update))
onUnmounted(() => window.removeEventListener('mousemove', update))

// 组合式函数写法
// import {useMouse} from "./mose-track";
// const {x, y} = useMouse();

</script>


<style scoped>

</style>