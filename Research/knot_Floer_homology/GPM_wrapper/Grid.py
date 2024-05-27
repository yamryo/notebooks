#!/opt/anaconda3/bin python3
# coding: utf-8

import sys; sys.path.append("../modules")
import Permutation as pm
from GridPythonModule import *

from itertools import product
import numpy as np

### Classes wrapping functions in GridPythonModule
class Edge:
    '''Edge class expressing edges in a grid diagram.'''
    def __init__(self, hv, index, xoends):
        self.hv = hv
        self.index = index
        self.xoends = xoends
        self.xend, self.oend = xoends
        self.direction = 1 if not (self.xend < self.oend)^(self.hv == 'h') else -1

    def __repr__(self):
        return f"{self.hv}{self.index}" #{self.xoends}"
        
    def __str__(self):
        return f"{self.hv}{self.index}({self.xend},{self.oend})"

class Crossing:
    def __init__(self, hedge, vedge):
        self.hedge, self.vedge = hedge, vedge
        self.sign = self.get_sign()
        self.index = (hedge.index, vedge.index)
        
    def get_sign(self):
        signs = [-1]
        he, ve = self.hedge, self.vedge
        for e, i in [(he, ve.index), (ve, he.index)]:
            e.sorted_end = e.xoends if e.xend < e.oend else e.xoends[::-1]
            sign = e.direction if e.sorted_end[0] < i < e.sorted_end[1] else 0
            signs.append(sign)
        return np.prod(signs)

    def __eq__(self, other_cr):
        return other_cr == self.index

    def __repr__(self):
        return f"x({self.hedge.index},{self.vedge.index})"

class Grid:
    def __init__(self, xlist, olist):
        self.orig = [xlist, olist]
        self.size = len(xlist)
        self.xprm, self.oprm = pm.Permutation(xlist), pm.Permutation(olist)
        self.hedges = [Edge('h', i, (self.xprm.act(i), self.oprm.act(i))) for i in range(self.size)]
        self.vedges = [Edge('v', i, (self.xprm.inverse().act(i), self.oprm.inverse().act(i))) for i in range(self.size)]
        self.crossings = self.get_crossings()
        
    def get_crossings(self):
        crossings = []
        for he, ve in product(self.hedges, self.vedges):
            if not (he.index in [0, self.size-1] or ve.index in [0, self.size-1]):
                cr = Crossing(he, ve)
                crossings.append(cr) if not cr.sign == 0 else None
        return crossings

    def draw(self):
        draw_grid(self.orig, markings='XO')

    def num_of_comps(self):
        number_of_components(self.orig)

    def edge_trace(self):
        et = [self.hedges[0]]
        closed = False
        while not closed:
            et.append(self.vedges[et[-1].oend])
            et.append(self.hedges[et[-1].xend])
            if et[-1] == et[0]:
                closed = True
        del et[-1]
        return et

    def get_PD(self):
        if len(self.crossings) == 0:
            return []
        else:
            dummy_cr = Crossing(self.hedges[0], self.vedges[0])
            et, et_divided = self.edge_trace(), []
         
            et_divided.append([(et[-1], dummy_cr)])
            for e in et:
                et_divided[-1].append((e, dummy_cr))
                e_div = []
                for cr in self.crossings:
                    if e in [cr.hedge, cr.vedge]:
                        e_div.append([(e, cr)])
                et_divided += e_div[::e.direction]
                    
#            for i, l in enumerate(et_divided):
#                print(f"{i}: {l}\n")
        
            modulo = len(et_divided) - 1
            cr_data = [{'cr': x, 'h-dir': None, 'code': {'w': None, 'n': None, 'e': None, 's': None}} for x in self.crossings]
            for i, l in enumerate(et_divided):
                nums = ((i-1)%modulo, i%modulo)
                e, x = l[0]
                for d in cr_data:
                    if d['cr'] == x:
                        if e.hv == 'h':
                            d['code']['e'], d['code']['w'] = nums[::e.direction]
                            d['h-dir'] = e.direction
                        else:
                            d['code']['n'], d['code']['s'] = nums[::e.direction]
            PD = []
            for d in cr_data:
                w, n, e, s = d['code']['w'], d['code']['n'], d['code']['e'], d['code']['s']
                code = [w,s,e,n] if d['h-dir'] == -1 else [e,n,w,s]
                PD.append(code)
            return reduce(PD)
#-----------------------------
def reduce_once(PD):
    for i, l in enumerate(PD):
        if len(set(l)) < len(l):
            pair = [v for v in l if l.count(v) == 1]
            del PD[i]
            PD = [list(map(lambda x: min(pair) if x==max(pair) else x, l)) for l in PD]
            break
    return PD

def reduce(PD):
    prev = len(PD)
    flag = True
    while flag and prev > 0:
        PD = reduce_once(PD)
        if len(PD) == prev:
            flag = False
        else:
            prev = len(PD)
    flatten = list(set(sum(PD, [])))
    return [list(map(lambda x: flatten.index(x), l)) for l in PD]