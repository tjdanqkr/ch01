# 예외 처리
try:
    # Do something
    print('1번')
    4/0
except Exception as e:
    # do something error
    print(e)

else :
    #예외가 발생하지 않는 경우
    print('에러 발생 x ')
finally:
    #마지막 무조건 실행
    print('ㅋㅋㅋㅋ')
print('넘어감 ')

#파일 입출력
f= open('multilines.txt', 'w', encoding='utf-8')
for i in range(1,10):

    write_size = f.write("Life is too short\n")
print(write_size)
f.close()

f= open('test.txt', 'r', encoding='utf-8')
write_size = f.read()
print(write_size)
f.close()

f= open('multilines.txt', 'r')
while True:
    line = f.readline() # 텍스트 단위를 줄 단위로 읽음
    if not line:
        break
    print(line, end='')
f.close()
print("*********************************")
try:
    f = open('multilines.txt', 'r')
    # while True:
    #     line = f.read()  # 텍스트 단위를 줄 단위로 읽음
    #     if not line:
    #         break
    #     print(line, end='')
    line = f.read()
    print(line)
except Exception as e:
    print("\n 파일이 없습니다.")
    print(e)
else:
    print(" 출력되었ㅅ브니다.")
finally:
    f.close()
print("*********************************")
f= open('multilines.txt', 'r')
#f.readlines()  # 리스트로 보여줌
for line in f.readlines():
    print(line,end="")

f.close()
print("*********************************")

print("*********************************")

f = open('multilines.txt', 'r')

lines = f.readlines()
for line in lines :
    print(line, end="")
f.close()
print("*********************************")

# 파일 입출력 개요 바이너리 파일 다루기
f_stc = open('3.png', 'rb')  # 파일 읽음
data= f_stc.read()
f_stc.close()

f_stc= open('3-copy.png', 'wb')  #파일을 씀
f_stc.write(data)
f_stc.close()

f_stc= open('3-copy.png', 'ab')  #파일을 덮어 씀
f_stc.write(data)
f_stc.close()

f= open('3-copy.png', 'rb')
#f.readlines()  # 리스트로 보여줌
print(f.read())
f.close()

#요즘은 이렇게 많이 씀 close를 지우는 형식으로 버전 3 에서 이렇게 씀

with open('3-copy.png', 'rb') as f:
    for line in f.readlines():
        print(line)

print(f.close())

#using pickle 통신용으로 많이 씀 직열화 통신
# a=input() #1번
# b= input()
# a,b = input().split(',') #2번
# a,b= map(int , input().split(',')) #3번
# print('Result : %d ' %(a+b))

#
# def a(ppp):
#     sum = 0
#     ppp1 = format(ppp, 'b')
#     for i in range(0, len(ppp1)):
#
#         if int(ppp1[i]) == 1:
#
#             sum = sum+1
#     print(sum)
#     f = open('test.txt', 'w', encoding='utf-8')
#     f.write("  "+str(ppp)+"   "+str(ppp1))
#     f.close()
#
# oooo = input("값")
# a(int(oooo))
#

