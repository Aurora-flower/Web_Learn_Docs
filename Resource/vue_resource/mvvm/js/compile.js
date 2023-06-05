// Compile 编译构造函数 - 接收 el 配置或 body & MVVM 实例
function Compile(el, vm) {
    // this - Compile 编译实例对象 - 添加 $vm 属性 - 存储 MVVM 实例
    this.$vm = vm;

    // 模板容器
    // 判断是否为元素节点(1) - 不是则通过 querySelector 选择器获取元素 - 存储元素
    this.$el = this.isElementNode(el) ? el : document.querySelector(el);

    // 判断模板容器是否存在
    if (this.$el) {
        // 添加 $fragment 属性 - 存储文档碎片对象 - 传入元素节点
        this.$fragment = this.node2Fragment(this.$el);

        this.init();

        // 将文档碎片对象插入到 DOM 树中
        this.$el.appendChild(this.$fragment);
    }
}

// Compile 编译构造函数的原型对象
Compile.prototype = {
    constructor: Compile, // 重写构造器
    node2Fragment: function (el) {
        // 创建文档碎片对象
        // 文档碎片对象是一个没有父节点的轻量级文档对象，用于在内存中存储一些 DOM 元素,可以减少修改DOM次数，提高性能。
        var fragment = document.createDocumentFragment(),
            child;

        // 将原生节点拷贝到 fragment - 当不存在子节点时,结束循环
        while (child = el.firstChild) {
            fragment.appendChild(child); // 向文档碎片对象中添加节点
        }

        return fragment; // 返回文档碎片对象
    },

    // 模版解析的方法（入口）
    init: function () {
        // this - Compile 实例（调用者）
        // 调用 compileElement（编译元素）方法，传入文档碎片对象
        this.compileElement(this.$fragment);
    },

    // 模版解析的方法（实际）
    compileElement: function (el) {
        // 模板容器的子节点 - 伪数组
        var childNodes = el.childNodes,
            me = this; // this - Compile 实例（调用者）

        // 遍历容器中的子节点
        // 伪数组转为真数组 [..., Array.prototype.slice.call, [].slice.call, Array.from]
        [].slice.call(childNodes).forEach(function (node) {
            // 节点的文本内容 [textContent\innerHTML\innerText]
            var text = node.textContent;

            // 插值语法的正则表达式 - (.*) 表示匹配任意字符任意次数（包括 0 次），并将匹配的连续字符作为一个分组返回。
            var reg = /\{\{(.*)\}\}/;

            // 判断是否为元素节点
            if (me.isElementNode(node)) {
                // 对元素节点进行解析
                me.compile(node);

            // 同时判断是否为文本节点，并对节点的文本内容进行正则校验
            } else if (me.isTextNode(node) && reg.test(text)) {
                // 对文本节点进行解析 - 传入当前节点以及正则捕捉的内容
                me.compileText(node, RegExp.$1.trim()); // 插值表达式内容 - $1 表示第一组, trim() 字符串两端空格
            }

            // 判断当前元素节点是否存在子节点 & 子节点数组的长度
            if (node.childNodes && node.childNodes.length) {
                // 深度递归模板解析
                me.compileElement(node);
            }
        });
    },

    // 解析元素节点
    compile: function (node) {
        // 元素节点的属性 - 以 key-value 形式存储
        var nodeAttrs = node.attributes,
            me = this; // this - Compile 实例（调用者）

        // 遍历元素的属性 - 主要判断是否为特殊属性
        [].slice.call(nodeAttrs).forEach(function (attr) {
            var attrName = attr.name; // attrName - 存储属性名

            // 判断是否为指令
            if (me.isDirective(attrName)) {
                var exp = attr.value; // exp - 存储属性值

                // substring() 用于从字符串中提取子字符串并返回。
                // 该方法有两个参数，分别是 indexStart 和 indexEnd，表示待提取子串的起始位置和结束位置（不包含结束位置处的字符），默认值为 0 和字符串的长度。
                var dir = attrName.substring(2); // 主要针对 v- 开头的指令属性

                // 事件指令
                if (me.isEventDirective(dir)) {
                    // 解析事件指令 - 传入当前元素节点 & MVVM 实例对象 & 属性值 & 指令部分
                    compileUtil.eventHandler(node, me.$vm, exp, dir);

                } else { // 普通指令
                    // 判断是否存在该指令 - 存在则执行 - 传入当前元素节点 & MVVM 实例对象 & 属性值
                    compileUtil[dir] && compileUtil[dir](node, me.$vm, exp);
                }

                node.removeAttribute(attrName); // 从当前元素节点上移除该指令属性
            }
        });
    },

    // 解析文本节点
    compileText: function (node, exp) {
        // this - Compile 实例（调用者）, exp - 插值内容
        compileUtil.text(node, this.$vm, exp);
    },

    // 判断是否为指令
    isDirective: function (attr) {
        // indexOf() 方法用于在一个字符串中查找指定的子字符串，并返回该子字符串第一次出现的位置。如果没有找到匹配的字符串，则返回 -1。
        return attr.indexOf('v-') === 0;
    },

    // 判断是否为事件指令
    isEventDirective: function (dir) {
        return dir.indexOf('on') === 0;
    },

    // 判断是否为元素节点 - nodeType === 1
    isElementNode: function (node) {
        return node.nodeType === 1;
    },

    // 判断是否为文本节点 - nodeType === 3 [空格为文本节点]
    isTextNode: function (node) {
        return node.nodeType === 3;
    }
};

// 指令处理集合
var compileUtil = {
    // 插值语法 - v-text
    text: function (node, vm, exp) {
        this.bind(node, vm, exp, 'text');
    },

    html: function (node, vm, exp) {
        this.bind(node, vm, exp, 'html');
    },

    model: function (node, vm, exp) {
        this.bind(node, vm, exp, 'model');

        var me = this,
            val = this._getVMVal(vm, exp);
        node.addEventListener('input', function (e) {
            var newValue = e.target.value;
            if (val === newValue) {
                return;
            }

            me._setVMVal(vm, exp, newValue);
            val = newValue;
        });
    },

    class: function (node, vm, exp) {
        this.bind(node, vm, exp, 'class');
    },

    // 建立 Dep 与 Watcher 的关系
    bind: function (node, vm, exp, dir) {
        // 更新程序函数 -  updater 对象下的 [指令 + "Updater"]
        var updaterFn = updater[dir + 'Updater'];

        // 判断函数是否存在 - 存在则执行 - 传入当前节点 & _getVMVal 函数
        updaterFn && updaterFn(node, this._getVMVal(vm, exp));

        // 模版中一个表达式对应一个 watcher 实例对象
        new Watcher(vm, exp, function (value, oldValue) {
            updaterFn && updaterFn(node, value, oldValue);
        });
    },

    // 事件处理
    eventHandler: function (node, vm, exp, dir) {
        var eventType = dir.split(':')[1],
            fn = vm.$options.methods && vm.$options.methods[exp];

        if (eventType && fn) {
            node.addEventListener(eventType, fn.bind(vm), false);
        }
    },

    // 根据 vm 获取 MVVM 的值 - 接收 MVVM 实例 & 插值表达式文本内容
    _getVMVal: function (vm, exp) {
        var val = vm; // 存储 MVVM 实例
        exp = exp.split('.');  // 对插值表达式文本内容进行切割
        exp.forEach(function (k) {
            val = val[k];
        });
        return val; // 此时 val 存储的是获取到的表达式的值
    },

    _setVMVal: function (vm, exp, value) {
        var val = vm;
        exp = exp.split('.');
        exp.forEach(function (k, i) {
            // 非最后一个key，更新val的值
            if (i < exp.length - 1) {
                val = val[k];
            } else {
                val[k] = value;
            }
        });
    }
};


var updater = {
    textUpdater: function (node, value) {
        node.textContent = typeof value == 'undefined' ? '' : value;
    },

    htmlUpdater: function (node, value) {
        node.innerHTML = typeof value == 'undefined' ? '' : value;
    },

    classUpdater: function (node, value, oldValue) {
        var className = node.className;
        className = className.replace(oldValue, '').replace(/\s$/, '');

        var space = className && String(value) ? ' ' : '';

        node.className = className + space + value;
    },

    modelUpdater: function (node, value, oldValue) {
        node.value = typeof value == 'undefined' ? '' : value;
    }
};