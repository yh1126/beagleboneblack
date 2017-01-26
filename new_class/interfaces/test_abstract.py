# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
#from gpio_sensor_conf import GpioSensorConf

# 抽象クラス
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def sound(self):
        pass

# 抽象クラスを継承
class Cat(Animal):
    def __init__(self):
        print('child')

    def sound(self):
        pass
#        print("Meow")


class Hello(object):
    def __init__(self, channel, mode):
        self.channel = channel
        print('hello', channel, mode)
        print(type(mode))

class Hello2(object):
    def __init__(self, channel=None, mode=None):
        self.channel = channel
        print('hello2', channel, mode)


class Test(Hello, Hello2):
    def __init__(self):
        print('test init')
        super().__init__(1, 'testmode')
        print(self.channel)
        Hello2.__init__(self, 3, 'mode')
        print(self.channel)


if __name__ == "__main__":
    #assert issubclass(Cat().__class__, Animal)
    #assert isinstance(Cat(), Animal)

    t = Test()
