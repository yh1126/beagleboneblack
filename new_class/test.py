class test1(object):
    def __init__(self, a='default'):
        print "init test1", a

    def method(self):
        print "test1 method"

class test2(object):
    def  __init__(self):
        print "test2"

class test(test1, test2):
    def __init__(self):
#        print "test"
      
      self.x = 1
    
    def __del__(self):
      print "del test"

    def main(self):
        """this method is main function"""
        self.method()

class example(test1):
    def __init__(self):
        self.y = 1
        super().__init__()

    def __del__(self):
      print "del example"




#a = test()
#a.main()

b = example()
