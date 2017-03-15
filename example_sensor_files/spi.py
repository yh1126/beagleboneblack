import time
import sys
import spidev

class Sensor(object):
    spi = spidev.SpiDev()
    spi.open(0,0)
    
    def readADC(channel): #抽象メソッド
# ADCから値を取得
# 以下の1はスタートビット, 8+channelはadcのどこのチャンネルを使用するか指定
# また、シングルエンド信号を使用するか差動信号を使用するか設定できるadc(依存)
        adc = spi.xfer([1, (8+channel)<<4, 0 ])
        data = ((adc[1]&3) << 8) + adc[2]
        return data

    def convertVolts(data): #スケルトン
# 分母はadcが何bitで量子化しているかの値が入ってくる
# 10bit = 0~1023なのでfloat(1023)
        volts = (data * 3.3) / float(1023)
        volts = round(volts,4)
        return volts

# 以下はセンサによるので抽象メソッド
    def convertTemp(volts): #抽象メソッド
          temp = (100 * volts) - 50.0
          temp = round(temp,4)
          return temp

    def closeSpiConnection(): #スケルトン
          spi.close()
          sys.exit(0)
