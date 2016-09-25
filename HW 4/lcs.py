# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 11:59:44 2016

@author: Ankur Dhoot
"""
import numpy as np

def LCS_LENGTH(X, Y) :
    m = len(X)
    n = len(Y)
    
    #two character array
    b = np.empty((m + 1, n + 1), dtype="a2")
    b[:] = " "
    c = np.zeros((m + 1, n + 1))
    
    #initialize first row and column to 0
    for i in range(1, m + 1):
        c[i,0] = 0
    for j in range(0, n + 1):
        c[0,j] = 0
        
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            #pretend indexing is 1 based
            if X[i - 1] == Y[j - 1]:
                c[i, j] = c[i - 1, j - 1] + 1
                b[i, j] = 'lu'
            elif c[i - 1, j] >= c[i, j - 1]:
                c[i, j] = c[i - 1, j]
                b[i, j] = 'u'
            else:
                c[i, j] = c[i, j - 1]
                b[i, j] = 'l'
    print b
    print c
    return b
    
    
def PRINT_LCS(b, X, i, j):
    print "PRINT-LCS called with i = %d and j = %d" %(i,j)
    if i == 0 or j == 0:
        return
    if b[i, j] == 'lu':
        PRINT_LCS(b, X, i - 1, j - 1)
        print X[i - 1]
    elif b[i, j] == 'u':
        PRINT_LCS(b, X, i - 1, j)
    else:
        PRINT_LCS(b, X, i, j - 1)
        
    