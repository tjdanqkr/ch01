import sys

# 사전 'key' value
d = {'bask': 5, 'soccer': 11, 'base': 9}
print(d, type(d))

print(d['bask'])
d['valley'] = 6
print(d)

print(len(d))
print('soocer' in d)
print('valley' not in d)

d = dict()
print(d)
d = dict(one=1, two=2)
print(d)
d = dict([('one', 1), ('two', 2)])
print(d)
keys = ('one', 'two', 'three')
values = (1, 2, 3)
d = dict(zip(keys, values))
print(d)
print(list(zip([1, 2, 3], [4, 5, 6])))

# 객체

a = 1
b = "symbol "
#
# def f():
#     a= 2
#     b="table"
#     print(lacals())
#


x = object()
sys.getrefcount(x)
y = x
sys.getrefcount(x)
sys.getrefcount(y)
del (x)
sys.getrefcount(y)

i1 = 10
i2 = 10
print(hex(id(i1)), hex(id(i2)))
s1 = [1, 2, 3]
s2 = [1, 2, 3]
print(hex(id(s1)), hex(id(s2)))
s1 = "hello"
s2 = "hello"
print(hex(id(s1)), hex(id(s2)))
# 주소 복사 레퍼런스 복사

x = [1, 2, 3]
y = x
print(y)
print(hex(id(x)), hex(id(y)))
x[1] = 4
print(y)
x = [1, 2, 3]
y = x[:]
print(y)
print(x is y)
x[1] = 4
print(y)
print(hex(id(x)), hex(id(y)))

import copy

x = [1, 2, 3]
y = copy.copy(x)
print(y is x)
x[1] = 4
print(y)
print(hex(id(x)), hex(id(y)))

a = [1, 2, 3]
b = [4, 5, a]
x = [a, b, 200]
y = copy.deepcopy(x)
print(y)

n = -2
if n > 0:
    print("정수")
elif n == 0:
    print("0")
else:
    print("음수")

money = 8500
print("bytaxi" if money > 10000 else "by bus")

print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])

for i in range(0, 5):
    for j in range(0, i + 1):
        print("*", end="")
    print()

data = [1, 2, 3, 85, 5, 41, 23, 8, 8, 31, 3]
for x in data:
    if x > 10:
        break
    else:
        print("10보다 큰거 없음 ")

for i in range(2, 10):
    for j in range(2, 10):
        print(i, "*", j, "=", i * j, end="\t")

    print()
n = 5
answer = ''
a = n % 2
b = n / 2
if a == 0:
    answer = '수박' * int(b)
else:
    answer = '수박' * int(b) + '수'
print(answer)

colors = ['red', 'orange', 'yellow', 'green', 'pink', 'blue']
for i, color in enumerate(colors):
    print(i, color)

a = [1, 6, 4, 13, 8, 3]
result = [num * 2 for num in a if num % 2 == 0]
print(result)
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
else:
    print(sum)


def swap(a, b):
    return b, a


print(swap(10, 20))

# def g(t):
#     t[0]=0
#
# a= 1,2,3
# g(a)
# print(a)

x = 1


def func(a):
    return a + x


def func2(a):
    global x
    x = 2
    return a + x


print(func(10))
print(func2(10))
print(x)


def sum(a, b):
    return a + b


def incr(a, step=1):
    return a + step


print(sum(2, 3))
print(incr(10))
print(incr(10, 2))
