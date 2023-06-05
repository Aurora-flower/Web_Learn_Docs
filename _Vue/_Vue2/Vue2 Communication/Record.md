# 组件间的通信方式

## 1. _props_ 
    
    props 主要用于 `父子组件` 间的一种通信机制。


### 基本通信步骤

(1) 在父组件中引入子组件

```html
  <div class="box">
	<h2> Father </h2>
	<hr>
	<!-- 此时，传递的是属性，尚未绑定父组件的数据 -->
	<h3>>>> 传递普通属性</h3>
	<Child message="message"></Child>
	<hr>

	<!-- v-bind 绑定基本数据类型 -->
	<h3>>>> v-bind 传递基本数据类型</h3>
	<Child :value="value"></Child>
	<hr>

	<!-- v-bind 绑定引用数据类型 -->
	<h3>>>> v-bind 传递引用数据类型</h3>
	<Child :obj="obj"></Child>
	<hr>

	<!---------------------------------------------------->
	<!--第一种情况:  普通属性 + v-bind 单向数据流 -->
	<Child message="message" :value="value" :obj="obj"></Child>
</div>
```



```js
export default {
// eslint-disable-next-line vue/multi-word-component-names
    name: "PropsTest",
    data(){
        return {
        // 基本数据类型
            value: 1,
        // 引用数据类型
            obj: {
                name: "HuaYin",
                age: 22,
    },

    }
    },
    components: {
        Child,
}
}
```


***关于 data 的写法***:

    Tip: 
        vue 中组件是用来复用的，为了防止 data 复用，将其定义为函数。
        vue 组件中的 data 数据都应该是相互隔离，互不影响的，组件每复用一次，data 数据就应该被复制一次.
        之后，当某一处复用的地方组件内 data 数据被改变时，其他复用地方组件的 data 数据不受影响，
    就需要通过 data 函数返回一个对象作为组件的状态。
        类似于给每个组件实例创建一个私有的数据空间，让各个组件实例维护各自的数据。

(2) 在子组件中通过 props 接收参数（三种方式）

```js
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "Child",
    // 1. 字符串数组形式接收 props 参数
    // props: ["message", "value", "obj"], // ["props 属性名" ]

    // 2. 对象形式接收 props 参数
    // props: {
    //   // 属性名: 数据类型
    //   message: String,
    //   value: Number,
    //   obj: Object,
    // },

    // 3. 对象配置形式接收 props 参数
    props: {
        message: {
            type: String, // 数据类型
            required: true, // 是否必填
        },
        value: {
            type: Number, // 数据类型
            default: 10, // 默认值 - 基本数据类型
        },
        obj: {
            type: Object,
            /*
            Tip: 引用数据类型的默认值， Object/Array 类型不能直接定义空对象或空数组，
            必须使用工厂函数 return 回一个默认值。
            */
            default: () => ({}),  // 默认值 - 引用数据类型
        },
    }
}
```

---

### 对 props 数据的修改

(1) 创建 methods 方法，修改 props 属性值

```js
  methods:{
    // [测试] 在子组件上尝试直接修改 props 属性
    changeProps(){
      this.$props.message = "hello world.";
    }
  }
```

`Tip`: ___避免直接更改属性，因为每当父组件重新渲染时，该值将被覆盖。___

(2) 修改来自父组件的 data 数据

    子组件中是无法直接修改父组件中的数据的，可以通过在父组件上定义可以修改数据的方法；
    传参类型: 非函数数据类型 && 函数数据类型。
    
非函数类型: （展示）

    a. 基本数据类型 - 字符串
    b. 引用数据类型 - 无法修改（对象）地址，但可以修改属性;

函数类型:   （为使子组件可以调用函数修改父组件的数据）


**事件的绑定**:
```js
    // 全写形式 v-on:事件类型="方法" <=> 简写形式 @事件类型="事件方法"
    <button v-on:click="change">Change</button>
    <button @click="change">Change</button>
```

**父组件传递 props** 
```html
  <div>
    <h2> Father </h2>
    <div>----------------------------------</div>
    <!-- 传递 基本数据类型，引用数据类型， 函数类型 -->
    <Child :message="message"  :obj= "obj" :changeMsg="changeMsg"></Child>
  </div>
```

```js
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Father",
  data(){
    return {
        message: "this is message.",
        obj: {
          name: "HuaYin",
            age: 22,
        },
    }
  },
  methods: {
    changeMsg(text){
      this.message = text;
    },
  },
  components: {
    Child,
  }
}
```

**子组件修改 props 数据**

```html
  <div>
    <h2>Child</h2>
    <p> message: {{ message }}</p>
    <p> object: {{obj.name}} - {{obj.age}}</p>
    <button @click="change"> Change </button>
    <button @click="changeObj"> changeObj </button>
  </div>
```

```js
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Child",
  props: {
      message: {
          type: String,
          require: false,
      },
      obj: {
          type: Object,
          // 引用数据类型的默认值，用函数返回值的形式;
          default: ()=> ({}) , 
      }
  },
  methods: {
      change(){
          let text = "this is a text.";
          this.changeMsg(text);
      },
      changeObj(){
          // this.$props.obj = {name: "huayin"};
          this.$props.obj.age = 23;
      },
  },
}
```

`Tip`: ___不建议直接修改属性，违反了数据流单向传递的规则。___


---


## 3. _ v-model 数据绑定_

**传递的数据**:
```js
  data(){
    return {
      value: "Hello World.",
    }
  }
```

(1) 单向数据绑定 v-bind

    数据只能从 data 流向页面。

**两种写法**:
```js
    // 全写形式: v-bind: 属性名 = " data 数据变量 "
    <input type="text" v-bind:value="value">
```

```js
    // 简写形式 v-bind  <=> :
    <input type="text" :value="value">
```

`Tip`: ___以 input 表单元素为例，v-bind 仅仅是把数据绑定在元素中，当修改文本框的内容时， data 数据不会改变。___


(2) 双向数据绑定 v-model

    常用于 表单元素 的双向数据的绑定。

```js
    // 全写形式 v-model:value="" <=> 简写形式 v-model=""
    <input type="text" v-model="value">
    <input type="text" v-model:value="value">
```

`Tip`: ___当修改文本框的内容时， data 数据会发生改变。___


## 2. _自定义事件_

    主要是通过自定义一种事件，触发 methods 方法，达到修改数据。


(1) 标签绑定事件 

a. 原生事件

b. 自定义事件

c. 关于参数


## 3. _事件总线（缺点）_


使用 Vue 的事件总线模式虽然可以方便实现组件之间的通信，但也存在一些缺点。其中比较明显的缺点有以下几个：

1. 耦合度高：事件总线模式需要创建一个全局的事件总线对象，所有组件都要绑定事件和触发事件，这样会导致组件之间的耦合度相对较高，一旦事件总线对象发生变化，所有相关组件都需要进行修改。

2. 调试困难：由于事件总线模式是基于全局事件来实现的，如果出现问题，调试起来比较困难。因为在调试过程中通常只能看到事件的发布和订阅行为，无法直接看到事件传递的具体值，也无法跟踪事件的调用栈。

3. 容易出现命名冲突：由于事件总线模式是基于字符串类型的事件名称来进行事件绑定和触发的，所以容易出现组件之间事件名称冲突的情况，这可能会导致难以预料的错误。






































