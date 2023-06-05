// 1. 获取父元素内第一个子元素节点
function getFirstElementNode(node) {
    // 高版本浏览器
    // 低版本中 node.firstElementChild == null,报错（error）
    if (node.firstElementChild) {
        return node.firstElementChild;
    } else {
        // 低版本浏览器
        // 在低版本浏览器中，若无任何数据则返回null
        let fChild = node.firstChild;

        // 判断是否存在或是否为元素节点
        while (fChild != null && fChild.nodeType !== 1) {
            /**
             * 在 HTML DOM 中，每个节点都有一个 nextSibling 属性，
             * 它返回其父元素的子节点中紧跟在该节点后面的节点。
             * 如果该节点是父元素的最后一个子节点，则该属性返回 null。
             * */
            fChild = fChild.nextSibling;
        }
        return fChild;
    }
}


// 2. 获取父元素内最后一个子元素节点
function getLastElementNode(node) {
    if (node.lastElementChild) {
        return node.lastElementChild;
    } else {
        let lChild = node.lastChild;
        while (lChild != null && lChild.nodeType !== 1) {
            lChild = lChild.nextSibling;
        }
        return lChild;
    }
}

// Tip: 要考虑兼容，获取节点的方式存在兼容性问题;
