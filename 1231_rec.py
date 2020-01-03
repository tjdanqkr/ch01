import turtle as t

import self as self


class rec:
    def box(x, y, color):
        t.color(color)
        t.fd(x)
        t.left(90)
        t.fd(y)
        t.left(90)
        t.fd(x)
        t.left(90)
        t.fd(y)

    def tri(x, color):
        t.color(color)
        t.fd(x)
        t.left(120)
        t.fd(x)
        t.left(120)
        t.fd(x)


# t.shape('turtle')
# rec.box(100, 50, 'red')
#
# t.penup()
# t.goto(-100,100)
# t.pendown()
# rec.tri(100, 'blue')
# input("")
#

class ppp:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rec1(self):
        print(self)

    def __str__(self):
        return '밑변 %d 높이 %d 인 사각형입니다. 넓이는 %d 입니다' % (self.x, self.y, self.x * self.y)

    def __int__(self):
        return self.x * self.y + self.x * self.y

    def plus(self, other):
        print("두 넓이의 합 %d " % (self.x * self.y + other.x * other.y))

    def __add__(self, other):
        return self.x * self.y + other.x * other.y

    def __mul__(self, other):
        return self.x * self.y * other.x * other.y


class ppp1:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def tri(self):
        print(self)

    def __str__(self):
        return '밑변 %d 높이 %d 인 삼각형입니다. 넓이는 %d 입니다' % (self.x, self.y, self.x * self.y / 2)

    def __add__(self, other):
        return self.x * self.y / 2 + other.x * other.y / 2

    def __mul__(self, other):
        return self.x * self.y / 2 * other.x * other.y / 2


a = ppp(30, 30)
a.rec1()
b = ppp(10, 10)
b.rec1()

print('두개의 사각형 합치기 = %d' % (a + b))
print("두개 넓이의 곱 = %d" % (a * b))

t = ppp1(20, 20)
t1 = ppp1(10, 20)
t.tri()
t1.tri()
print("두개의 삼각형 합치기 = %d " % (t + t1))
print("두개 넓이의 곱 = %d" % (t * t1))

print(a + t)


class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        return self.age + other.age

    def __str__(self):
        return "이양반은 %s 이고, %d 살입니다." % (self.name, self.age)


a1 = student('홍길동', 14)
a2 = student('홍동길', 17)

print(a1, a2)
print(a1 + a2)


class coun:
    name = '국가명'
    pop = '인구'
    cap = '수도'

    def __str__(self):
        return '나의 수도 '


class Korea(coun):

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print('국가 이름은 : ', self.name)


a = Korea('대한민국')
a.show_name()
print(a)

e = "tjdanqkr@gmail.com"

import re

p = re.compile('[a-z]+')
m =p.finditer(e)
for i in m:

    print(i)
print()
print(re.match(r"\w+\@\w+\.",e))