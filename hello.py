# import calendar
# a= "hello"
# name = input("너의 이름은?")
# print(a, name)
#
#
# print(calendar.month(2020, 1))
#
# for i in range(10):
#     num = input("숫자")
#     if int(num)%2==0:
#         print("짝수")
#     else:
#         print("홀수")


print((3 - 4j).real)  # 실수
print((3 - 4j).imag)  # 허수
print((3 - 4j).conjugate())  # 켤레 복소수

e, f = 3.5, 5.3
print(e, f)
x = y = z = 10
print(x, y, z)
e, f = f, e
print(e, f)
strings = "[dave],[b],[c],[d]"
strings.split(",")
for string in strings.split(","):
    print(string.strip("[]"))

list_a = {"a", "b", "c", "d", "e", "f"}
for data in list_a:
    print(data, "길이", len(data))

data = [1, 2, 3, 4, 5, 6, 7, 8]
data.reverse()
for q in data:
    print(q)

d = "100 달라"
price = int(d.split(" ")[0]) * 1112
print(price)
print("짝수 구구단")
for i in range(2, 10):
    for j in range(2, 10):
        if i * j % 2 == 0:
            print(i, "*", j, "=", i * j)

dong = {"1동", "2동", "3동"}
ho = {"102호", "103호", "104gh"}
for ddd in dong:
    for hhh in ho:
        print(ddd, hhh)

bi = {"a": "f", "b": "g", "c": "h"}
for da in bi:
    print(da, bi[da])

di = {"a": {"f", "o"}, "b": {"g", "x"}, "c": {"h", "o"}}
for da in di.keys():
    for i in di[da]:
        print(i)
        # if da[i] == "o":
        #     print(da)

# def a(ppp):
#     sum = 0
#     ppp1 = format(ppp, 'b')
#     for i in range(0, len(ppp1)):
#
#         if int(ppp1[i]) == 1:
#
#             sum = sum+1
#     print(sum)
#
# oooo = input("값")
# a(int(oooo))
number_list = [5, 1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10, 10]
number_list.sort()

a = set(number_list)
print(a)

s = "i like python"
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.capitalize())
print(s.title())

s = "i like Python. I like java also"
s = s.title()
print(s.count('like'))
print(s.find('like'))
print(s.find('like', 5))
#print(s.find('JS'))
#print(s.rfind('like'))
#print(s.index('js'))
#print(s.rindex('like'))
print(s.startswith("i like"))
print(s.startswith('like', 2))
print(s.endswith('also'))
print(s.endswith('java'), 0, 26)

s = 'spam and ham'

print(s.strip())
print(s.rstrip())
print(s.lstrip())
s = '<><abc><><defg><><>'
print(s.strip('<>'))

s = 'hello java'
print(s.replace('java', 'python'))

s = ' a alive and the heart queen  a'
print(s.center(60))
print(s.center(60, '-'))
# print(s.zfill(60, '0'))
print(s.ljust(60, '0'))

print('20'.zfill(5))

s = 'spam and ham'
t = s.split()
print(t)
t = s.split('and')
print(t)

s2 = ":".join(t)
print(s2)

s3 = "one,two,three"
print(s3.split(','))
print(s3.rstrip(','))
lines = '''lst line
2
3
4
5
6'''
print(lines.splitlines())
print('1234'.isdigit())
print('abcd'.isalpha())
print('1234'.isalpha())
print('abcd'.isdigit())
print('abcd'.islower())
print('abcd'.isupper())

print('\n\n'.isspace())
print(' '.isspace())
print(''.isspace())

print('i have %d apples' % 4)
print('interest rate is %f' % 1.24)
print('intetset rate is %2.4f' % 1.24532353241142)

print('i have {} apples, and i ate {} apples.'.format(5,3))
print('i have {total} apples, and i ate {num} apples.'.format(total=5, num = 3))
print('i have {total} apples, and i ate {num} apples.'.format_map({"total":5,"num":3}))

l = [1, 2, 'ptyhon']
print(l[-2], l[-1], l[0], l[1], l[2])
print(l[1:5])
print(l * 2)
print(l + [3, 4, 5])
print(len(l))
print(2 in l)
del l[0]
print(l)

a= ['apple', 'banana', 10, 20]
a[2] =a[2]+90
print(a)
a = [1,12,123,1234]
a[0:2] =[10,20]
print(a)
a[0:2] =[10]
print(a)

a[1:2] = [20]
print(a)
a[2:3] = [30]
print(a)

a= [1,2,123,1234]
a[1:2]=[ ]
print(a)
a[0:]=[]
print(a)
a= [1,12,123,1234]
a[1:1]= ['a']
print(a)
a[5:] =[123456]
print(a)
a[:0]=[-12,-1,0]
print(a)

a=[1,2,3]
print(a)
a.append(5)
print(a)
a.insert(3,4)
print(a)
print(a.count(2))
a.reverse()
print(a)
a.sort()
print(a)
a.remove(3)
print(a)
a.extend([6,7,8])
print(a)
a.append([5,6,7])
print(a)

a =[1,2,3]
print(a,type(a))
print(a)
print(2 in a)
print(2 not in a)
s ={1,2,3}
s.add(4)
print(s)
s.add(1)
print(s)
s.discard(2)
print(s)
s.remove(3)
print(s)
s.update({2,3})
print(s)
s.clear()
print(s)
s ={1,2,3}
s.add("hi")
print(s)
#set
a={1,2,3,4,5,6,7,8,9,10}
b={10,20,30}

c=a.union(b)
print(c)
d= a.intersection(b)
print(d)
d= a.difference(b)
print(d)
f= a.symmetric_difference(b)
print(f)
print(a.issuperset(d))
print(f.issuperset(a))
print(b.issubset(c))
c= a&b
print(c)
c= a|b
print(c)
c=a-b
print(c)
# 집합이랑 관련이 많은 set
#tuple

t={1,2,3}
print(t, type(t))

t=1,2,'python'
print(t,type(t))

print(t[-2], t[-1], t[0],t[1], t[2])
print(t[1:3])
print(t[:])
print(t*2)
print(len(t))
print(5 in t)

# list [] 원소 변경가능 set {} tuple() 원소 변경 불가능

t=1,2,3
print(t,type(t))
t=1,2,'python'
print(t,type(t))

print(t[-2],t[-1],t[0],t[1],t[2])
print(t[1:3])
print(t[:])
print(t+(3,4,5))


t= 10,20,30,'python' #패킹

print(t)
print(type(t))

a,b,c,d = t #언패킹
print(a,b,c,d)
a,b,c,d= [10,20,30,'python']
print(a,b,c,d)

#a,b =(10,20,30,40,50)
t= (1,2,3,4,5,6)
a, *b= t
print('프린트 ')
print(a,b)
*a, b= t
print(a,b)

a,b,*c= t
print(a,b,c)
a,*b,c= t
print(a,b,c)