# -*- codeing: UTF-8 -*-
import math

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
    return result
    
    result1 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    return result1

b = quadratic
print(b(2,3,1))
print(b(1,3,-4))

