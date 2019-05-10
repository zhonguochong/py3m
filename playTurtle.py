# -*- coding: utf-8 -*-
"""
Created on 19-5-8

@author: zhonguochong

@requirements: PyCharm-2018.3.5; Python3.5.2

@description:
"""
import turtle
import time

# turtle.("fastest")
turtle.pensize(2)
for x in range(100):
    turtle.fd(x*2)
    turtle.left(90)
time.sleep(3)
