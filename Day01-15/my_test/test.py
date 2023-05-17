# username = input('请输入用户名')
# pwd = input('请输入密码')
#
# if username == 'admin' and pwd == '123456':
#     print('身份验证成功')
# else:
#     print('身份验证失败')
# import inspect
import sys


# value = float(input('请输入长度：'))
# unit = input('请输入单位：')
#
# if unit == '英寸' or unit == 'in':
#     print(f'英寸为 {value:.1f} , 厘米为 {value * 2.54:.1f}')
# elif unit == '厘米' or unit == 'cm':
#     print(f'英寸为{value/2.54:.1f} , 厘米为 {value:.1f}')
# else:
#     print('单位不正确，请重新输入')

# sum = 0
# for i in range(101):
#     print(i)
#     sum += i
# print(sum)
#
# sum = 0
#
# for i in range(2, 101, 2):
#     sum += i
# print(sum)
#
# sum = 0
#
# for i in range(101):
#     if i % 2 == 0:
#         sum += i
#
# print(sum)


# import random
#
# answer = random.randint(1, 100)
# counter = 0
# print(answer)
# while True:
#     counter += 1
#     gusnumber = int(input('输入数字'))
#     if gusnumber > answer:
#         print('小一点')
#     elif gusnumber < answer:
#         print('大一点')
#     else:
#         print('正确答案！')
#         break
# print('您一共猜了%d次' % counter)
# if counter > 7:
#     print('您的智商明显不足')


# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d * %d = %d' % (i, j, i * j), end='\t')
#     print()


# 数学基础： 值得注意的是，end的来源是:
# 如果x已经被检验不可被除尽，
# 那么 number/x 同样如此，所以，我们只需验证到当number/x 与 x 相交时的x的值即可
# 即x = number/x x = sqrt(number)
# 在是否需要+1的这个问题上来说，
# 可知若 x = int(sqrt(number)) 且 number % x != 0 则 number % (x + 1)  != 0
# 则 end 可以设为 sqrt(number)
# from math import sqrt
#
# num = int(input('请输入一个素数'))
# end = int(sqrt(num))
# is_prime = True
#
# for i in range(2, end + 1):
#     if num % i == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print('%d 为素数' % num)
# else:
#     print('%d 不为素数' % num)


# for i in range(1, 5 + 1):
#     for j in range(1, i + 1):
#         print('*', end='')
#     print()

# for x in range(0, 20):
#     for y in range(0, int((100 - 5 * x)/3)):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z / 3 == 100:
#             print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))
#


# import random
#
# money = 1000
#
# while money > 0:
#     need_going_on = True
#     print('您的总资产为：%d' % money)
#     debt = int(input('请下注'))
#     if debt > money:
#         print('您没有这么多钱')
#         continue
#     current_point = random.randint(1, 6) + random.randint(1, 6)
#     if current_point == 7 or current_point == 11:
#         print('玩家胜')
#         money += debt
#     elif current_point == 2 or current_point == 3 or current_point == 12:
#         print('庄家胜')
#         money -= debt
#     else:
#         while need_going_on:
#             need_going_on = False
#             new_point = random.randint(1, 6) + random.randint(1, 6)
#             if new_point == current_point:
#                 print('玩家胜利')
#                 money += debt
#             elif new_point == 7:
#                 print('庄家胜利')
#                 money -= debt
#             else:
#                 need_going_on = True
# print('您没钱了，游戏结束')


# 斐波那契
# x = 1
# y = 1
# t = 0
# for i in range(20 - 2):
#     x = x + y
#     t = x
#     x = y
#     y = t
#     print(x)
# 完美数
# import math
# for i in range(1, 10000):
#     end = int(math.sqrt(i))
#     num = 0
#     for j in range(1, end + 1):
#         if i % j == 0:
#             num = j + num + i // j
#     if num - i == i:
#         print(i)

# 阶乘
# def fac(num):
#     res = 1
#     for i in range(1, num + 1):
#         res *= i
#     return res
#
#
# result = int(fac(7) / (fac(3) * fac(4)))
#
# print(result)

# import random
#
#
# def roll(n=2):
#     total = 0
#     for _ in range(n):
#         total += random.randint(1, 6)
#     return total
#
#
# def add(a=0, b=0, c=0):
#     return a + b + c
#
#
# def fac2(a=0, b=0, c=0):
#     return a * b + c
#
#
# print(roll())
# print(roll(4))
#
# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
#
# print(add(c=50, a=100, b=20))
#
# print(fac2(a=1, c=6, b=1))
#
#
# def add(*a):
#     total = 0
#     for val in a:
#         total += val
#     return total
#
#
# print(add(1, 2, 3, 4, 5, 6))
#
# print(add(23, 3, 4, 5, 56, 6, 7))

# import model1
# import model2
# import model3
#
# if __name__ == '__main__':
#     print('call foo()')
#     model2.foo()
#
#
# model1.foo()
# model2.foo()
# model3.foo()
#
# if __name__ == '__main__':
#     print('call foo()')
#     model1.foo()

# def gcd(x , y):
#
#     (x , y) = (y , x) if x > y else (x ,y)
#     print(x)
#     print(y)
#     for fac in range(x ,0 ,-1):
#         if x % fac == 0 and y % fac == 0 :
#             return fac
#
#
# i = gcd(12, 3)
# print(i)
#
# def lcm(x, y):
#     return x * y // gcd(x , y)
#
#
# lcm1 = lcm(12, 3)
# print(lcm1)

# def is_palindrome(num):
#     t = num
#     tmp = 0
#     while t > 0:
#         tmp = tmp * 10 + t % 10
#         t //= 10
#         # print(t)
#         # print(tmp)
#     return num == tmp


#
#
# print(is_palindrome(131))


# from math import *
# #
# #
# def is_prime(num):
#     end = int(sqrt(num))
#     for i in range(2 , end + 1):
#         if num % i == 0:
#             return False
#     return True
# # print(is_prime(11))
#
# if __name__ == '__main__':
#     num = int(input('输入数据'))
#     if is_prime(num) and is_palindrome(num):
#         print('是回文素数')

# def foo():
#     b = 'hello'
#
#     def foo1():
#         c = True
#         print(a)
#         print(b)
#         print(c)
#
#     foo1()
#
#
# if __name__ == '__main__':
#     a = 10
#
#     foo()


# def foo():
#     global a
#     a = 200
#     print(a)
#
#
# if __name__ == '__main__':
#     a = 100
#
#     foo()
#
#     print(a)

# def foo():
#     a = 100
#
#     def foo1():
#         nonlocal a
#         a = 200
#         print(a)
#     foo1()
#     print(a)
#
#
# if __name__ == '__main__':
#     foo()


# s1 = '\'hello, world!\''
# s2 = '\n\\hello, world!\\\n'
# print(s1, s2, end='')
#
# s1 = r'\'hello, world!\''
# s2 = r'\n\\hello, world!\\\n'
# print(s1, s2, end='')

# if __name__ == '__main__':
#     s = 'hello , world'
#
#     s1 = s + '你好，这个世界'
#
#     print('你好' in s1)
#
#     print('hello' not in s)
#
#     str2 = 'abc123456'
#
#     print(str2[2])
#
#     print(str2[2:5])
#
#     print(str2[2:])
#
#     print(str2[0::3])
#
#     print(str2[::2])
#
#     print(str2[::-1])
#
#     print(str2[-3::-2])
#
#     print(str2[-3:])
#
#     print(s)
#     print(s1)


# if __name__ == '__main__':
#     str1 = "helloworld"
#     print(str1.find('or'))
#     print(str1.find('h'))
#
#     print(str1.capitalize())
#
#     print(str1.title())
#
#     print(str1.upper())
#
#     print(str1.isupper())
#
#     print(str1.__len__())
#
#     print(str1[str1.__len__() - 1])
#
#     print(str1[-1:])
#
#     print(str1.startswith('he'))
#
#     print(str1.__sizeof__())
#
#     # print(inspect.getsource(type(str1)))
#
#     print(str1.endswith('!'))
#
#     print(str1.rjust(50 , '*'))
#
#     print(str1.ljust(50 , '#'))
#
#     print(str1.center(50))
#
#     str2 = str(1345) + 'sfsf'
#     print(str2)
#
#     print(str2.isdecimal())
#
#     print(str2.isalnum())
#     print(str1.isalpha())
#     print(str1.isdigit())
#
#     print(str1.rjust(50 , '*').strip('*'))


# def mix_plus_multi(x, y):
#     return x + y, x * y


# if __name__ == '__main__':
#     # a = 5
#     # b = 10
#     #
#     # print('{0} * {1} = {2}'.format(a , b , a * b))
#     #
#     # print(f'{a} * {b} = {a * b}')
#
#     list1 = [1, 2, 3, 4, 123]
#
#     # l = [1, 23, 4, 4]
#
#     print(list1.__sizeof__())
#     print(list1)
#     list1 = [1, 2, 3, 4, 123] * 3
#     # list1 *= list1
#     print(list1)
#
#     print(len(list1))
#
#     print(list1[0])
#     print(list1[-1])
#
#     print(list1[0::2])
#
#     print(list1[-1::-1])
#
#     for i in range(list1.__len__()):
#         print(list1[i])
#
#     print('======================')
#
#     for elem in list1:
#         print(elem)
#
#     for index, elem in enumerate(list1):
#         print(index, elem)
#
#     p, m = mix_plus_multi(1, 5)
#
#     print(p)
#     print(m)
#
#     list_ = list1[0:5]
#
#     list_.append(1)
#     list_.append(2)
#
#     list1 += list_
#
#     print(list_)
#     print(list1)
#
#     list_ += [1, 2]
#
#     print(list_)
#
#     if 1 in list_:
#         list_.remove(1)
#     print(list_)
#
#     list_.pop(0)
#     print(list_)
#
#     list_.pop(-1)
#     print(list_)
#
#     list_.clear()
#     print(list_)

# if __name__ == '__main__':
#     fruits = ['grape', 'apple', 'strawberry', 'waxberry']
#     fruits += ['pitaya', 'pear', 'mango']
#
#     fruits += [1]
#
#     print(fruits)
#     print(type(fruits[0]))
#     print(type(fruits[-1]))
#     fruits.pop(-1)
#
#     st_ = 'st11'
#
#     l = sorted(fruits, key=len , reverse=True)
#     print(fruits)
#     print(l)
#
#     fruits.sort(key=len, reverse=True)
#     print(fruits)

# 在python中，与其他语言不同的是，他可以将形参编译到字节码文件中
# def foo(a=10, b=1, c=2):
#     return c * a + b
#
#
# if __name__ == '__main__':
#     i = foo(a=2, c=1, b=6)
#     print(i)

# if __name__ == '__main__':
#     t = [x for x in range(1, 100)]
#     r = range(1, 100)
#     print(type(r))
#     print(t)
#     print(sys.getsizeof(t))
#     f = (x for x in range(1 , 100))
#     print(type(f))
#     print(sys.getsizeof(f))
#     print(f)
#     print(sys.getsizeof(f))
#
#     f = [x + y for x in '123444' for y in 'adsfsadfa']
#     print(f)

# for val in f:
#     print(val)


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for i in fib(20):
        print(i)


if __name__ == '__main__':
    main()
