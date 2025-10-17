#!/usr/bin/env python
# coding: utf-8

## Ideal_wrt_monodromy_class on SageMath

## Import libraries
# import numpy as np
# import math
from sage.all import *
import itertools
import functools

## Classes

### Sp_representation class
class Sp_representation():
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

### ideal class
class ideal():
    def __init__(self, monodromy:str):
        self.matrix = eval('*'.join(monodromy))
        self.char_poly = self.matrix.charpoly('t')
        try:
            self.field = NumberField(self.char_poly, names=('alpha'))
            self.UnitGroup = UnitGroup(self.field)
            self.root = self.field.gen()
            self.tau = self.field.hom([1/(self.root)],self.field)
            self.Delta = diff(self.char_poly)(self.root)/self.root
            self.eigen_vector = self.get_ev()
            self.generator = self.get_gen()
        except ValueError as e: #NotImplementedError as e:
            print(e, f",  Char_poly = {self.char_poly.factor()}")
        
    def get_ev(self):
        X_K = (self.matrix).change_ring(self.field)
        rt = self.root
        evlist = X_K.eigenvectors_right()
        vec = [v[1][0] for v in evlist if v[0] == rt][0]
        if X_K*vec == rt*vec:
            denom = vec[1].denominator()
            if not denom == 1:
                vec = denom*vec
            return vec
        else:
            return None

    def get_gen(self):
        v = self.eigen_vector
        tau_v = vector([self.tau(e) for e in v])
        return v.dot_product(J4*tau_v)/self.Delta

    def _compare_tuples(self, a,b):
        absed = [list(map(lambda x: abs(x), t)) for t in [a,b]]
        sums = [functools.reduce(lambda x,y: x+y, t) for t in absed]
        (A, B) = (b, a) if sums[0] == sums[1] else (sums[0], sums[1])
        if A > B: 
            return 1
        elif A < B: 
            return -1
        else: 
            return 0
        
    def equiv_rel(self, another_generator, rng=10):
        c = self.generator/another_generator
        flag = 0
        if c == self.tau(c):
            unit_gens = self.UnitGroup.gens_values()
            r = len(unit_gens)
            signs = sorted(list(itertools.product(range(-1,2), repeat=r)), key=functools.cmp_to_key(self._compare_tuples))
            #---
            for ids in itertools.product(range(rng+1), repeat=r):
                for s in signs:
                    factors = [unit_gens[i]**(s[i]*ids[i]) for i in range(r)]
                    u = functools.reduce(lambda x,y: x*y, factors)
                    if u*(self.tau(u)) == c: 
                        flag = [ids, u]
                        break
                if flag: break
        else: flag = -1
        return flag

## Constants
a,b,c,d,f = tuple(map(lambda l: Sp_representation(l).matrix, ['a','b','c','d','f']))
A, B, C, D, F = (k.inverse() for k in [a,b,c,d,f])

e, E = d, D

J4 = Sp_representation.J4

## Functions
def is_Sp(M):
    return M.transpose()*J4*M == J4

def conjugate_check(m1, m2, rng=10):
    i, j = ideal(m1), ideal(m2)
    if i.char_poly == j.char_poly:
        rel_value = i.equiv_rel(j.generator, rng)
        return rel_value if rel_value else "Possiblly not conjugate"
    else: return "Not conjugate. (Different Alex. ploy.'s)"
