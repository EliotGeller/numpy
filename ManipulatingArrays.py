#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 14:36:55 2018

@author: eliotgeller
"""

import numpy as np
from time import clock

# Writing an array to file and formatting  
array1 = np.linspace(0, 10, 11, dtype=int)
print(array1)

f = open("TestOutputFile.txt", "w")
array1.tofile(f, sep=", ")
f.close()

testText = "Rainbow"

print("%s %d"%(testText, 5))
print("{1} {0}".format(testText, 5))

print("%5s"%(testText))
print("{:>5}".format(testText))

print("%-5s 5"%(testText))
print("{:<5} 5".format(testText))

#print("%_5s 5"%(testText))
print("{:_<5} 5".format(testText))

print("{:^6} 5".format(testText))

print("%.5s"%(testText))
print("{:.5}".format(testText))

print("%5.6s"%(testText))
print("{:5.6}".format(testText))

print("%0.3d"%(1))
print("{:03d}".format(1))
print()

# Random Numbers
xrand = np.random.rand(3)  #[0,1]
print(xrand)
print()

mu = 100
sigma = 10
standardNormal = np.random.randn(2, 3)
print(sigma*standardNormal + mu)
print()

randInt = np.random.randint(1, 10, size=5)
print(randInt)
print()

randomChoice = np.random.choice(randInt, size=(2, 2), replace=False, 
                                p=[0.0, 0.25, 0.25, 0.25, 0.25])
print(randomChoice)
print()

# Sorting
data = np.random.randint(0, 10000, size=100)
dataCopy = data.copy()
done = False
print(data)
print()

startAlgOne = clock()
while done == False:
    for i in range(len(data)-1):
        if data[i+1] < data[i]:
            temp = data[i]
            data[i] = data[i+1]
            data[i+1] = temp
            break
        elif i == (len(data)-2):
            done = True          
endAlgOne = clock()
print(data)
print()
    
sortedData = np.sort(dataCopy, kind="quicksort") #quicksort, 
                                                #mergesort, heapsort
endAlgTwo = clock()                                                
sortedData = np.sort(dataCopy, kind="mergesort")
endAlgThree = clock()  
sortedData = np.sort(dataCopy, kind="heapsort")                                      
endAlgFour = clock()
print(sortedData)
print()

print("for loop: ", endAlgOne - startAlgOne, "s")
print("quicksort: ", endAlgTwo - endAlgOne, "s")
print("mergesort: ", endAlgThree - endAlgTwo, "s")
print("heapsort: ", endAlgFour - endAlgThree, "s")

























