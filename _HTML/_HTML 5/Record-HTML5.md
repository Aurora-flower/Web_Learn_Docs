# HTML 5


## H5 新特性

HTML 5 是 HTML 的第五个版本，相较于前几个版本，提供了一些新特性和改进，包括但不限于：

1. 语义化标签：

    HTML 5 引入了一些新的语义化标签，如 header、nav、section、article、footer 等，用于更加准确地描述网页内容，提高可访问性。

2. 视频和音频支持：

    HTML 5 提供了对视频和音频的本地支持，可以通过 video 和 audio 标签直接在网页上播放视频和音频。

3. Canvas：

    HTML 5 中新增了 Canvas 元素，提供了一种基于 JavaScript 的绘图 API，
    可以用来绘制图像、动画等交互式内容。

4. Web 存储：

    HTML 5 支持使用 localStorage 和 sessionStorage 来进行数据存储，
    相比于传统的 cookie 方式更加方便和高效。

5. Web Workers：

    HTML 5 允许在后台运行 JavaScript 脚本，避免了长时间运行脚本导致
    浏览器阻塞的问题，提高了页面的响应性能。

6. 地理位置支持：

    HTML 5 提供了 Geolocation API，可以获取用户的地理位置信息，
    用于实现基于位置的服务和应用。

7. Web Socket：

    HTML 5 中引入了 WebSocket 协议，可以在客户端和服务器之间进行实时双向通讯，
    极大地提高了实时性和交互性。

8. 表单增强：

    HTML 5 可以处理更多的表单类型，支持日期、时间、搜索等类型输入，
    并且可以进行本地验证和自动填充功能，提高了用户体验。

以上只是 HTML 5 的一部分新特性，还有很多其他改进和新功能。这些新特性大大提高了 Web 应用和服务的功能和性能，使得开发者更加容易实现丰富的用户体验。


---
### 新表单控件

HTML5 引入了一些新的表单控件，使得表单更加丰富，便于使用者直观地操作表单。以下是 H5 新表单控件的一些示例：

1. `date` 和 `time`
      ```html
      <input type="date" name="birthday">
      <input type="time" name="appointment-time">
      ```

2. `datetime-local`
      ```html
      <input type="datetime-local" name="meeting-time">
      ```

3. `week`
      ```html
      <input type="week" name="week-year">
      ```

4. `month`
      ```html
      <input type="month" name="month-year">
      ```

5. `color`
      ```html
      <input type="color" name="color-picker">
      ```

6. `search`
      ```html
      <input type="search" name="search-box">
      ```

7. `tel`
      ```html
      <input type="tel" name="phone-number">
      ```

8. `email`
      ```html
      <input type="email" name="email-address">
      ```

9. `url`
      ```html
      <input type="url" name="website-url">
      ```

10. `range`
      ```html
      <input type="range" name="volume-control">
      ```

以上是一些常见的 H5 新表单控件，除此之外，还有一些其他的表单控件和新特性，如 `autocomplete`、`placeholder`、`required`、`pattern` 等属性，使得表单开发更加高效和灵活。