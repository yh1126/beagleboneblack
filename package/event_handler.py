#!/usr/local/bin/python
# -*- coding: utf-8 -*-


class EventHandler(object):

    def __init__(self):
        #イベントとメソッドを追加する箱の作成
        #メソッドをlistとして定義することで呼び出すときにfor文一つで呼び出せるようにする。もう一つ理由があって、同じキーに対して追加を容易にする
        self.events   = {}
        self.earg = 0

    def add_event_handler(self, event, handler):
        #イベント(key)とメソッドの追加
        self.handlers = []

        #すでにあるイベントにメソッドを追加するとき、もともとあるメソッドを取得してくる
        if event in self.events:
            for method in self.events[event]:
                self.handlers.append(method)
        else:
            pass
        self.handlers.append(handler)
        self.events.update({event:self.handlers})
        print(self.events, 'complete add')

    def remove_event_handler(self, event):
        #イベント(key)を元にメソッドを削除
        self.events.pop(event)

    def call_event_handler(self, event, earg=None):
        #イベント(key)を元にメソッドをコール
        #listで値があるものと、単一であるもので
        self.earg = earg
        if event in self.events:
            for method in self.events[event]:
                method(self.earg)
        else:
            pass
        # keyがないときのエラーをちゃんと書く

    __call__ = call_event_handler
