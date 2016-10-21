# -*- coding: utf-8 -*-
from multiprocessing import Pool
from multiprocessing import Process

def function(hoge):
    #やりたいこと
    return hoge

def multi(n):
    p = Pool(10) #最大プロセス数:10
    result = p.map(function, range(n))
    return result

def main():
    data = multi(20)
    for i in data:
        print i

main()
