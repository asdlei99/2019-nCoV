#!/usr/bin/env python3.7
# -*- coding: UTF-8 -*-

'''
Name   : datasource.py
Author : Modnar
Date   : 2020/02/09
Copyrights (c) 2020 Modnar. All rights reserved.
'''

import crawler

data = None

def refresh():
    global data
    data = crawler.request()


def names():
    names = []
    countryNames = []
    provinceNames = []
    for country in data['areaTree']:
        countryNames.append(country['name'])
    names.append(countryNames)
    for province in data['areaTree'][0]['children']:
        provinceNames.append(province['name'])
    names.append(provinceNames)
    return names
    

def countries(idx):
    dic = dict()
    dic['name'] = data['areaTree'][idx]['name']
    if idx == 0:
        dic['isUpdated'] = True
        dic['today'] = data['chinaAdd']
        dic['total'] = data['chinaTotal']
    else:
        dic['isUpdated'] = data['areaTree'][idx]['today']['isUpdated']
        dic['today'] = data['areaTree'][idx]['today']
        dic['total'] = data['areaTree'][idx]['total']
    return dic


def provinces(idx):
    dic = dict()
    dic['name'] = data['areaTree'][0]['children'][idx]['name']
    dic['isUpdated'] = data['areaTree'][0]['children'][idx]['today']['isUpdated']
    dic['today'] = data['areaTree'][0]['children'][idx]['today']
    dic['total'] = data['areaTree'][0]['children'][idx]['total']
    dic['children'] = data['areaTree'][0]['children'][idx]['children']
    return dic

# Initialize the program with `refresh`.
refresh()
