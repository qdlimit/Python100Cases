# **一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3
# 6能被 1 2 3整除.1+2+3=6
# 26能被2 14 4 7 1整除 1+2+4+7+14=28
def factor(num):
    target=int(num)
    res=set()
    for i in range(1,num):
        if num%i==0:
            res.add(i)
            res.add(num/i)
    return res

for i in range(2,1001):
    if i==sum(factor(i))-i:
        print(i)
