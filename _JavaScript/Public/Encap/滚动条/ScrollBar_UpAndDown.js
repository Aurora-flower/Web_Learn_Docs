;
(function () {
    // 获取DOM对象 [querySelector 高版本浏览器支持]
    let slider = document.querySelector('.wrapper .scroll .slider');
    let content = document.querySelector('.wrapper .content');

    // 输入内容
    for (let i = 0; i <= 1000; i++) {
        content.innerHTML += i + '<br>';
    }

    let bug_con = false;

    // region 滑块跟随内容的高度（视口）调整大小
    function changeSlider (slider, contentElement) {


        // 万能比例公式：滑块的高度 / 滑槽的高度 = 滑槽的高度 / 内容的高度;

        // 视口高度
        let viewportY = document.documentElement.clientHeight;
        let contentH = contentElement.offsetHeight;

        // 滑槽(spout)的高度 / 内容的高度
        let ratioY = viewportY / contentH;

        // 设置滑块的大小
        let sliderScaleY = ratioY * viewportY;
        slider.style.height = sliderScaleY + 'px';

    }

    // endregion

    // region 滑块拖拽效果
    function UpAndDownDrag (object) {
        object.onmousedown = function (event) {
            // event 兼容
            event = event || window.event;

            // 获取元素的初始偏移量(deviation\drift\shifting)
            // (object == event.target)
            let elementDriftY = event.target.offsetTop;

            // 获取鼠标的开始位置
            let mouseStartY = event.clientY;

            document.onmousemove = function (event) {
                // // event 兼容
                // event = event || window.event;

                // （开始移动后）动态获取鼠标的结束（当前）位置；
                let mouseEndY = event.clientY;

                // 鼠标的移动距离
                let mouseMoveDistanceY = mouseEndY - mouseStartY;

                // 元素的结束位置 = 鼠标的移动距离 + 元素的初始偏移量
                let elementLastY = mouseMoveDistanceY + elementDriftY;

                // 边界问题
                // 设置边界[以视口为界限]
                let boundaryY = document.documentElement.clientHeight;

                // 元素大小
                let elementY = object.offsetHeight;

                // 判断是否越过边界
                if (elementLastY >= boundaryY - elementY) {
                    elementLastY = boundaryY - elementY;
                } else if (elementLastY <= 0) {
                    elementLastY = 0;
                }


                // 赋值(样式设置)
                object.style.top = elementLastY + 'px';
            }
            document.onmouseup = function () {
                // 内存占用优化[事件解绑]
                document.onmousemove = document.onmouseup = null;
            }
            // DOM0 取消浏览器默认样式
            return false;
        };
    }

    // endregion

    // 调用函数
    changeSlider(slider, content);
    UpAndDownDrag(slider);


    function fun (event) {
        event = event || window.event;

        let flag;
        event.wheelDelta ? flag = event.wheelDelta > 0 : flag = event.detail < 0;

        let viewportY = document.documentElement.clientHeight;

        let scale = viewportY / content.offsetHeight;
        // console.log(flag)

        // 滑块开始的偏移量
        let startY = slider.offsetTop;

        function exeT () {
            // 滑块结束的偏移量
            let endY = startY - 10;
            startY <= 0 ? endY = 0 : null;
            slider.style.top = endY + 'px';
            // 内容的滚动距离 = 滑块滚动距离 / (滑槽的高度 / 内容的高度);
            let content_dis = endY / scale;
            content.style.top = -content_dis + 'px';
        }

        function exeF () {
            let endY = startY + 10;
            if (startY >= viewportY - slider.offsetHeight) {
                endY = viewportY - slider.offsetHeight;
            }
            slider.style.top = endY + 'px';
            // 内容的滚动距离 = 滑块滚动距离 / (滑槽的高度 / 内容的高度);
            let content_dis = endY / scale;
            content.style.top = -content_dis + 'px';
        }

        flag ? exeT() : exeF();

    }

    document.addEventListener('mousewheel', fun);
    document.addEventListener('DOMMouseScroll', fun);
}());