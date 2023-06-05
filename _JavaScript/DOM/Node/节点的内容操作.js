//#region （兼容性）文本内容读写
function getOrSetTextContent(node, content) {
    // 未传递内容时为获取
    if (arguments.length === 1) {
        // textContent 不为 undefined 则为高级浏览器
        // if(node.textContent){
        //     return node.textContent;
        // }else{
        //     return node.innerText;
        // }
        // node.textContent ? node.textContent : node.innerText;
        return node.textContent || node.innerText;   // JS精髓思想
    } else if (arguments.length === 2) {
        // if(node.textContent){
        //     var newContent = node.textContent;
        //     newContent = content;
        //     return newContent;
        // }else{
        //     var newContent = node.innerText;
        //     newContent = content;
        //     return newContent;
        // }
        node.textContent ? node.textContent = content : node.innerText = content;
    }

}
//#endregion