def kitchen(unserved, served):  # served 上菜
    """将未服务的餐点为已服务"""
    print("厨房处理顾客所点菜单")
    while unserved:
        current_meal = unserved.pop()
        # 模拟出餐点的过程
        print("菜单:", current_meal)
        # 将已出餐点转入已服务列表
        served.append(current_meal)


def show_unserved_meal(unserved):
    """显示尚未服务餐点"""
    print("====以下是暂未服务餐点====")
    if not unserved:
        print("***没有餐点***", '\n')
    for unserved_meal in unserved:
        print(unserved_meal)


def show_served_meal(served):
    """显示已经服务的餐点"""
    print("====以下是已经服务餐点====")
    if not served:
        print("***没有餐点***", '\n')
    for served_meal in served:
        print(served_meal)


"""
unserved = ["可乐", "劲辣鸡腿堡", '脆皮鸡']
served = []

# 列出餐厅处理前的点餐内容
show_unserved_meal(unserved)
show_served_meal(served)

# 餐厅服务过程
kitchen(unserved, served)
print("\n", "===厨房处理完毕===", "\n")

# 列出餐厅处理后的点餐内容
show_unserved_meal(unserved)
show_served_meal(served)
"""

# ---------------------------------------------------------------
# 函数可以与主函数的变量名称不一致.
#   涉及全局变量(global variables),局部变量 (local variables)


order_list = ["可乐", "劲辣鸡腿堡", '脆皮鸡']
serve_list = []

# 列出餐厅处理前的点餐内容
show_unserved_meal(order_list)
show_served_meal(serve_list)

# 餐厅服务过程
kitchen(order_list, serve_list)
print("\n", "===厨房处理完毕===", "\n")

# 列出餐厅处理后的点餐内容
show_unserved_meal(order_list)
show_served_meal(serve_list)

# ---------------------------------------
# 问题:
#       当服务完毕后发现order_list为空列表,无法保存餐点内容
# 使用副本传递列表 (列表浅复制)

# 在调用函数 kitchen时传递副本列表
# kitchen(order_list[:],serve_list)
