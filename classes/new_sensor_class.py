# -*- condig: utf-8 -*-

import smbus
import time
import RPi.GPIO as GPIO

class Sensor(object):

  def __init__():
# gpioやis2の設定を行う
# eventが必要な場合、eventHandlerの用意。すでに用意しておいたほうがいいのでは？
# 考えられる変数
# in_pin, out_pin, cycle, class_variable
# 入力は必ずしも１つとは限らないので注意
# inは必ずいると思うが、outは必ず必要ではない。pinがnullのときはerrorをかえす。
# inをsetなどで変更しようと思ったが、勝手に変えられたら困るからつくらないほうがいいんじゃないか?
# ledのような出力だけを行うものの場合どうする？そもそもledはセンサーじゃねえ！
# 周期を定義する変数: cycle? period? なにがいいのかな？
# なんか調べたらgetter, setterは悪だ的なのがあったが..どうしよう
# sensorの仕事はセンシングすることだからeventを呼び出すのはまた別のクラスの仕事なのでは？オブジェクト指向では、一つのオブジェクトは一つの仕事で終わらせるのが良い的なのをどっかでみたような、聞いたような 
# 上記のようにした場合センサーが無線でつながっているとき、get_sensor_value()を実行するたびに無線でつながっているセンサーに命令が行くとする。そうした場合、長期的に動かした場合命令のたびに通信を行うので無駄なのでは？だから、どの周期で動かすかはセンサーで定義したほうがいいきがしてきた！

  def get_sensor_value():
      self.value = 0
      # センサごとのdata取得方法を記述
      return value

  def exception_method():
      # 例外処理を記述

  def set_in():
# 入力用のpin番号をセットするためのメソッド
# in_pinがnullの場合、動かないようにする。

  def set_out():
# 出力用のpin番号をセットするためのメソッド

  def set_cycle():
# 周期を定義する変数だが、そもそもすべてwhileで回すと決めていいのか?
# forで20回だけセンシングするといった場合はないのか？
# と、おもったけどforで回しても周期あるわ〜

  def exception_method():
      # 例外処理を記述
