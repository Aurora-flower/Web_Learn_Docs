// 轮播效果
;
// anonymous
(function () {
// region 按钮浮现
    let box = document.getElementById('box');
    let toggle_btn = document.getElementsByTagName('span');

    box.onmouseenter = function () {
        for (let i = 0; i < toggle_btn.length; i++) {
            toggle_btn[i].style.opacity = '.8';
        }
        clearInterval(auto_timer);
    }
    box.onmouseleave = function () {
        for (let i = 0; i < toggle_btn.length; i++) {
            toggle_btn[i].style.opacity = '';
        }
        auto_play();
    }
// endregion

// region 点击切换图片
    let content = document.querySelector('.content');
    let img = document.querySelectorAll('#box .content img');

    // 定时器未初始化前不能访问;
    let auto_timer = null;
    let timer = null;

    // 解决定时器叠加问题[防止重复触发]
    let bug_solve = false;

    // 图片移动
    function Move (object, img, flag) {
        if (bug_solve) {
            return;  // return一旦执行，后面的代码不执行;
        }
        bug_solve = true;

        // 获取轮播图的总宽度
        let contentX = object.offsetWidth;
        let imgX = contentX / img.length;
        let moveDistance;
        flag ? moveDistance = -imgX : moveDistance = imgX;

        // 元素偏移量
        let elementStartX = object.offsetLeft;
        let elementEndX = elementStartX + moveDistance;

        let allTime = imgX; // 间隔移动总距离 [一张图片的大小]
        let stepTime = imgX / 20;  // 间隔移动距离
        let stepNumber = allTime / stepTime;  // 一张图片内移动的次数

        // 图片移动时的渐变效果
        timer = setInterval(function () {
            // 每次间隔期间的元素开始偏移量[从0至1]
            let startX = object.offsetLeft;
            let stepX = moveDistance / stepNumber;
            let endX = startX + stepX;

            function exe () {
                clearInterval(timer);
                // 无限轮播
                endX === -object.offsetWidth + imgX ? endX = -imgX : endX === 0 ?
                    endX = -object.offsetWidth + imgX * 2 : null;
                bug_solve = false;
            }

            // 图片轮播联动小圆点切换
            function btn_img () {
                let icon_index = elementEndX / -imgX - 1;
                for (let m = 0; m < iconList.length; m++) {
                    iconList[m].className = '';
                }
                icon_index > 5 ? icon_index = 0 : icon_index < 0 ? icon_index = 5 : null;
                iconList[icon_index].className = 'current';
            }

            btn_img();

            endX === elementEndX ? exe() : null;
            object.style.left = endX + 'px';
        }, stepTime)
    }

    let contentX = content.offsetWidth;
    let imgX = contentX / img.length;

    let iconList = document.querySelectorAll('.iconList li')

    // 点击小圆点，图片切换
    function changeIcon () {
        for (let j = 0; j < iconList.length; j++) {
            iconList[j].index = j;
            iconList[j].onclick = function () {
                for (let m = 0; m < iconList.length; m++) {
                    iconList[m].className = ''
                }
                let transX = -imgX * this.index - imgX;
                content.style.left = transX + 'px';
                iconList[this.index].className = 'current';
            }
        }
    }

    changeIcon(img);


// endregion
    toggle_btn[1].onclick = function () {
        Move(content, img, true);
    }
    toggle_btn[0].onclick = function () {
        Move(content, img, false);
    }

    auto_play();

    function auto_play () {
        auto_timer = setInterval(function () {
            Move(content, img, true);
        }, 2000)
    }
})();
