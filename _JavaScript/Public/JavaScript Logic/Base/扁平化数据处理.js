function flatToTree(flatData) {
    const tree = {};
    for (let i = 0; i < flatData.length; i++) {
        const node = flatData[i];
        if (!node.pid) {
            tree[node.id] = node;
        } else {
            const parentId = node.pid;
            const parentNode = tree[parentId];
            if (parentNode) {
                if (!parentNode.children) {
                    parentNode.children = {};
                }
                parentNode.children[node.id] = node;
            } else {
                findParent(tree, node);
            }
        }
    }
    return Object.values(tree);
}

function findParent(tree, node) {
    for (const key in tree) {
        const parentNode = tree[key];
        if (parentNode.children) {
            if (parentNode.children[node.pid]) {
                parentNode.children[node.id] = node;
                return true;
            } else {
                if (findParent(parentNode.children, node)) {
                    return true;
                }
            }
        }
    }
    return false;
}

flatToTree(flatData);