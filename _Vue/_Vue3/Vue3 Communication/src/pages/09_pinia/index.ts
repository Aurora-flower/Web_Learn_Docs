import {defineStore} from "pinia";
import {ref} from "vue";


// 可以使用一个函数（类似于一个组件setup()）来为更高级的用例定义一个Store：
export const useTestStore = defineStore("test", {
    state: (): { count: number } => ({
        count: 0
    }),
    actions: {
        // Increase, decrease
        Increase() {
            this.count++;
            console.log(">>> Increase:", this.count);
        },
        Decrease() {
            this.count--;
            console.log(">>> Decrease:", this.count);
        }
    }
})