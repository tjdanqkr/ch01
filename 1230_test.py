import a
from a import mya

import M.b
import sys
a = a.mya(sys.argv[1], sys.argv[2])
b = M.b.myb(sys.argv[3], sys.argv[4])
print(a, b)