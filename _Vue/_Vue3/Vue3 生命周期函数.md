在 Vue 3 中，除了和 Vue2.x 相同的生命周期函数以外，还新增了一些独有的生命周期函数。

以下是 Vue 3 独有的生命周期函数示例：

1. `setup`：组件实例创建时，该函数会被调用，并返回一个对象。这个对象中包含了组件的响应式数据、方法和计算属性。
它替代了 Vue2.x 中的 beforeCreate 和 created 生命周期，并提供了更加灵活的使用方式。

2. `onBeforeMount`：在组件挂载到 DOM 前，该函数会被调用。它和 Vue2.x 中的 beforeMount 生命周期功能相同，但名称有所改变。

3. `onMounted`：在组件被挂载到 DOM 后，该函数会被调用。它和 Vue2.x 中的 mounted 生命周期功能相同，但名称有所改变。

4. `onBeforeUpdate`：在组件更新之前，该函数会被调用。它和 Vue2.x 中的 beforeUpdate 生命周期功能相同，但名称有所改变。

5. `onUpdated`：在组件更新之后，该函数会被调用。它和 Vue2.x 中的 updated 生命周期功能相同，但名称有所改变。

6. `onBeforeUnmount`：在组件被卸载之前，该函数会被调用。它和 Vue2.x 中的 beforeUnmount 生命周期功能相同，但名称有所改变。

7. `onUnmounted`：在组件被卸载之后，该函数会被调用。它和 Vue2.x 中的 unmounted 生命周期功能相同，但名称有所改变。


以下是 Vue 3 中特殊的钩子函数：

1. `onErrorCaptured`：在组件内部的捕获错误处理函数中执行，可以用来捕获子组件的错误，并进行处理。

2. `onRenderTracked` 和 `onRenderTriggered`：在追踪响应式数据变化时，可以用来获取响应式数据改变的时间点和依赖项的变化情况。

需要注意的是，Vue 3 中新增的生命周期函数名称均以 on 开头，和 Vue2.x 中的生命周期函数名称相比略有不同。
同时，Vue 3 中的 setup 函数也提供了和 Vue2.x 中 beforeCreate 和 created 生命周期相似的功能，但使用方式更加灵活。