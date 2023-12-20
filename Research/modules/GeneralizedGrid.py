#!/usr/bin/env python
# coding: utf-8

# # Generarlized grid notation of permutations on Python

# ## Import libraries
import random
import numpy as np
import sympy
# import Permutations as pm
# import math

# ## Classes

class Grid:
    '''Grid notation of a permutation'''
    
    def __init__(self, signlist, perm=pm.Permutation()):
        if not type(perm) is pm.Permutation: raise(TypeError)
        #---
        self.signlist = signlist
        self.permutation = perm
        self.gpm = sympy.diag(*signlist)*perm.matrix()
        self.matrix = self.form_grid(self.gpm)
        self.size = len(self.matrix)
    def __init__(self, mtx):
        if not type(mtx) is list: raise(TypeError)
        #---
        self.original_matrix = mtx
        self.matrix = self.form_grid(mtx)
        self.size = len(self.matrix)
#-----
    def reduce(self, arg_mtx):
        mtx = arg_mtx.copy()
        size = len(mtx)
        for row in range(size-1):
            col = np.where(mtx[row] != 0)[0][0]
            left_up = mtx[row][col]
            if (row < size-1) and (col < size-1):
                right_bottom = mtx[row+1][col+1]
                if right_bottom == left_up:
                    mtx[row][col] += right_bottom
                    mtx = np.delete(mtx, row + 1, 0)
                    mtx = np.delete(mtx, col + 1, 1)
                    break
        return mtx

    def form_grid(self, mtx):
        prev_size = len(mtx)
        while True:
            mtx = self.reduce(mtx)
            if len(mtx) < prev_size:
                prev_size = len(mtx)
            else:
                break
        return mtx
    
    def copy(self):
        return type(self)(self.original_matrix)
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
    def transform(self, bottom_right=False):
        if not self.size > 1: raise(ValueError('The grid size is 1'))
        p = -1 if bottom_right else 0
        #---
        gd = self.matrix.copy()
        num = gd[p][p]
        if num > 0:
            gd = np.delete(np.delete(gd, p, 0), p, 1)
        else:
            a_col = np.where(gd[p] > 0)[0][0]
            a = gd[p][a_col]
            flc = np.array([r[p] for r in gd])
            b_row = np.where(flc > 0)[0][0]
            b = flc[b_row]
            if a > b:
                gd[p][a_col] = a - b
                gd = np.insert(gd, a_col - p, flc, 1)
                gd = np.delete(gd, p, 1)
            elif a < b:
                gd[b_row][p] = b - a
                gd = np.insert(gd, b_row - p, gd[p], 0)
                gd = np.delete(gd, p, 0)
            else:  # a == b  ## trans III
                gd[b_row][a_col] = a
                gd = np.delete(gd, p, 0)
                gd = np.delete(gd, p, 1)
        new_grid = type(self)(restore_permutation(gd))
        direction = "BR" if bottom_right else "TL"
        return {"num": num, "grid": new_grid, "direction": direction}

#-----
    def get_reduction(self):
        grid = self.copy()
        series = [{"num": 0, "grid": grid, "direction": None}]
        while grid.size > 1:
            series.append(grid.transform(random.randint(0,1) == 0))
            grid = series[-1]["grid"]
        return series

#-----
def restore_permutation(gmtx):
    marr = [max(row) for row in gmtx]
    img = []
    for col in np.transpose(gmtx):
        i = np.where(col>0)[0][0]
        num = col[i]
        s = sum(marr[:i])
        img += [s+k for k in range(num)]
    return pm.Permutation(img)
    

###################
### End of File
###################