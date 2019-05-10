# -*- coding: utf-8 -*-
"""
Created on 19-5-9

@author: zhonguochong

@requirements: PyCharm-2018.3.5; Python3.5.2

@description:
"""
import numpy as np
from sklearn.manifold import TSNE
from sklearn.datasets import load_digits
RS = 20150101
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects
import seaborn as sns
sns.set_style('darkgrid')
sns.set_palette('muted')
sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})
digits = load_digits()
# We first reorder the data points according to the handwritten numbers.
# ###X.shape=[1797,64]  点数1797 维度64
X = np.vstack([digits.data[digits.target==i]for i in range(10)])
# print(X[0])
# ###y.shape=[1797]  点的标签1797
y = np.hstack([digits.target[digits.target==i]for i in range(10)])
# print(y[0])
# ###使用TSNE算法将高维度数据点进行降维处理
# ###X.shape=[1797,64]  降维后为:[1797,2],即digits_proj.shape=[1797,2]
digits_proj = TSNE(random_state=RS).fit_transform(X)


def scatter(x, colors):
    palette = np.array(sns.color_palette("hls", 10))
    f = plt.figure(figsize=(8, 8))
    ax = plt.subplot(aspect='equal')
    sc = ax.scatter(x[:, 0], x[:, 1], lw=0, s=40, c=palette[colors.astype(np.int)])
    plt.xlim(-25, 25)
    plt.ylim(-25, 25)
    ax.axis('off')
    ax.axis('tight')
    txts = []
    for i in range(10):
        xtext, ytext = np.median(x[colors == i, :], axis=0)
        txt = ax.text(xtext, ytext, str(i), fontsize=24)
        txt.set_path_effects([PathEffects.Stroke(linewidth=5, foreground="w"), PathEffects.Normal()])
        txts.append(txt)
    return f, ax, sc, txts


scatter(digits_proj, y)
plt.savefig('digits_tsne-generated.png', dpi=120)
plt.show()
