# username = input('请输入用户名')
# pwd = input('请输入密码')
#
# if username == 'admin' and pwd == '123456':
#     print('身份验证成功')
# else:
#     print('身份验证失败')


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




