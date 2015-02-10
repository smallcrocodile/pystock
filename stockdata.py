#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# -------------------------------------------------------------------------------
# FileName:     [stockdata.py]
# Purpose:      [module for handle stock data]
# Author:       [Zhou Ke]
# Created:      [2015-2-10]
# Copyright:   (c) ZhouKe 2015
# Licence:     <GPL>
# -------------------------------------------------------------------------------
"""
import struct
import os

# 字典保存设置
settings = {}
settings['syspath'] = r'D:\MyApplications\new_gdzq_v6'
settings['daydata_sh'] = 'vipdoc\sh'
settings['daydata_sz'] = 'vipdoc\sz'
settings['chuquandata'] = 'T0002\hq_cache\gbbq'


# 日线数据格式, 每32个字节为一天数据
# 每4个字节为一个字段，每个字段内低字节在前
# 00 ~ 03 字节：年月日, 整型
# 04 ~ 07 字节：开盘价*1000， 整型
# 08 ~ 11 字节：最高价*1000,  整型
# 12 ~ 15 字节：最低价*1000,  整型
# 16 ~ 19 字节：收盘价*1000,  整型
# 20 ~ 23 字节：成交额（元），float型
# 24 ~ 27 字节：成交量（手），整型
# 28 ~ 31 字节：上日收盘*1000, 整型
# define a dict to store single day data
s_day =    {'date':'1900-01-01',
            'open': 0.0,
            'high': 0.0,
            'low': 0.0,
            'close': 0.0,
            'amount': 0.0,
            'vol': 0.0,
            'reserved': ''}


def get_filename(stockcode):
    """
    Purpose / Usage: 转换股票代码为一个对应的日线数据文件, 返回全路径文件名

    Parameter(s): stockcode string
    """
    if stockcode[0] == '6':
        stockfile = os.path.join(settings['syspath'], 'vipdoc', 'sh', 'lday', 'sh'+ stockcode + '.day')
    else:
        stockfile = os.path.join(settings['syspath'], 'vipdoc', 'sz', 'lday', 'sz'+ stockcode + '.day')

    return stockfile


def load_stock_data(stockfile):
    """
    Purpose / Usage: 从日线数据文件加载单支股票数据, 返回list

    @parameter stockfile
    """
    lst = []
    with open(stockfile, 'rb') as df:
            block = df.read(32)

            while True:
                sd = struct.unpack('iiiiifii', block)
                lst.append(sd)
    return lst


print(load_stock_data(get_filename('600100'))[0])
