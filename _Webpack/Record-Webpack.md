# webpack 的安装

1. 安装 Node.js

    因为 webpack 是一个 Node.js 模块，所以首先需要安装 Node.js。 

2. 创建项目

    在本地创建一个新的项目文件夹，并进入该文件夹，例如：

```
mkdir my-project
cd my-project
```

3. 初始化项目

    在项目文件夹中使用以下命令初始化项目：

```
npm init -y
```

_Tip: 会在项目文件夹中生成一个 package.json 文件，用于管理项目依赖。_

4. 安装 webpack

    在项目文件夹中使用以下命令安装 webpack：

```
npm install webpack webpack-cli --save-dev
```

_Tip: --save-dev 参数表示将 webpack 和 webpack-cli 作为开发依赖保存到 package.json 文件中。_

5. 编写代码

    在项目文件夹中创建 src 目录，并在该目录中编写 JavaScript 代码。可以创建一个 index.js 文件，并输出一些内容，例如：

```javascript
console.log('Hello, webpack!');
```

6. 编写配置文件

    在项目文件夹中创建一个名为 webpack.config.js 的文件，并在该文件中编写 webpack 配置，例如：

```javascript
const path = require('path');

module.exports = {
  // 入口
  entry: './src/index.js',
  // 出口
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist')
  }
};
```

_Tip: entry 属性指定了入口文件，output 属性指定了输出文件的名称和路径。_

7. 运行打包命令

    在项目文件夹中使用以下命令运行 webpack：

```
npx webpack
```

_Tip: 会自动查找 webpack.config.js 文件，并根据配置进行打包。_

8. 查看结果

    在项目文件夹中会生成一个 dist 目录，其中包含打包后的 bundle.js 文件。在浏览器中打开 index.html 文件，就可以看到打包后的代码运行结果。
