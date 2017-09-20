# -*- codeing: UTF-8 -*-
import math
import os

def my_abs(a):
    if not isinstance(a,(int,float)):
        raise TypeError('bad operand type')

    if a > 0:
        return a
    if a == 0:
        pass
    if a < 0:
        return -a

a = my_abs

print(a(-1))

def quadratic(a,b,c):
    if not isinstance(a,(int,float)):
        raise TypeError('bad operand type')
    result = (-b+math.sqrt(b*b-4*a*c))/(2*a)
    
    
    result1 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    return result,result1

b = quadratic
print(b(2,3,1))
print(b(1,3,-4))

#可变参数
def cal(*numble):
    sum = 0
    for n in numble:
        sum += n
    return sum

print(cal(1,2,3,4,5)) 

#切片
L = ['a','b','c','d','e']
print(L[:3])

#列表生成式
#L1 = [x * x for x in range(1,10) if x % 2 == 0]
#print(L1)

print([x * x for x in range(1,10) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'DEF'])
print(m for m in os.listdir('.'))

#dict
d = {'a':'x','b':'y','c':'z'}
print([x + '=' + y for x,y in d.items()])
#for x,y in d.items():
#   print(x,'=',y)

#将字符串所有字母小写
LM = ['Hello','World','HaHa']
print([c.lower() for c in LM])
