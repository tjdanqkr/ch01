import random

def ran():
    a = 0
    for i in range(1,11) :
        for j in range(1,6):
            a +=1
            print("%d 번째 : " %a ,random.randint(1,100), end="\t" )
        print()

ran()