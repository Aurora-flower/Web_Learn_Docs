Flex（Flexbox）是一种用于网页布局的 CSS 弹性盒子模型，它能够对元素进行弹性的排列和对齐。使用 Flex 可以更加方便地实现各种复杂的布局效果。

在使用 Flex 进行布局时，需要将父元素设置为 flex container（弹性容器），并添加相应的属性：

- `display`: flex;  // 将元素设置为弹性容器
- `flex-direction`: row/column;   // 设置主轴方向
- `justify-content`: flex-start/center/flex-end/space-between/space-around;  // 设置主轴方向上的对齐方式
- `align-items`: stretch/flex-start/center/flex-end/baseline;  // 设置交叉轴方向上的对齐方式
- `flex-wrap`: nowrap/wrap/wrap-reverse;    // 是否允许换行
- `flex-flow`: row wrap;  // 简写方式，设置主轴方向和是否换行

在使用 Flex 进行布局时，每个子元素都可以设置如下属性：

- `flex-grow`: <number>;   // 指定子元素的放大比例，默认为 0
- `flex-shrink`: <number>; // 指定子元素的缩小比例，默认为 1
- `flex-basis`: <length>/%/auto;   // 指定子元素在主轴方向上的基础长度，默认为 auto
- `flex`: <flex-grow> <flex-shrink> <flex-basis>;   // 指定三个属性的组合写法

使用 Flex 进行布局时，可以轻松实现以下效果：

1. 等分布局：将多个元素等分排列于一行或一列中。
2. 左右布局：将一个元素居左，另一个元素居右。
3. 上下布局：将多个元素水平居中，竖直排列。
4. 容器自适应高度：将子元素的高度加和，使父容器自适应高度。

总之，Flex 是一种强大的 CSS 布局方式，它能够使页面布局更加简单、灵活和易于维护。在实际开发中，建议多尝试使用 Flex 进行布局，以提升开发效率和代码质量。