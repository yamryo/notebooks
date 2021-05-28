#!/usr/bin/env python
# coding: utf-8

# # Permutations on Python

# ## Import libraries

import math
import itertools
import random

import sympy
sympy.init_printing()


# ## Classes

# ### Permutation class

class Permutation:
    '''Permutation class'''

    def __init__(self, image=list(range(4))):
        if not type(image) is list: raise(TypeError)
        try:
            [image.index(v) for v in range(max(image)+1)]
        except:
            print("ArgumentError: ", image)
        self.image = image
        self.size = len(image)
        self.repr = [list(range(self.size)),self.image]
#-----
    def act(self,arg):
        if not type(arg) in [list,int]:
            raise TypeError("type(arg)={}".format(type(arg)))
        if type(arg) is int:
            if arg in self.image:
                return self.image[arg]
            else:
                return arg
        else:
            try:
                return [self.act(v) for v in arg]
            except IndexError as e: print(e)
#-----
    def __mul__(self,aPerm):
        if not isinstance(aPerm, type(self)): raise(TypeError)
        return type(self)(self.act(aPerm.image))

    def inverse(self):
        inverse_image = []
        inverse_image = [self.image.index(v) for v in range(self.size)]
        return type(self)(inverse_image)
#-----
    def __repr__(self):
        return "{}\n{}".format(self.repr[0],self.repr[1])

    def display(self):
        display(sympy.Matrix(self.repr))


# ### Cycle class

class Cycle(Permutation):
    def __init__(self, arg):
        if not type(arg) is list: raise(TypeError)
        self.seq = arg
        self.len = len(arg)
        image = []
        for k in range(max(arg)+1):
            if k in arg:
                ind = arg.index(k)
                image += [arg[(ind+1)%self.len]]
            else:
                image += [k]
        super().__init__(image)

    def __repr__(self):
        return "{}".format(self.seq)

    def repr_as_perm(self):
        return "{}\n{}".format(self.repr[0],self.repr[1])
#        super().__repr__()

    def display(self, flag=False):
        if flag:
            super(Cycle, self).display(self)
        else:
            display(sympy.transpose(sympy.Matrix(self.seq)))


# ### Transposition class

class Transposition(Cycle):
    def __init__(self, i, j):
        self.pair = [i,j]
        super().__init__(self.pair)


# ## Decomposeritions

# ### Decompose into Cycles

def cycle_decomp(aPerm):
    factors = []
    im = [v for v in aPerm.image]  #a deep-copy of aPerm.image
    while len(im) > 0:
        orbit = [im[0]]
        while orbit.count(orbit[0]) == 1:
            current = orbit[-1]
            succ = aPerm.act(current)
            orbit += [succ]
        orbit.pop()
        factors += [Cycle(orbit)]
        im = [v for v in im if not v in orbit]
    return factors
