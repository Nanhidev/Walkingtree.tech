import sys

class test :
    pass

t1 = test()
t2 = t1
t3 = t1
t4 = t1
t5 = t1
print(sys.getrefcount(t1))