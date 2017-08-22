# -*- coding: utf-8 -*- 

#study list
classmates = ['wangkai','sunbowei','xiewei']
print(classmates);

#add
classmates.append('1214')               #add list nail#
classmates.insert(1,'wangyuchen')               
a = len(classmates)
print(a,classmates)

#pop
classmates.pop(1)
print(classmates)

#tuple
classmates1 = (0,1,['kai','kai1','kai2'])
print(classmates1)
classmates1[2][0] = 2
classmates1[2][1] = 3
classmates1[2][2] = 4
print(classmates1)

#for and while
for name in classmates:
    print(name)

sum = 0
for x in range(101):
    sum += x
print(sum)

n = 0
sum1 = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    sum1 += n 
print(sum1)

#dict　and set