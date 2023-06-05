// region >>> 依赖
import {fileURLToPath, URL} from 'node:url'

// vite 相关
import {defineConfig} from 'vite';
import vue from '@vitejs/plugin-vue';


// endregion

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        vue(),
    ],
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src', import.meta.url))
        }
    }
})


// vite.config.ts
