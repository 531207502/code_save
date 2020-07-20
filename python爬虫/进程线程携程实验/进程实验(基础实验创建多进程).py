from multiprocessing import Process
from time import sleep
import os
testnum=1
def test1(a):
    global testnum
    print("任务1的子进程号是{}，父进程号是{}".format(os.getpid(), os.getppid()))
    while True:
        print("这是任务1，传递的值为{}".format(a))
        a+=1
        sleep(1)
        testnum+=10
        print("这个是test1测试num的值：{}".format(testnum))
def test2(b):
    global testnum
    print("任务2的子进程号是{}，父进程号是{}".format(os.getpid(),os.getppid()))
    while True:
        print("这是任务2，传递的值为{}".format(b))
        b+=1
        sleep(2)
        testnum += 15
        print("这个是test2测试num的值：{}".format(testnum))
if __name__=="__main__":
    p1=Process(target=test1,name="任务1",args=(1,))
    p2=Process(target=test2,name="任务2",args=(2,))
    p1.start()
    p2.start()
    print("主进程号是{}".format(os.getpid()))
    b=1
    while True:
        print("这是主界面的程序，3秒一次，第{}次".format(b))
        b+=1
        sleep(3)
        testnum += 5
        print("这个是主程序测试num的值：{}".format(testnum))