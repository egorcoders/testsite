# text = '321'
# print(text*-1)


# a = 23
# num = 0 if a > 10 else 11
# print(num)


# a = (5,)

# print(a.copy())

# tup = tuplen(range (0,500,100))
# print(tup.pop())


# a = [ 'cpp', 'go', 'php', 'js', 'java']
# print(a.sort())

# a = 1,
# print(a)


# print(''.split(' '))

# def decorator(func):
#     def inner():
#         func()
#         print('mello')
#     return inner

# # @decorator
# def say_hello():
#     print('hello')

# d = decorator(say_hello)

# d()

# def numbers():
#     lst = []

#     def add_number(number):
#         nonlocal lst
#         lst.append(number)
#         print(sum(lst) / len(lst))

#     return add_number


# n = numbers()
# print(n)
# n(3)
# n(4)
# n(8)


# def decorator_h1(fun):
#     def inner(*args, **kwargs):
#         print('<h1>')
#         fun(*args, **kwargs)
#         print('</h1>')
#     return inner


# def decorator_table(fun):
#     def inner(*args, **kwargs):
#         print('<table>')
#         fun(*args, **kwargs)
#         print('</table>')
#     return inner


# @decorator_table
# @decorator_h1
# def say_name(n):
#     print(n, 'Misha')

# say_name('Good')

# class Balance:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def __repr__(self):
#         return f'Это аккаунт {self.name}'

#     def __str__(self) -> str:
#         return f'Это аккаунт пользователя {self.name}'


# b1 = Balance('Misha', 25)

# print(b1)

# a = 'hello'
# b = 'hello'

# c = [1, 2, 3]
# print(a.__hash__())
# print(c.__missing__(2))