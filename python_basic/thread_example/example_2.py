# coding=utf-8
import threading
import time
from threading import current_thread


class MyThread(threading.Thread):
    def run(self) -> None:
        print(current_thread().getName() + " start")
        time.sleep(2)
        print(current_thread().getName() + " end")


th = MyThread()
th.start()
th.join()   # 让主线程等待当前线程结束后再结束
print(current_thread().getName() + " end")
