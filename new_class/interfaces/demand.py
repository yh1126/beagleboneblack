#!/usr/local/bin/python
# -*- coding: utf-8 -*-


class Demand(object):

    def __init__(self, mode, edge, *interval, *write, *read):
        print(mode, edge)
        if isinstance(mode, str):
            if mode.upper() == 'DOUBLE':
                self.mode  = mode.upper()
            elif mode.upper() == 'SINGLE':
                self.mode  = mode.upper()
            elif mode.upper() == 'CMD':
                self.mode  = mode.upper()
            else:
                print(mode, 'is not supported. Please give a value(double, single, cmd).')
                return False
        else:
            print(mode, 'is not supported. Please give a value(double, single, cmd).')

        if self.mode == 'DOUBLE' or self.mode == 'SINGLE':
            if edge == True or edge == False:
              self.next_edge = edge
            else:
                print(edge, 'is not supported. Please give a True or False.')
        else:
            #型判定は後で実装 0番地にモードを, 1番地にレジスタを
            self.write_mode  = write[0]
            self.write_cmd   = write[1]
            self.write_value = write[2]
            self.read_mode  = read[0]
            self.read_cmd    = read[1]
            self.read_blocks  = read[2] # read[1]が存在することを事前に確認する必要あり

        if interval != []:
            self.interval = interval
        else:
            pass

    def set_mode(self, mode):
        if isinstance(mode, str):
            if mode.upper() == 'DOUBLE':
                self.mode  = mode.upper()
            elif mode.upper() == 'SINGLE':
                self.mode  = mode.upper()
            elif mode.upper() == 'CMD':
                self.mode  = mode.upper()
            else:
                print(mode, 'is not supported. Please give a value(double, single, cmd).')
                return False
        else:
            print(mode, 'is not supported. Please give a value(double, single, cmd).')

    def set_edge(self, edge):
        if edge == True or edge == False:
            self.edge == edge
        else:
            print(edge, 'is not supported. Please giva a Tru or False.')

    def set_interval(self, interval):
        if interval != []:
            self.interval = interval
        else:
            print('Please give a value.')
        # 型判定は後で実装
