a, b, c = {int(x) for x in input("输入三个数字\n").split()}

# 第一个方法 sort
s = [a, b, c]
print("方法一\n")
print(*sorted(s, reverse=True))

# 第二个方法:bubble_sort
for i in range(0,2):
    for j in range(0,2-i):
        if s[j] < s[j+1]:
            s[j], s[j+1] = s[j+1], s[j]
print(*s)