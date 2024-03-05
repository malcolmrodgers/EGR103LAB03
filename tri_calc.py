#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 19:27:06 2022

@author: malcolmrodgers
"""

#import modules
import numpy as np
import matplotlib.pyplot as plt

#define 'Triangles' function
def triangles( a, b, c, draw=False, fnum=1):
     cosA = ((b*b) + (c*c) - (a*a)) / (2*b*c)
     cosB = ((a*a) + (c*c) - (b*b)) / (2*a*c)
     cosC = ((a*a) + (b*b) - (c*c)) / (2*a*b)
     
     #calculate interior angles
     A = np.arccos(cosA)
     B = np.arccos(cosB)
     C = np.arccos(cosC)
     
     #generate plots if draw=True
     if draw:
         fig = plt.figure(num=fnum, clear=True)
         ax = fig.add_subplot(1, 1, 1)
         
         #h = horizontal distance, v = vertical
         h = b * np.cos(C)
         v = b * np.sin(C)
         
         x = [0, a, (a-h), 0]
         y = [0, 0, v, 0]
         
         ax.plot(x, y, '-')
         ax.set(title = "Triangle (mlr81)")
         ax.axis("equal")
         fig.tight_layout()
         
         #return angles
         return A, B, C
     
if __name__ == "__main__":
    print(triangles(3, 6, 4, True, 5))