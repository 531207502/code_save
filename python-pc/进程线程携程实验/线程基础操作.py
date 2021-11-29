import threading
from time import sleep
n=1000
def task1(recycle1):
    global n
    for i in range(recycle1):
        n-=1
        sleep(0.05)
def task2(recycle2):
    global n
    for i in range(recycle2):
        n-=1
        sleep(0.05)
if __name__ == '__main__':
    xc1=threading.Thread(target=task1,args=(100,))
    xc2=threading.Thread(target=task2, args=(200,))
    xc1.start()
    xc2.start()
    xc1.join()
    xc2.join()
    print("这个时候N的值为：{}".format(n))
    print("这个是执行完成后打印")