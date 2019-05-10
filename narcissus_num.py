# -*- coding: utf-8 -*-
"""
Created on 19-5-8

@author: zhonguochong

@requirements: PyCharm-2018.3.5; Python3.5.2

@description:
"""

for i in range(999):
    if (i // 100) ** 3 + (i % 100 // 10) ** 3 + (i % 100 % 10) ** 3 == i:
        print(i)
    else:
        continue
