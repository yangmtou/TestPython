# TestPython
Python 一切皆对象

基本类型
#数字（Number）
加 减 乘 除 乘方 求余 
除在python3中默认结果为浮点数
如果需要得到整数需要使用8//2

#变量 variable

#字符串
可用单引号或者双引号包裹
转义字符
格式化字符串
f-strings
name = 'guozhan'
print(f'My name is {name}')

字符串相关的方法
字符串索引

#列表
a = [1,"hh",23,[2,3,4]]
列表的相关的方法
a.insert
a.pop
len

#函数
 
 
 总结：
 def triangle():
    name = input('你的名字是什么？ ')
    width = int(input('输入三角形宽度: '))
    height = int(input('输入三角形的高度:'))
    result = width*height//2
    print(f'三角形的面积: {result}')

triangle()


#字典
其实就是一对一对的键值对
{'zhangsan':177,'zhangsi':188}

#if条件语句
if age > 18
    do sth
布尔值
0的布尔值是false，其他的都是true
空字符串是false
空数组，空元组是false

==等于
字符串要注意大小写
example：
age = int(input('请输入你的年纪: '))

if age>=18 and age<70:
    print('ok')
elif age>=70:
    print('the age is not ok')
else:
    print('sorry') 
	
#for循环
for x in xs

letters = [1,2,3,4,5,6,7]

for letter in letters:
    if letter==3:
        print('u r so luck')
    else:
        print('this is '+str(letter))

#range函数

生成某个范围的数字

numbers = range(0,11)  #注意为前包含后不包含

for num in numbers:
    print(num)


numbers = list(range(0,41))
print(numbers)

numbers = [x for x in range(0,91)]
print(numbers)

#while循环

flag = True
number = 1

while flag:
    if number <=3:
        answer = input('为什么超级英雄都穿紧身衣')
        if answer == '救人要紧':
            flag = False
            print('恭喜你答对了')
        else:
            print('回答错误')
    else:
        print('次数用完了')
        break

    print(f'这是你的第{number}次回答')
    number += 1
	
#decorator装饰器
用于对函数进行增强

def link(a):
    def linked():
        print('begin')
        a()
        print('end')
    return linked


@link
def personOneSay():
    print('my name is yct')

#personTwoSay = link(personTwoSay())
@link
def personTwoSay():
    print('my name is ymt')

personOneSay()

personTwoSay()

#class类

class Phone():
    def __init__(self):
        self.name = 'iPhone'
        self.color = 'black'
        self.price = 7000

    def print_color(self):
        return self.color

iPhone = Phone()

print(iPhone.color)
print(iPhone.print_color())
#==
print(Phone.print_color(iPhone))

#class类二
传入相应的参数给相应的属性
class Phone():
    def __init__(self,name,color,price):
        self.name = name
        self.color =color
        self.price = price

    def print_color(self):
        return self.color

iPhone = Phone('htc','red',6000)

print(iPhone.color)
print(iPhone.print_color())
#==
print(Phone.print_color(iPhone))


#class类三

要分清哪些属性和方法是属于class的属性和方法，还是只属于
instance的属性和方法
属于class的instance级别的也有

class Phone():
    #class级别的属性
    shape = 'rectangle'
    def __init__(self,name,color,price):
        self.name = name
        self.color =color
        self.price = price

    def print_color(self):
        return self.color

    @classmethod
    def call(self):
        print('喂喂喂')

iPhone = Phone('htc','red',6000)

print(iPhone.color)
print(iPhone.print_color())
#==
print(Phone.print_color(iPhone))

print(Phone.shape)
print(iPhone.shape)

Phone.call()
iPhone.call()

#module 模板
module_print.py
def print_num():
    print(123)

def print_color():
    print('red')

test_module_from_module_print.py
#one
import module_print
module_print.print_color()

#two
from module_print import print_color
print_color()

#three
from module_print import print_color as color
color()

#four
from module_print import *
color()
