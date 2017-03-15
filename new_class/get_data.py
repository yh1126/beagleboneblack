import time

class GetData(object):

    def __init__(self):
        self.loop_cycle   = 0.1
        self.loop_flag    = 1
        self.sensor_value = None

    def sensor_sensor_value(self):
        """abstract method. implement sensing method"""
        return self.sensor_value

    def pooling_get_value(self, method):
        """loop get_sensor_value"""
        while loop_flag:
            self.get_sensor_value()
            time.sleep(self.loop_cycle)

    def period_get_value(self, value):
        for n in range(0, value):
            self.get_sensor_value()
            time.sleep(self.loop_cycle)

    def set_loop_flag(self, new_flag):
        self.loop_flag = new_flag
    
    def set_cycle(self, new_cycle):
        self.loop_cycle = new_cycle

