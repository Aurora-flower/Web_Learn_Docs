# Vue

## 脚手架环境搭建

### 全局安装 Vue CLI
```bash
npm install -g @vue/cli
```

### 全局安装 vite 命名
```bash
npm install -g vite
```

### vue2

```bash

# 方式一: Vue CLI 2.x 版本命令 - Vue CLI 3.x 中被移除
# <template-name>：必填，表示你要使用哪个模板来创建项目。
# <project-name>：必填，表示你要为项目取什么名字。
vue init <template-name> <project-name>

# 方式二: 在 Vue UI 界面中创建项目
vue ui
```

### vue3

```bash
# 方式一: 该命令用于初始化一个基于 Vite 构建工具的 Vue 项目。
npm init vite@latest <project-name> --template vue

# 方式二: Vue CLI 3.x 版本命令
vue create <project-name>
```

_Tip：执行 create-vue - 项目脚手架工具_