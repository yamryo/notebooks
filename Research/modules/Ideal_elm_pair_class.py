#!/usr/bin/env python
# coding: utf-8

## Ideal_with_element_class on SageMath

## Import libraries
# import numpy as np
# import math
from sage.all import *

## Classes

### Sp_repr class
class Sp_repr:
    #--- 2x2 ---
    I = identity_matrix(2)
    O = zero_matrix(ZZ,2)
    J = matrix([[0,1],[-1,0]])
    #---
    L = matrix([[1,0],[1,1]])
    K = matrix([[0,-1],[0,0]])
    #--- 4x4 ---
    J4 = block_matrix([[J, O], [O, J]])
    # J4 = J4_bm.subs([(J, evJ)]).as_explicit()
    #---
    CHR_2_MTX = {'a': block_matrix([[L.inverse(), O], [O, I]]),
                 'b': block_matrix([[L.T, K], [K, L.T]]),
                 'c': block_matrix([[I, O], [O, L.inverse()]]),
                 'd': block_matrix([[I, O], [O, L.T]]),
                 'f': block_matrix([[L.T, O], [O,I]])}
    #---
    
    def __init__(self, l:str):
        self.loop = l
        self.matrix = self.CHR_2_MTX.get(l) if l.islower() else self.CHR_2_MTX.get(l.lower()).inverse()

### ideal_elm_pair class
class ideal_elm_pair():
    def __init__(self, M:matrix, root='alpha'):
        self.matrix = M
        self.char_poly = M.charpoly('t')
        self.field = NumberField(self.char_poly, names=root)
        self.root = self.field.gen()
        self.tau = self.field.hom([1/self.root],self.field)
        self.Delta = diff(self.char_poly)(self.root)/self.root
        self.eigen_vector = self.ev()
        self.generator = self.get_gen()
        self.UnitGroup = UnitGroup(self.filed)

    def ev(self):
        X_K = (self.matrix).change_ring(self.field)
        a = self.root
        evlist = X_K.eigenvectors_right()
        vec = [v[1][0] for v in evlist if v[0] == a][0]
        if X_K*vec == a*vec:
            return vec
        else:
            return None

    def get_gen(self):
        v = self.eigen_vector
        tau_v = vector([self.tau(e) for e in v])
        return v.dot_product(J4*tau_v)/self.Delta

    def equiv_check(self, a, b):
        c = a/b
        flag = False
        if c == self.tau(c):
            ########### TODO ##########
            unit_gens = self.UnitGroup.gens_values()
        else:

## Constants
a,b,c,d,f = tuple(map(lambda l: Sp_repr(l).matrix, ['a','b','c','d','f']))
A, B, C, D, F = (k.inverse() for k in [a,b,c,d,f])

J4 = Sp_repr.J4

## Functions
def is_Sp(M):
    J = Sp_repr.J4
    return M.transpose()*J*M == J

def bilinear_form(x, y, A = identity_matrix(ZZ, 4)):
    return x.dot_product(A * y)    

