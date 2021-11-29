import time
from multiprocessing import Pool
#使用单线程串行方式执行
def get_page(str):
    print("正在下载 ：",str)
    time.sleep(2)
    print('下载成功：',str)
#使用多线程方式执行
if __name__=="__main__":
    name_list = ['xiaozi', 'aa', 'bb', 'cc']
    start_time = time.time()
    for i in range(len(name_list)):
        get_page(name_list[i])
    end_time = time.time()
    print('单线程执行结果时间为：{} second'.format((end_time - start_time)))
    pool = Pool(4)
    start_time1 = time.time()
    for i in range(len(name_list)):
        pool.apply_async(func=get_page,args=(name_list[i],))
    pool.close()
    pool.join()
    end_time1 = time.time()
    print('多线程执行结果时间为（4个）：{} second'.format((end_time1-start_time1)))
