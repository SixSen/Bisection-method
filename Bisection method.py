#  区间二分法
import sys


def f(xe):
    y = xe ** 3 - xe - 1
    return y


a = 1
b = 1.5
e = 0.000000001  # 误差要求
i = 0  # 迭代次数计数

if f(a) * f(b) >= 0:
    print("此区间内无根")
    sys.exit()
while i < 1000:
    x = (a + b) / 2
    if f(x) == 0:
        print("方程的解为:%f" % b)
        sys.exit()
    elif (f(x) * f(a)) >= 0:
        a = x
    elif (f(x) * f(a)) < 0:
        b = x
    if abs(b - a) < e:
        print("方程的解为:%f" % b)
        sys.exit()
    else:
        i = i + 1

print("计算失败")
