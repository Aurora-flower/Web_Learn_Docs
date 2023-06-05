# HTML Node

## nodeType


在 HTML DOM 中，每个节点都有一个 `nodeType` 属性，表示该节点的类型。
`nodeType` 的值是一个数值，不同的值表示不同类型的节点。

以下是 `nodeType` 常用的几个值：

- `1` 表示元素节点（`Node.ELEMENT_NODE`）
- `2` 表示属性节点（`Node.ATTRIBUTE_NODE`）
- `3` 表示文本节点（`Node.TEXT_NODE`）
- `4` 表示 CDATA 节点（`Node.CDATA_SECTION_NODE`）
- `5` 表示实体参考节点（`Node.ENTITY_REFERENCE_NODE`）
- `6` 表示实体节点（`Node.ENTITY_NODE`）
- `7` 表示处理指令节点（`Node.PROCESSING_INSTRUCTION_NODE`）
- `8` 表示注释节点（`Node.COMMENT_NODE`）
- `9` 表示文档节点（`Node.DOCUMENT_NODE`）
- `10` 表示文档类型节点（`Node.DOCUMENT_TYPE_NODE`）
- `11` 表示文档片段节点（`Node.DOCUMENT_FRAGMENT_NODE`）
- `12` 表示表示 Notation 节点（`Node.NOTATION_NODE`）

_Tip: 可以通过节点的 `nodeType` 属性来判断其类型，从而进行相应的操作。_

