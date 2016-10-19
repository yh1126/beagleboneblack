from multiprocessing import Pool
from multiprocessing import Process
from multiprocessing import Queue
import os
import event

class Test:
  def __init__(self):
    self.evt = event.Event()
  
  def function(self, sendor, earg):
    print("process id:" + str(os.getpid()))
    print(sendor, earg)

  def sub(self, earg=None):
    self.function(self, earg)
  
  def main(self):
    self.ps = [
      Process(target=self.sub, args=(1,)),
      Process(target=self.sub, args=(2,))
    ]
    for p in self.ps:
      p.start()
      p.join()
    
t = Test()
t.main()
