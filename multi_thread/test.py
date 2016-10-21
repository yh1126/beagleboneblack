# -*- coding: utf-8 -*-
import threading
import time

class Test1(object):
  def worker(self, num):
    """thread worker function"""
    print 'Worker: %s' % num
    return
  
  def execute(self):
    threads = []
    for i in range(5):
      self.t = threading.Thread(target=self.worker, args=(i,))
      threads.append(self.t)
      self.t.start()

class Test2(object):
  def worker(self):
    print threading.currentThread().getName(), 'Starting'
    time.sleep(2)
    print threading.currentThread().getName(), 'Exiting'
  
  def my_service(self):
    print threading.currentThread().getName(), 'Starting'
    time.sleep(3)
    print threading.currentThread().getName(), 'Exiting'
  
  def execute(self):
    self.t = threading.Thread(name='my_service', target=self.my_service)
    self.w = threading.Thread(name='worker', target=self.worker)
    self.w2 = threading.Thread(target=self.worker) # デフォルト名を使う
    
    self.w.start()
    self.w2.start()
    self.t.start()
  

class Test3():

  def prints(self, name, sleep_time):
    for i in range(10):
      print(name + ':' + str(i))
      time.sleep(sleep_time)

  def execute(self):
    thread1 = threading.Thread(target=self.prints, args=('a', 1))
    thread2 = threading.Thread(target=self.prints, args=('b', 1))
    thread1.start()
    thread2.start()

if __name__ == '__main__':
#  t1 = Test1()
#  t1.execute()
#  t2 = Test2()
#  t2.execute()
  t3 = Test3()
  t3.execute()
