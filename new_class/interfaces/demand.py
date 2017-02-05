#!/usr/local/bin/python
# -*- coding: utf-8 -*-


class Demand(object):

    def __init__(self, mode, edge, interval=0.1, *write, *read):
        self.read_methods = []
        self.write_methods = []
        self.output_edge
        self.mode
        self.interval

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
              self.output_edge = edge
            else:
                print(edge, 'is not supported. Please give a True or False.')

        else:
            if write != ():
                for write_method in write:
                    self.write_methods.append(write)

            if read != ():
                for read_method in read:
                    self.read_methods.append(read)

        if interval != []:
            self.interval = interval
        else:
            self.interval = 0.1 # default by my package

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
            self.edge = edge
        else:
            print(edge, 'is not supported. Please giva a Tru or False.')

    def set_interval(self, interval):
        if interval != []:
            self.interval = interval
        else:
            print('Please give a value.')
