import random

lotto = ['9', '13', '28', '31', '39', '41']
l = ['', '', '', '', '', '']
l1 = ['', '', '', '', '', '']
a = 0
p = [0, 1, 2]
p1 = ['0', '1', '2']
print(p == p1)
print(str(p) == p1)

# while True:
#     i = 0
#     while i != 6:
#         if i == 0:
#             l[i] = random.randint(1, 45)
#         else:
#             l[i] = random.randint(1, 45)
#             for j in range(0, i):
#                 if l[i] == l[j]:
#                     i = i - 1
#         i += 1
#
#     a += 1
#     l.sort()
#     for j in range(6):
#         l1[j] = str(l[j])
#     print(a)
#     print(l1)
#     if l1 == lotto:
#         break


class Account:
    def __init__(self, name, amount):
        self.name = name
        self.balance = amount
        print("개설된 %s 님의 잔고는 %d 입니다." % (self.name, self.balance))

    def deposit(self, amount):
        self.balance += amount
        print('%s 님 %d 입금되었습니다.' % (self.name, self.balance))

    def info(self):
        print(self)


    def withraw(self, amount):
        self.balance -= amount
        print('%s 님 잔고에서 %d 빠져나가서 %d 입니다.'%(self.name, amount, self.balance))

    def __str__(self):
        return '%s 님 잔고는 %d 원입니다.' % (self.name, self.balance)



a1 = Account('ㅋㅋㅋ', 1000000)
b1 = Account('fff', 500000)
b1.deposit(10000)
a1.info()
b1.info()
b1.withraw(10000)
a1.withraw(5000)
c1 = Account('박성무', 500000)
c1.deposit(10000)
# Account.withraw(c1, 50000)
c1.withraw(50000)
