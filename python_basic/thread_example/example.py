# coding=utf-8
import threading
import time


def func():
    print(threading.current_thread().getName() + " start")
    time.sleep(1)
    print(threading.current_thread().getName() + " end")


for x in range(5):
    threading.Thread(target=func).start()

print(threading.current_thread().getName() + " end")
