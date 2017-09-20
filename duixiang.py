#-*- coding: utf-8 -*-
#! /usr/bin/env python3

'learn duixiang'

__author__ = 'wangkai'

class Student(object):
    def __init__(self,name,num):
        self.__name = name
        self.__num = num
    def myPrint(self):
        print('%s%s' % (self.__name,self.__num))
    def get_grade(self):
        if self.__num > 100:
            return 'A'
        else:
            return 'B'

student = Student('wangkai',100)

student.myPrint()
print student.get_grade()

class animal(object):
    def run(self):
        print 'Animal is running'

class dog(animal):
    def run(self):
        print 'dog is running'
    def __len__(self):
        return 100

        

d = dog()
d.run()
print len(d)