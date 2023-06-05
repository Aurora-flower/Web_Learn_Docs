# 列出a、b、c、d的二、八、十六进位的值
a, b, c, d = 100, 55, 299, 399
print("它们二进制的值：", bin(a), bin(b), bin(c), bin(d), sep=";\t", end='\n')
print("它们八进制的值：", oct(a), oct(b), oct(c), oct(d), sep=";\t", end='\n')
print("它们十六进制的值：", hex(a), hex(b), hex(c), hex(d), sep=";\t", end='\n')

# 将下列数值转成10进位
x, y = 0b11110010, 0xaaabbb
print("它们10进位的值:", x, y, sep='\t')

a = 10
b = 18
c = 5

result1 = a + b - c
result2 = 2 * a + 3 - c
result3 = b * c - 20 / b
result4 = a % c * b + 10
result5 = a ** c - a * b * c

print(result1, result2, result3, result4, result5, sep=';  ')
