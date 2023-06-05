def build_vip(Id, Name, Telephone=''):
    """建立VIP信息"""
    vip_dict = {'VIP_ID': Id, 'Name': Name}
    if Telephone:   # 元素除了是 0、空、None、False 外都是True
        vip_dict['Tel'] = Telephone  # 当赋值的 key不存在时，则为字典增加
    return vip_dict


# 采用while True循环语句的核心思想是如果出现错误的话，可以继续循环。
while True:     # 元素除了是 0、空、None、False 外都是True
    print("建立VIP信息系统")
    id_num = input("请输入ID:")
    name = input("请输入姓名:")
    tel = input("请输入电话号码:")  # 如果直接按 Enter可不建立此字段
    member = build_vip(id_num, name, tel)  # 建立字典
    print(member, '\n')
    repeat = input("是否继续(y/n)? 输入非y字符可结束系统:")
    if repeat != 'y':
        break

print("欢迎下次再使用!")
