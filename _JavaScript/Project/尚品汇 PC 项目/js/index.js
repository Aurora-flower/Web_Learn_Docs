// 放大镜（联动主图、蒙版、大图）
oLope()

function oLope () {
    let oMask = document.querySelector(".previewArea .preview .smallArea .mask");
    let oMainBox = document.querySelector(".previewArea .preview .smallArea");
    let oBigBox = document.querySelector(".previewArea .preview .bigArea");
    let oBigImg = document.querySelector(".previewArea .preview .bigArea img");

    // 不设置进入事件，节省内存的占用
    oMainBox.onmousemove = function (event) {
        oMask.style.display = "block";
        oBigBox.style.display = "block";
        let variable = {
            mouseX: event.clientX,
            mouseY: event.clientY,
            boxW: oMainBox.clientWidth,
            boxH: oMainBox.clientHeight,
            maskW: oMask.offsetWidth,
            maskY: oMask.offsetHeight,
            gapX: oMainBox.getBoundingClientRect().left,
            gapY: oMainBox.getBoundingClientRect().top,
        }
        let location = {
            x: variable.mouseX - variable.gapX - variable.maskW / 2,
            y: variable.mouseY - variable.gapY - variable.maskY / 2,

        }
        let bounding = {
            x: variable.boxW - variable.maskW,
            y: variable.boxH - variable.maskW,
            NX: oBigBox.clientWidth - oBigImg.offsetWidth,
            NY: oBigBox.clientHeight - oBigImg.offsetHeight,
        }
        let scaleX = bounding.NX / bounding.x;
        location.x >= bounding.x ? location.x = bounding.x : location.x <= 0 ? location.x = 0 : null;
        location.y >= bounding.y ? location.y = bounding.y : location.y <= 0 ? location.y = 0 : null;
        oMask.style.left = location.x + 'px';
        oMask.style.top = location.y + 'px';
        oBigImg.style.left = scaleX * location.x + 'px';
        oBigImg.style.top = scaleX * location.y + 'px';
    }
    oMainBox.onmouseleave = function () {
        oMask.style.display = "none";
        oBigBox.style.display = "none";
    }
}

// 缩略图操作
oThumb()

function oThumb () {
    let oBigImg = document.querySelector(".previewArea .preview .bigArea img");
    let imgListOut = document.querySelector(".previewArea .prescroll .listOut .list");
    let oMainImg = document.querySelector(".previewArea .preview .smallArea img")
    let imgSrcS = goodData.imgsrc;
    // 创建标签
    imgSrcS.forEach(function (item) {
        let li = document.createElement("li");
        let img = new Image();
        img.src = item.s;
        li.append(img);
        imgListOut.append(li)
    });

    let imgList = document.querySelectorAll(".previewArea .prescroll .listOut .list img");
    imgList.forEach(function (item, index) {
        // console.log(imgList.length);
        item.onmouseenter = function () {
            this.style.border = '1px solid red';
            oMainImg.src = this.src;
            oBigImg.src = imgSrcS[index].b
        }
        item.onmouseleave = function () {
            this.style.border = '';
        }
    });
    let btnLeft = document.querySelector(".previewArea .prescroll .left");
    let btnRight = document.querySelector(".previewArea .prescroll .right");
    let singleLi = document.querySelectorAll(".previewArea .prescroll .listOut .list li")[0];
    // console.log(imgList.length,singleLi.offsetWidth);
    let step = singleLi.offsetWidth * 2;
    let allMove = singleLi.offsetWidth * (imgList.length - 5);
    let location = 0;
    // console.log(allMove)
    btnRight.onclick = function () {
        location + step <= allMove ? location += step : location = allMove;
        imgListOut.style.transform = "translateX(-" + location + "px)"
    }

    btnLeft.onclick = function () {
        location > step ? location -= step : location = 0;
        imgListOut.style.transform = "translateX(-" + location + "px)"
    }
}

// 添加详情
oAddDetail()

function oAddDetail () {
    let priceArea = document.querySelector('.mainCon .detailArea .priceArea');
    let goodsDetail = goodData.goodsDetail;
    // region 字符串
    priceArea.innerHTML = "<h3 class=\"title\">" + goodsDetail.title + "</h3>\n" +
        "\t\t\t\t\t\t\t<p class=\"con1\">" + goodsDetail.recommend + "</p>\n" +
        "\t\t\t\t\t\t\t<div class=\"price\">\n" +
        "\t\t\t\t\t\t\t\t<div class=\"priceDetail\">\n" +
        "\t\t\t\t\t\t\t\t\t<p>价&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;格</p>\n" +
        "\t\t\t\t\t\t\t\t\t<p>￥ <span>" + goodsDetail.price + "</span> 元</p>\n" +
        "\t\t\t\t\t\t\t\t</div>\n" +
        "\t\t\t\t\t\t\t\t<div class=\"buy\">\n" +
        "\t\t\t\t\t\t\t\t\t<p>促&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;销</p>\n" +
        "\t\t\t\t\t\t\t\t\t<p><span>" + goodsDetail.promoteSales.type + "</span>" + goodsDetail.promoteSales.content + "\n" +
        "\t\t\t\t\t\t\t\t\t</p>\n" +
        "\t\t\t\t\t\t\t\t</div>\n" +
        "\t\t\t\t\t\t\t</div>\n" +
        "\t\t\t\t\t\t\t<div class=\"support\">\n" +
        "\t\t\t\t\t\t\t\t<div class=\"supportDetail\">\n" +
        "\t\t\t\t\t\t\t\t\t<p>支&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;持</p>\n" +
        "\t\t\t\t\t\t\t\t\t<p>" + goodsDetail.support + "</p>\n" +
        "\t\t\t\t\t\t\t\t</div>\n" +
        "\t\t\t\t\t\t\t\t<div class=\"address\">\n" +
        "\t\t\t\t\t\t\t\t\t<p>配&nbsp;送&nbsp;至</p>\n" +
        "\t\t\t\t\t\t\t\t\t<p>" + goodsDetail.address + "</p>" +
        "\t\t\t\t\t</div>\n" +
        "\t\t\t\t\t</div>";
    // endregion
    let chooseArea = document.querySelector(".chooseArea");
    let crumbData = goodData.goodsDetail.crumbData;

    // 创建标签
    crumbData.forEach(function (item) {
        let dt = document.createElement('dt');
        dt.innerHTML = item.title;
        let dl = document.createElement('dl');
        dl.append(dt);
        item.data.forEach(function (item) {
            let dd = document.createElement('dd');
            dd.innerHTML = item.type;
            dl.append(dd);
            // 绑定价格数据，联动价格变动
            dd.dataset.changePrice = item.changePrice;
        });
        chooseArea.append(dl);
    })
}

// 选中高亮显示
oChoose();

function oChoose () {
    let arr = new Array(4);
    arr.fill(null);
    let detail_dl = document.querySelectorAll(".detailArea .chooseArea dl ");
    let chooseInsert = document.querySelector(".detailArea .chooseInsert");
    // console.log(detail_dl);
    detail_dl.forEach(function (item, index) {
        let detail_dd = item.querySelectorAll("dd");
        // console.log(detail_dd);
        detail_dd.forEach(function (item) {
            item.onclick = function () {
                detail_dd.forEach(function (item) {
                    item.style.color = "#666";
                })
                this.style.color = "red";
                // arr[index] = item.innerHTML;
                arr[index] = item;
                // console.log(arr);

                chooseInsert.innerHTML = ""
                arr.forEach(function (item,index) {
                    if (item) {
                        let mark = document.createElement("mark");
                        let a = document.createElement("a");
                        a.innerHTML = "X";
                        a.dataset.index = index;
                        // console.log(a.dataset.index);
                        // mark.innerHTML = item;
                        mark.innerHTML = item.innerHTML;
                        mark.append(a);
                        // console.log(mark);
                        chooseInsert.append(mark);
                    }
                });
                oRemove(arr);
                oSinglePrice(arr);
            };
        });
    });
}

// 删除选中
function oRemove (arr) {
    let aList = document.querySelectorAll(".detailArea .chooseInsert mark a");
    let dlList = document.querySelectorAll(".detailArea .chooseArea dl");
    aList.forEach(function (item) {
        item.onclick = function () {
            arr[item.dataset.index] = null;
            item.parentElement.remove();
            let dd = dlList[item.dataset.index].querySelectorAll("dd");
            dd.forEach(function (item) {
                item.style.color = '#666';
            })
            dd[0].style.color = "red";
            // console.log(item.dataset.index);
            // console.log(arr)
        }
    });
    // console.log(arr);
}


// 价格联动 - 单价
function oSinglePrice (arr) {
    let basePrice = goodData.goodsDetail.price;
    let priceValue = document.querySelector('.detailArea .price .priceDetail p:nth-child(2) span');
    let inp = document.querySelector('.detailArea .goodsNum .num input');
    let num = Number(inp.value);
    arr.forEach(function(item){
        if(item){
            basePrice += +item.dataset.changePrice;
        }
    });
    priceValue.innerHTML = String(basePrice * num);
}

// 价格联动 - 数量选择
changeNum();
function changeNum(){
    let singPrice = document.querySelector('.detailArea .price .priceDetail p:nth-child(2) span');
    let inp = document.querySelector('.detailArea .goodsNum .num input');
    let add = document.querySelector('.detailArea .goodsNum .num .plus');
    let sub = document.querySelector('.detailArea .goodsNum .num .mins');
    let inp_value = inp.value;

    // 加
    add.onclick = function(){
        inp_value++;
        inp.value = inp_value;  // wait for
        singPrice.innerHTML = String(singPrice.innerHTML/(inp_value-1) * inp.value);
    }
    // 减
    sub.onclick = function(){
        if(inp_value > 1){
            inp_value--;
        }else{
            return;
        }
        inp.value = inp_value;
        singPrice.innerHTML = String(singPrice.innerHTML / (inp_value + 1) * inp.value);
    }
}

