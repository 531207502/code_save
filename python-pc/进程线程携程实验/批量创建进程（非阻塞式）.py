from multiprocessing import Pool,Queue
import time
from time import sleep
import os
import random
list=[]
def task(task_name):
    print("开始做任务了：",task_name)
    start=time.time()
    sleep(random.random()*2)
    end=time.time()
    #print("完成任务使用时间{},完成任务{}".format(end-start,task_name),os.getpid(),--------os.getppid())
    return "完成任务使用时间{},完成任务{}".format(end-start,task_name),os.getpid(),--------os.getppid()
def callback_func(n):
    list.append(n)
if __name__=="__main__":
    print('开始时间:{}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    pool=Pool(4)
    tasks=["听音乐","吃饭","洗衣服","拖地","赌球","打游戏","打PS"]
    for i in range(7):
        pool.apply_async(func=task,args=(tasks[i],),callback=callback_func)
    pool.close()
    pool.join()
    print("所有任务都结束了")
    for i in list:
        print(i)
    print("运行结束")
    print('结束时间:{}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

