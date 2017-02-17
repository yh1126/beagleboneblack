#!/usr/local/bin/python
# -*- coding: utf-8 -*-


class EventHandler(object):

    def __init__(self):
        # dictで宣言することで{event:method, event1:method1}の関係を持たせる
        self.events  = {}
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
        # あとで型判定実装
        self.handlers.append(handler)
        self.events.update({event:self.handlers})
        print(self.events, 'complete add')

    def remove_event_handler(self, event):
        self.events.pop(event)

    def call_event_handler(self, event, earg=None):
        self.earg = earg
        if event in self.events:
            for method in self.events[event]:
                method(self.earg)
        else:
            print('handler not found')
        # keyがないときのエラーをちゃんと書く

    __call__ = call_event_handler
