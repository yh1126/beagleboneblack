import RPi.GPIO as GPIO

class GpioClass(object):

    def __init__(self, channel=None, mode='board'):
        assert channel != None, "please select channel"
        
        if isinstance(channel, int):
            self.PIN == channel
        elif isinstance(channel, list):
        # listの要素数, intかチェックがいる
            self.PIN == channel
        else:
            exception_method()

        if (mode == 'bcm'): #デフォルトでboardモードに設定
            GPIO.setmode(GPIO.BCM)
        else
            GPIO.setmode(GPIO.BOARD)

    def __del__(self):
        print("instance del")
        remove_event_detect(self.PIN)
        GPIO.cleanup(self.PIN)

    def input(self):
        #入力
        return GPIO.input(self.PIN)

    def output(self, value):
        #出力
        GPIO.output(self.PIN, value)

    def pwm(self, freq):
        #pwm 実装は後日考える
        pass

    def add_event_detect(self, edge):
        #event検出機能の追加
        GPIO.add_event_detected(self, edge)

    def add_event_handler(self, handlers):
        #イベントハンドラの追加, handlersはメソッドの参照先でも、メソッドの参照先が格納されたlistでもおk
        if isinstance(handlers, list):
            for handler in handlers:
                GPIO.add_event_callback(self.PIN, handler)
        else:
            GPIO.add_event_callback(self.PIN, handlers)

    def exception_method(self):
        print("instance del")
        remove_event_detect(self.PIN)
        GPIO.cleanup(self.PIN)
