from multiprocessing import Process
from time import sleep
import os
class MyProcess(Process):
    def __init__(self,name,num):
        #super(MyProcess,self).__init__()
        super().__init__()
        self.name=name
        self.n=num
        print("self.n的值是{}".format(self.n))
    def run(self):
        while True:
            print("这个是重写的run方法里的东西，数值是{}".format(self.n))
            self.n+=1
            sleep(1)
    def test1(self,num1):
        while True:
            print("这个是自定义的test方法，数值是{}".format(num1))
            sleep(4)
if __name__== '__main__':
    p1=MyProcess("刘金凤",10)
    p2 = MyProcess("程宇龙", 100)
    p1.start()
    p1.test1(222)
    p2.start()
