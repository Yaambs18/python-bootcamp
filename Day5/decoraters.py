import time
def calculate_time(fun):
    
    def wraper():
        t1 = time.time()
        fun()
        t2 = time.time()
        print(t2 -t1)
    return wraper

@calculate_time
def fun():
    for i in range(20):
        print(i, end=' ')
    
fun()