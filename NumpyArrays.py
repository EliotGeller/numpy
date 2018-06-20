#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 12:21:33 2018

@author: eliotgeller
"""

import numpy as np

# Creating and reshaping numpy arrays
x = [1, 2, 3, 4]

y=[[1, 2],[3, 4]]

xNp = np.array(x, dtype=complex)

print(x)
print(xNp)
print(xNp.shape)
print()

xReshaped = np.reshape(x, (2, 2))

print(y)
print(xReshaped)
print(xReshaped.shape)
print()

# Creating standard numpy arrays
x = [1, 2, 3]
npEmpty = np.empty((3, 3, 4), dtype=int, order='F')
npEmptyLike = np.empty_like(x, dtype=int)
print(npEmpty)
print()
#print(npEmptyLike)
#print()

npZeros = np.zeros((2, 3, 4), dtype=int)
npZerosLike = np.zeros_like(x)
print(npZeros)
print()
#print(npZerosLike)
#print()

npOnes = np.ones((4, 4, 3), dtype=int)
npOnesLike = np.ones_like(x)
print(npOnes)
print()
#print(npOnesLike)
#print()

npLinSpace = np.linspace(0, 49, 26, endpoint=False, dtype=int) 
#start, stop, num of elements
print(npLinSpace)
print()

# Creating standard 2d arrays
eye = np.eye(5, dtype=int, k=0)
print(eye)
print()

identity = np.identity(4, dtype=int)
print(identity)
print()

diagVal = np.diag(identity)
print(diagVal)
print()

oneDArray = np.array([1, 2, 3, 4])
twoDArray = np.diag(oneDArray, k=1)
print(twoDArray)
print()

# Attributes on numpy arrays
npOnes = np.ones((10, 2, 3))
print(npOnes)
print(npOnes.flags)
print(npOnes.shape)
print(npOnes.strides)
print(npOnes.ndim)
print(npOnes.data)
print(npOnes.size)
print(npOnes.itemsize)
print(npOnes.nbytes)
print()

npLinspace = np.linspace(0, 3, 4)
npDiag = np.diag(npLinspace, k=1)
npDiag2 = npDiag + npDiag*1j
print(npDiag)
print()
print(npDiag.T)
print()
print(npDiag.real)
print()
print(npDiag2)
print()
print(npDiag2.T)
print()
print(npDiag2.real)
print()

# Resizing arrays
aranged = np.arange(8)
resized = np.resize(aranged, (2, 2))
resized2 = np.resize(aranged, (2, 2))
 
cLikeArray = np.array([[0, 1, 2, 3], [4, 5, 6, 7]], order="c")
fLikeArray = np.array([[0, 1, 2, 3], [4, 5, 6, 7]], order="F")

cLikeArray.resize((3, 3))
fLikeArray.resize((3, 3))

print(cLikeArray)
print()
print(fLikeArray)
print()



