# -*- coding: utf-8 -*-
"""
Created on 19-5-10

@author: zhonguochong

@requirements: PyCharm-2018.3.5; Python3.5.2

@description: from http://litaotao.github.io/python-materials
"""
# enumerate
# for i, item in enumerate('abc',1):
#     print(i, item)

# dict && set
# my_dict = {i: i * i for i in range(100)}
# my_set = {i * 15 for i in range(100)}
# print(my_dict)
# print(sorted(my_set))

# reversed string and sequence
a = [i for i in range(10)]
a.reverse()
a = a[::-1]
print(a)
stra = "gnohcougnohz"
stra = stra[::-1]
print(stra)