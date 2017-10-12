# import threading
# import _thread
# import time
#
# exit_flag = 0
#
#
# class myThread(threading.Thread):
#
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#
#     def run(self):
#         print ("Starting " + self.name)
#         print_time(self.name, self.counter, 5)
#         print ("Exiting " + self.name)
#
#
# def print_time(threadName, delay, counter):
#     while counter:
#         if exit_flag:
#             _thread.exit()
#         time.sleep(delay)
#         print("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1
#
# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# # 开启线程
# thread1.start()
# thread2.start()
#
# print("Exiting Main Thread")


# # 进行同步的多线程
#
# import threading
# import time
#
#
# class myThread(threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#
#     def run(self):
#         print("Starting "+self.name)
#         # 获得锁，成功获得锁定后返回True
#         # 可选的timeout参数不填时将一直阻塞直到获得锁定
#         # 否则超时后将返回False
#         threadLock.acquire()
#         print_time(self.name, self.counter, 3)
#         threadLock.release()
#
#
# def print_time(threadName, delay, counter):
#     while counter:
#         time.sleep(delay)
#         print("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1
#
# threadLock = threading.Lock()
# threads = []
#
# #创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# # 开启新线程
# thread1.start()
# thread2.start()
#
# # 添加线程到线程列表
# threads.append(thread1)
# threads.append(thread2)
#
# # 等待所有线程完成
# for t in threads:
#     t.join()
#
# print("Exiting Main Thread")

#使用队列

import queue
import threading
import time

exitFlag = 0




class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print("Starting " + self.name)
        process_data(self.name, self.q)
        print("Exiting " + self.name)


def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

#创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print("Exiting Main Thread")