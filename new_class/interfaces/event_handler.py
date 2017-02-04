#!/usr/local/bin/python
# -*- coding: utf-8 -*-


class EventHandler(object):

    def __init__(self):
        #イベントとメソッドを追加する箱の作成
        #メソッドをlistとして定義することで呼び出すときにfor文一つで呼び出せるようにする。もう一つ理由があって、同じキーに対して追加を容易にする
        self.events   = {}

    def add(self, event, handler):
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

    def remove(self, event):
        #イベント(key)を元にメソッドを削除
        self.events.pop(self.events[event])
        return self

    def run(self, event):
        #イベント(key)を元にメソッドをコール
        #listで値があるものと、単一であるもので
        for method in self.events[event]:
            method()
        return self

        # keyがないときのエラーをちゃんと書く

    __call__ = run
