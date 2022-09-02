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

def numbers():
    lst = []

    def add_number(number):
        nonlocal lst
        lst.append(number)
        print(sum(lst) / len(lst))

    return add_number


n = numbers()
print(n)
n(3)
n(4)
n(8)
