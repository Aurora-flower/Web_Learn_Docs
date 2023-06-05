"""
1.模拟多张银行卡，分别设置密码和余额（使用列表嵌套字典的方式）；

2.提示用户输入银行卡和密码，遍历每张卡的信息验证是否成功；

3.如果用户输入正确：
    提示让用户选择功能（取款，存款，查询...并提示余额）
输入错误：
    提示用户重新输入卡号密码；
选择取款 —— 提示输入取款额度；若是超过余额，提示余额不足；否则，在余额上减去相应的金额；
选择存款 —— 输入存款金额，余额加上相应的额度，并提示余额；
选择退出 —— 重新登；

4.设置：
    三次输入错误账号密码，提示银行卡已锁定，程序结束；
"""
# ----------------------------用户信息-----------------------------------
BankCard_001 = {"姓名": "小白", "卡号": "1001", "密码": "1234", "余额": 10000}
BankCard_002 = {"姓名": "小黑", "卡号": "1002", "密码": "1234", "余额": 15000}
BankCard_003 = {"姓名": "小红", "卡号": "1003", "密码": "1234", "余额": 17000}

cardsList = [BankCard_001, BankCard_002, BankCard_001]

count = 0  # 记录输入错误的次数

# for card in cardsList:
#     if card["姓名"] == "小黑":
#         print(card["余额"])  # 检查是否可执行

# ----------------------------用户登录----------------------------
while 1 == 1:
    card_number = input("请输入卡号:")
    card_password = input("请输入密码:")

    msg = 0  # 记录登陆状态：1成功 0失败
    for card in cardsList:
        if card_number == card["卡号"] and card_password == card["密码"]:
            msg = 1
            count = 0  # 当验证成功时，错误次数清零
            print("恭喜你！%s,已登陆成功！" % card["姓名"])
            break
    if msg == 0:
        count += 1
        if count == 3:
            print("抱歉！您的银行卡已锁定!\n请联系银行工作人员！")
            break
        else:
            print(f"验证失败!您已经连续{count}次输入错误，还有{3 - count}次机会")
            continue
    # break

    # ----------------------------选择银行业务----------------------------
    while 2 == 2:
        choice = int(input("请输入要办理的业务:(1.存款 2.取款 3.退出):"))
        if choice == 1:
            deposit_money = float(input("请输入存款金额:"))
            for card in cardsList:
                if card["卡号"] == card_number:
                    card["余额"] += deposit_money
                    print(f"存款成功！存入{deposit_money}元，余额%s元！" % card["余额"])
                    break
        elif choice == 2:
            withdraw_money = float(input("请输入取款金额:"))
            for card in cardsList:
                if card["卡号"] == card_number:
                    card["余额"] -= withdraw_money
                    print(f"取款成功！取出{withdraw_money}元，余额%s元！" % card["余额"])
                    break
            # pass
        elif choice == 3:
            print("------已退出！------")
            break
        else:
            print("无此业务，请重新选择！")
            continue
        break
