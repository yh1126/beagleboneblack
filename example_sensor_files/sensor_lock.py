import threading

motion_sensor_rlock = threading.RLock() #local object

class MotionSensor():

    def __init__():
        #コンストラクタ
        global motion_sensor_rlock
    def get_senor_value():
        motion_sensor_rlock.acquire()
        # センサごとのdata取得方法を記述
        motion_sensor_rlock.release()
