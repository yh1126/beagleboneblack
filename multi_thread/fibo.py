import threading
import time

class MyThread(threading.Thread):
  def __init__(self, count):
    threading.Thread.__init__(self)
    self.count = count
    self.return_value = None #return value

  def run(self):
    sum_value = 0
    for i in range(1, 1 + self.count):
      sum_value += 1
      time.sleep(0.1)
    self.return_value = sum_value #set return value

  def get_value(self): #getter method
    return self.return_value


thread1 = MyThread(5)
thread1.start()
thread1.join()
print(thread1.return_value)
print(thread1.get_value())
