s = input("输入一个字符串\n")
if "oi" in s:
    print("有字串！")
s=s.replace("oi","fzu")
print(s[::-1])