#!/usr/bin/env python
# coding: utf-8

# # Permutation on Python

# ## Import libraries
import numpy as np
# import math

# ## Classes

# ### Permutation class

class Permutation:
    '''Permutation class'''

    def __init__(self, image=list(range(4))):
        if not type(image) is list: raise(TypeError)
        try:
            [image.index(v) for v in range(max(image)+1)]
        except:
            print(f"ArgumentError: {image} is a wrong image")
        self.image = image
        self.size = len(image)
#-----
    def act(self,arg):
        if type(arg) in {int, np.int64}:
            return self.image[arg] if arg in self.image else arg
        elif type(arg) is list:
            try:
                return [self.act(v) for v in arg]
            except IndexError as e: print(e)
        else: raise TypeError("type(arg)={}".format(type(arg)))
#-----
    def __mul__(self,aPerm):
        if not isinstance(aPerm, type(self)): raise(TypeError)
        return type(self)(self.act(aPerm.image))

    def inverse(self):
        inverse_image = []
        inverse_image = [self.image.index(v) for v in range(self.size)]
        return type(self)(inverse_image)
#-----
    def two_line(self):
        return [list(range(self.size)),self.image]

    def matrix(self):
        M = np.zeros((self.size,self.size), dtype=int)
        # for column in range(self.size):
        #     M[self.act(column)][column] = 1
        for row in range(self.size):
            M[row][self.act(row)] = 1
        return M
        
    def __repr__(self):
        mat = self.two_line()
        return "{}\n{}".format(mat[0],mat[1])


# ### Cycle class

class Cycle(Permutation):
    def __init__(self, arg, num_of_elements = None):
        if not type(arg) is list: raise(TypeError)
        self.seq = arg
        self.len = len(arg)
        M = max(arg)+1 if num_of_elements is None else num_of_elements
        image = []
        for k in range(M):
            if k in arg:
                ind = arg.index(k)
                image += [arg[(ind+1)%self.len]]
            else:
                image += [k]
        super().__init__(image)
    
    def __mul__(self, aPerm):
        return Permutation(self.act(aPerm.image))
    
    def __repr__(self):
        return "{}".format(self.seq)
    
    def len(self):
        return len(self.seq)
#---
Perm = Permutation

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
    
###################
### End of File
###################