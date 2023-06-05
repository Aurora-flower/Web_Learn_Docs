import re

# ---------------------------------------------------------------------------------------
# 1. 验证手机号码
#   规则： （中国）1开头，第二位可以是3、4、5、7、8
text_numbers = "18677889900"
result_numbers = re.match("1[34587]\d{9}",text_numbers)
print(result_numbers.group())

# ---------------------------------------------------------------------------------------
# 2. 验证邮箱：
#   规则:邮箱名称(由数字、英文字符、下划线组成的) + @符号 + 域名
text_email = "huaying@163.com"
result_email = re.match("\w+@[a-z0-9]+\.[a-z]+",text_email)   # 这里的 .被逸出(转义),普通符号
print(result_email.group())

# ---------------------------------------------------------------------------------------
# 3. 验证 URL：
#   规则:协议(http(s) etc):// + 任意非空白字符
text_url = "https://baike.baidu.com/item/Python/407313?fr=aladdin"
result_url = re.match("(http|https|ftp)://\S+",text_url)  # |：匹配多个字符串或者表达式,'或运算'
print(result_url.group())

# ---------------------------------------------------------------------------------------
# 4. 验证身份证：
#   规则:(china) 18位(前 17位都是数字，后面 1位 number \ x \ X)
text = "36530019870716234x"
result = re.match("\d{17}[\dxX]",text)
print(result.group())