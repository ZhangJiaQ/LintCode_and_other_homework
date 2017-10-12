# import multiprocessing
# import time
#
# def process(num):
#     time.sleep(num)
#     print('Process',num)
#
# if __name__ == '__main__':
#     for i in range(5):
#         p = multiprocessing.Process(target=process, args=(i,))
#         p.start()
#     print('CPU number:' + str(multiprocessing.cpu_count()))
#     for p in multiprocessing.active_children():
#         print('Child process name: ' + p.name + ' id: ' + str(p.pid))
#     print('Process Ended')

# from multiprocessing import Process, Lock
# import time
#
# class  MyProcess(Process):
#     def __init__(self, loop, lock):
#         Process.__init__(self)
#         self.loop = loop
#         self.lock = lock
#
#     def run(self):
#         for count in range(self.loop):
#             time.sleep(1)
#             self.lock.acquire()
#             print('Pid:' + str(self.pid) + ' LoopCount: ' + str(count))
#             self.lock.release()
#
# if __name__ == '__main__':
#     lock = Lock()
#     for i in range(10,15):
#         p = MyProcess(i, lock)
#         p.start()


# from multiprocessing import Semaphore, Lock, Process, Queue
# import time
#
# buffer = Queue(10)
# empty = Semaphore(2)
# full = Semaphore(0)
# lock = Lock()
#
#
# class Consumer(Process):
#
#     def run(self):
#         global buffer, empty, full, lock
#         while True:
#             full.acquire()
#             lock.acquire()
#             buffer.get()
#             print('Consumer pop an element')
#             time.sleep(1)
#             lock.release()
#             empty.release()
#
#
# class Producer(Process):
#     def run(self):
#         global buffer, empty, full, lock
#         while True:
#             empty.acquire()
#             lock.acquire()
#             buffer.put(1)
#             print('Producer append an element')
#             time.sleep(1)
#             lock.release()
#             full.release()
#
#
# if __name__ == '__main__':
#     p = Producer()
#     c = Consumer()
#     p.daemon = c.daemon = True
#     p.start()
#     c.start()
#     p.join()
#     c.join()
#     print('Ended!')



from multiprocessing import Process, Semaphore, Lock, Queue
import time
from random import random

buffer = Queue(10)
empty = Semaphore(2)
full = Semaphore(0)
lock = Lock()


class Consumer(Process):
    def run(self):
        global buffer, empty, full, lock
        while True:
            full.acquire()
            lock.acquire()
            print('Consumer get', buffer.get())
            time.sleep(1)
            lock.release()
            empty.release()


class Producer(Process):
    def run(self):
        global buffer, empty, full, lock
        while True:
            empty.acquire()
            lock.acquire()
            num = random()
            print('Producer put ', num)
            buffer.put(num)
            time.sleep(1)
            lock.release()
            full.release()


if __name__ == '__main__':
    p = Producer()
    c = Consumer()
    p.daemon = c.daemon = True
    p.start()
    c.start()
    p.join()
    c.join()
    print
    'Ended!'







