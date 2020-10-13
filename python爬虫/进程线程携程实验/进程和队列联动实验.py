from multiprocessing import Process,Queue,Lock
import time
from time import sleep
import os
import random
num = 1
list = ["a", "b", "c", "d", "e"]
lockA=Lock()
q = Queue(5)
def task1(queue,time1):
    global num
    while True:
        lockA.acquire()
        if queue.full():
            print("队列已经满了")
            lockA.release()
            break
        elif queue.empty():
            print("进行放操作时发现放的检查为空，停止了")
            lockA.release()
            break
        else:
            print("这是第{}次放东西进去".format(num))
            queue.put(list[0])
            print("现在队列长度是{}".format(queue.qsize()))
            num += 1
        lockA.release()
        sleep(random.random() * time1)
def task2(queue,time2):
    global num
    while True:
        lockA.acquire()
        if queue.empty():
            print("队列已经空了")
            lockA.release()
            break
        elif queue.full():
            print("进行取操作时发现取的检查为满，停止了")
            lockA.release()
            break
        else:
            print("这是第{}次取东西出来".format(num))
            queue.get()
            print("现在队列长度是{}".format(queue.qsize()))
            num +=1
        lockA.release()
        sleep(random.random() * time2)
if __name__ == '__main__':
    p1=Process(target=task1,args=(q,1))
    p2=Process(target=task2,args=(q,1))
    q.put(list[0])
    p1.start()
    sleep(0.1)
    #p1.join()如果在这里开启了，那么p2.start()就是会等到p1执行完成后再执行
    p2.start()
    p1.join()
    p2.join()
    print("整个程序结束了")