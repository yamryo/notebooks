#!/usr/bin/env python
# coding: utf-8

# # Grid notation of permutations on Python

# ## Import libraries
import random
import numpy as np
import Permutations as pm
# import math

# ## Classes

class Grid:
    '''Grid notation of permutations'''
    
    def __init__(self, perm=pm.Permutation()):
        if not type(perm) is pm.Permutation: raise(TypeError)
        #---
        self.permutation = perm
        self.matrix = self.form_grid(perm.matrix())
        self.size = len(self.matrix)
#-----
    def reduce(self,pm):
        mtx = pm.copy()
        size = len(mtx)
        for row in range(len(mtx)-1):
            col = np.where(mtx[row] > 0)[0][0]
            if (row < size-1) and (col < size-1):
                rb_num = mtx[row+1][col+1]
                if rb_num > 0:
                    mtx[row][col] += rb_num
                    mtx = np.delete(mtx, row + 1, 0)
                    mtx = np.delete(mtx, col + 1, 1)
                    break
        return mtx

    def form_grid(self,pm):
        mtx = pm.copy()
        prev_size = len(mtx)
        while True:
            mtx = self.reduce(mtx)
            if len(mtx) < prev_size:
                prev_size = len(mtx)
            else:
                break
        return mtx
    
    def to_permutation(self,gmtx):
        marr = [max(row) for row in gmtx]
        img = []
        for col in np.transpose(gmtx):
            i = np.where(col>0)[0][0]
            num = col[i]
            s = sum(marr[:i])
            img += [s+k for k in range(num)]
        return pm.Permutation(img)
    
    def copy(self):
        return type(self)(self.permutation)
#-----
    def show(self):
        hline, vline = "+---" * self.size + "+", "|   " * self.size + "|"
        for row in self.matrix:
            idx = np.where(row > 0)[0][0]
            print(
                hline
                + "\n"
                + vline[: 4 * idx + 2]
                + "{}".format(row[idx])
                + vline[4 * (idx + 1) - 1 :]
            )
        else: print(hline)
#-----
    def transform(self):
        gd = self.matrix.copy()
        if gd[0][0] > 0:
            num = gd[0][0]
            gd = np.delete(np.delete(gd, 0, 0), 0, 1)
            # print("Decompose into {} + the remaining grid".format(num))
            rtn = {"num": num, "grid": type(self)(self.to_permutation(gd))}
        else:
            a_col = np.where(gd[0] > 0)[0][0]
            a = gd[0][a_col]
            fc = np.array([r[0] for r in gd])
            b_row = np.where(fc > 0)[0][0]
            b = fc[b_row]
            if a > b:
                gd[0][a_col] = a - b
                gd = np.insert(gd, a_col, fc, 1)
                gd = np.delete(gd, 0, 1)
            elif a < b:
                gd[b_row][0] = b - a
                gd = np.insert(gd, b_row, gd[0], 0)
                gd = np.delete(gd, 0, 0)
            else:  # a == b  ## trans III
                gd[b_row][a_col] = a
                gd = np.delete(gd, 0, 0)
                gd = np.delete(gd, 0, 1)
            rtn = type(self)(self.to_permutation(gd))
        return rtn

###################
### End of File
###################