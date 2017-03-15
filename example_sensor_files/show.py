import time


class IwataLab(object):

    def method(self, name):
        print("hello, world.")
        time.sleep(1)
        print(name)

iwatalab = IwataLab()
iwatalab.method("yh1126")
