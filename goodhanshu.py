#高阶函数　让函数的参数接受其他的函数

#map函数：一个参数为函数　另一个参数为可迭代的
#将０－９转化为字符串

L = list(map(str,range(10)))
print(L)


#reduce函数　
#与map函数类似　只不过函数的参数为２个　并且做累乘运算


#filter函数 将传入的函数一次作用于每个每个元素，然后根据
# 返回结果来判断是否舍弃该元素
#filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强
# 迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
def func(n):
    return n % 2 == 1

L1 = range(15)
print(L1)