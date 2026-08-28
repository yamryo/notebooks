#!/usr/bin/env python
# coding: utf-8

## Symplectic representation for mapping classes

## Import libraries
# import numpy as np
# import math
import sympy as sp
# import itertools
# import functools

## Classes

### Sp_representation class
class Sp_representation():
    #--- 2x2 ---
    I = sp.Identity(2)
    O = sp.ZeroMatrix(2,2)
    J, evJ = sp.MatrixSymbol('J',2,2), sp.Matrix([[0,1],[-1,0]])
    #---
    L, evL = sp.MatrixSymbol('L',2,2), sp.Matrix([[1,0],[1,1]])
    K, evK = sp.MatrixSymbol('K',2,2), sp.Matrix([[0,-1],[0,0]])
    #--- 4x4 ---
    J4_bm = sp.BlockMatrix([[J, O], [O, J]])
    J4 = J4_bm.subs([(J, evJ)]).as_explicit()
    #---
    # CHR_2_MTX = {'a': sp.BlockMatrix([[L.inv(), O], [O, I]]),
    #              'b': sp.BlockMatrix([[L.transpose(), K], [K, L.transpose()]]),
    #              'c': sp.BlockMatrix([[I, O], [O, L.inv()]]),
    #              'd': sp.BlockMatrix([[I, O], [O, L.transpose()]]),
    #              'f': sp.BlockMatrix([[L.transpose(), O], [O,I]])}
    CHR_2_MTX = {'a': sp.BlockMatrix([[L.inv(), O], [O, I]]),
                 'b': sp.BlockMatrix([[L.transpose(), K], [K, L.transpose()]]),
                 'c': sp.BlockMatrix([[I, O], [O, L.inv()]]),
                 'd': sp.BlockMatrix([[I, O], [O, L.transpose()]]),
                 'f': sp.BlockMatrix([[L.transpose(), O], [O,I]])}
    #---
    
    def __init__(self, l:str):
        self.loop = l
        self.block_matrix = self.CHR_2_MTX.get(l) if l.islower() else self.CHR_2_MTX.get(l.lower()).inv()
        self.matrix = self.block_matrix.subs([
            (self.L, self.evL), (self.K, self.evK) #, (self.tl, self.evtl), (self.br, self.evbr)
        ]).as_explicit()

## Constants
a,b,c,d,f = tuple(map(lambda l: Sp_representation(l).matrix, ['a','b','c','d','f']))
A, B, C, D, F = (k.inverse() for k in [a,b,c,d,f])

e, E = d, D

J4 = Sp_representation.J4

## Functions
def rho2(monod:str):
    return eval("*".join(monod))
    
def is_Sp(M):
    return M.transpose()*J4*M == J4

def char_poly(M):
    return M.charpoly().as_expr().factor()

def conjugate_check(m1, m2, rng=10):
    if char_poly(m1) == char_poly(m2):
        return "They are possiblly conjugate"
    else: 
        return "Not conjugate. (Different Alex. ploy.'s)"
