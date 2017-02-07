#!/usr/local/bin/python
# -*- coding: utf-8 -*-


class EventHandler(object):

    def __init__(self):
        #イベントとメソッドを追加する箱の作成
        #メソッドをlistとして定義することで呼び出すときにfor文一つで呼び出せるようにする。もう一つ理由があって、同じキーに対して追加を容易にする
        self.events   = {}
        self.earg

    def add_event_handler(self, event, handler):
        #イベント(key)とメソッドの追加
        print(event, handler, 'get event and handler')
        self.handlers = []

        #すでにあるイベントにメソッドを追加するとき、もともとあるメソッドを取得してくる
        if event in self.events:
            for method in self.events[event]:
                self.handlers.append(method)
            print('found event')
        else:
            print('event not found')

        self.handlers.append(handler)
        self.events.update({event:self.handlers})
        print(self.events, 'complete add')
        return self

    def remove_event_handler(self, event):
        #イベント(key)を元にメソッドを削除
        self.events.pop(event)
        return self

    def call_event_handler(self, event, earg=None):
        #イベント(key)を元にメソッドをコール
        #listで値があるものと、単一であるもので
        if event in self.events:
            for method in self.events[event]:
                method(earg)
        else:
            return self
        return self

        # keyがないときのエラーをちゃんと書く

    __call__ = call_event_handler
