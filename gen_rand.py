#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 19:52:53 2022

@author: malcolmrodgers
"""

#import modules
import numpy as np
import matplotlib.pyplot as plt
import math as m

#seed based on NetID
NetID = input("NetID = ")
seed = 0
for code in map(ord, NetID):
    seed = seed + code
    
np.random.seed(seed)

#user inputs desired # of numbers
nums = int(input("how many numbers? "))

#distribution calculations
ud = np.random.uniform(0, 1, size = nums)
nd = np.random.normal(0, 1, size = nums)

#generate plots
num_bins = m.ceil(10 * m.log10(nums))

fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1, 1, 1)
ax.hist(ud, num_bins)
ax.set(title="Uniform")
fig.tight_layout()
fig.savefig("Figures/UniformPlot.png")

fig = plt.figure(num=2, clear=True)
ax = fig.add_subplot(1, 1, 1)
ax.hist(nd, num_bins)
ax.set(title="Normal")
fig.tight_layout()
fig.savefig("Figures/NormalPlot.png")

#print statistics
a = np.min(ud)
b = np.mean(ud)
c = np.max(ud)

d = np.min(nd)
e = np.mean(nd)
f = np.max(nd)

print("Min: {:+.3e}".format(a), "Avg: {:+.3e}".format(b), "Max: {:+.3e}".format(c))
print("Min: {:+.3e}".format(d), "Avg: {:+.3e}".format(e), "Max: {:+.3e}".format(f))
