import sys
from mymodule import myadd
import random
#  hard-code 시켰다고 함
# a=sys.argv[1]
#
# f= open(a, 'w', encoding='utf-8')
# for i in range(1,10):
#
#     write_size = f.write(sys.argv[2] +"\n")
# print(write_size)
# f.close()
#
# print(myadd(int(sys.argv[3]),int(sys.argv[4])))

for i in range(1,11) :
    print("%d 번째 : " %i ,random.randint(1,100) )