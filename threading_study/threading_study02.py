"""
自定义线程：
继承threading.Thread来定义线程类，然后重写__init__方法和run方法，使用start方法来启动线程。

"""
import threading
import time

class MyThread(threading.Thread):

    def __init__(self,name):
        """
        重写__init__方法,可以使用super来调用父类的方法
        :param name:
        """
        # super().__init__()
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        """
        重写run方法，注意方法名只能是 run
        这里也可以调用其他方法
        :return:
        """
        print(self.name, time.ctime())
        time.sleep(2)
        print(self.name, time.ctime())
        time.sleep(2)
        print(self.name, time.ctime())
        time.sleep(2)
        print(self.name, time.ctime())

if __name__ == '__main__':
    for i in range(3):
        t = MyThread(name="线程-%s"%i)
        t.start()



