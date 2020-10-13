"""
信号量（BoundedSemaphore类）
互斥锁同时只允许一个线程更改数据，而Semaphore是同时允许一定数量的线程更改数据，

"""

import threading,time

#最多允许2个线程同时运行
semaphore = threading.BoundedSemaphore(2)

def run():
    semaphore.acquire()   #加锁
    print(threading.current_thread().getName(),time.ctime())
    time.sleep(2)
    semaphore.release()    #释放


if __name__ == '__main__':
    for _ in range(10):
        t = threading.Thread(target=run)
        t.start()



"""
python多线程的缺陷：
1、GIL-全局解释器锁
2、无论系统CPU是几核的,只能使用一个来处理进程
https://www.cnblogs.com/xiangsikai/p/8178729.html

"""
