# BOM


## 重排与重绘


### 1. 两者的区别:


    重排(reflow)和重绘(repaint)都是浏览器渲染页面时的关键环节，
    它们分别对应了浏览器中两个重要的操作：布局（layout）和绘制（paint）。

(1) 重排是指当 DOM 结构中的元素发生变化（如，大小或位置的变化）时，
浏览器需要重新计算并确定页面中每个元素的准确位置和大小，然后重新渲染更新后的页面。
由于这个过程牵扯到多个元素的重新布局及其计算，
因此会消耗大量的计算资源和时间，使页面的性能受到明显影响。

**Tip: 重排会引发重绘。**

(2) 重绘则是指当元素的外观（如，颜色或背景的变化）发生变化时，
浏览器只需将更新后的元素的样式重新绘制在内存中，而无需重新计算元素的大小和位置。
基于现代浏览器使用的分层渲染机制，**重绘的开销通常比重排小得多。**
然而，频繁的重绘仍然会影响页面性能，甚至可能导致页面的视觉闪烁。

_所以，重排和重绘都会对页面性能产生负面影响，因此在实际开发中，我们应该尽可能减少 DOM 操作、避免频繁修改样式，以减少页面的重排和重绘次数，从而提高页面的性能。_

### 2. 内存开销对比

    在浏览器渲染页面时，重排和重绘都会对内存产生开销。

1. 重排的内存开销通常比重绘大，因为重排涉及到重新计算和更新多个元素的几何属性（如大小、位置、布局等），需要重新构建布局树和绘制树。每次发生重排时，都会导致浏览器重新计算并确定所有元素的位置和大小，这些计算结果被临时存储在内存中，直到渲染引擎完成页面的渲染和绘制。

2. 重绘的内存开销相对较小，因为它只涉及到重绘元素的样式和外观，而不需要重新计算元素的位置和大小。每次发生重绘时，渲染引擎会将已经计算好的布局树和绘制树直接绘制到屏幕上，而无需重新计算和确定元素的几何属性。

_所以，重排的内存开销比重绘大。在实际开发中，我们应该尽可能减少页面的重排和重绘次数，从而提高页面的性能和响应速度。_