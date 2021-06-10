#!/usr/bin/env python
# coding: utf-8

# # Incidence Matrices for quasi-cords

# ## Import modules

import numpy as np
import plotly.graph_objects as go

#--- import original modules ---
from Permutations import Permutation


# ## Classes and functions

# ### Code class

LABELS = ['T','L','B','R']

class Code(tuple):
    '''
    4-tuple of integers representing a quasi-cord.
    4 integers T,L,B and R have the following rule;

    1) T+L >= B+R
    2) T <= L+B+R+1
    3) L <= T+B+R
    '''
    def __init__(self, arg):
        self.verify_code(arg)
        self = tuple(arg)
        
    def verify_code(self, code):
        if not type(code) in [list,tuple]: raise TypeError("Not list or tuple.")
        if len(code) != 4: raise ValueError("Not a 4-tuple.")
        for v in code:
            if not type(v) is int: ValueError("Not integers.")
            if v < 0: raise ValueError("Not positive values.")  
        tl = sum(code[:2])
        br = sum(code[-2:])
        if tl < br:
            raise ValueError("T+L < B+R")
        elif code[0] > code[1] + br+1:
            raise ValueError("T > L+B+R+1")
        elif code[1] > code[0] + br:
            raise ValueError("L > T+B+R")
        else: 
            return True


# ### Side class, Segment class

class Side:
    '''A side of the square'''
    
    def __init__(self, label, number):
        '''
        Arguments
        ---------
        label : string
            One of the letters in {T,L,B,R}.
        number : int
            The number coressponding to the points on the side of the label.
        '''
        self.label = label
        self.number = number
        self.points = self.get_points()
        
    def get_points(self):
        points = [self.label+str(k)+'+' for k in range(self.number)]
        points += [label[:-1]+'-' for label in reversed(points)]
        if self.label in ['L','R']:
            idx = int(len(points)/2)
            points.insert(idx, self.label)
        return points

class Segment:
    '''A segment on the square connecting two points on the sides'''
    
    def __init__(self, point01, point02):
        '''
        Arguments
        ---------
        point01, point02 : string
            The labels of the two points on the sides.
        '''
        self.ends = (point01, point02)
        
    def show(self):
        return self.ends


# ### Square class

class Square:
    '''A square obtained by cut the disk with 4 points T,L,B,R along the arcs a_T, a_L, a_B, a_R'''
    
    def __init__(self, arg):
        '''
        Arguments
        ---------
        code : tuple
            The 4-tuple corresponding to the quasi-cord.
        '''
        #---
        self.code = Code(arg)                 # tuple: code = (\d, \d, \d, \d)
        self.sides = self.get_sides()         # dict: sides = {label: Side(label, num),...}
        self.segments = self.get_segments()   # list: segments = [Segment,...]
   
    def get_sides(self):
        sides_dict = {}
        for i in range(len(LABELS)):
            sides_dict[LABELS[i]] = Side(LABELS[i], self.code[i])
        return sides_dict

    def get_segments(self):
        segs_list = []
        
        # create the top-left segments 
        tl = self.sides['T'].number + self.sides['L'].number
        br = self.sides['B'].number + self.sides['R'].number
        diff = tl - br
        for i in range(diff):
            a_tlseg = Segment(self.sides['T'].points[i], self.sides['L'].points[i])
            segs_list.append(a_tlseg)
        
        # the remaining
        remaining = []
        TL_points = list(reversed(self.sides['L'].points[diff:]))+self.sides['T'].points[diff:]
        BR_points = self.sides['B'].points+self.sides['R'].points

        for i in range(len(TL_points)):
            a_seg = Segment(TL_points[i], BR_points[i])
            segs_list.append(a_seg)
        return segs_list
    
    def matrix(self):
        variables = []
        for label in LABELS:
            num = self.sides[label].number
            if label in ['L','R']:
                num += 1
            variables.append(self.sides[label].points[:num])
        variables = [v.replace('+','') for v in sum(variables, [])] # flatten and remove '+'
        #---
        s = len(self.segments)
        M = np.zeros((s,s+1), dtype=int)
        raw = 0
        for a_seg in self.segments:
            i = 0
            for end_point in a_seg.ends:
                if end_point[-1] in ['+','-']:
                    end_point = end_point[:-1]  # remove '+' and '-'
                M[raw][variables.index(end_point)] = (-1)**i
                i += 1
            raw += 1

        tl = self.sides['T'].number + self.sides['L'].number
        C = np.roll(np.eye(1, s+1, dtype=int), shift=tl, axis=1)
        M = np.r_[M, C]
        return M

    def grid_diagram(self):
        M = self.matrix()
        size = len(M)
        #--- Initialize Grid diagram matrix ---
        GM = np.where(M!=0, 2, M)
        GM[size-1][size-1] = 2
        #-----
        rows = list(range(size))
        next_row = []
        #-----
        while len(rows) > 0:
            if len(next_row) == 1:
                o_column = x_column
                current_row = next_row[0]
                rows.remove(current_row)
            elif len(next_row) == 0:
                o_column = -1
                current_row = rows.pop()
            else: raise ValueError("next_row = {} (rows = {})".format(next_row,rows))
            marking_columns = np.where(GM[current_row]==2)[0]
            if len(marking_columns) != 2:
                raise ValueError("marking_columns = {} (rows = {})".format(marking_columns,rows))
            if o_column >= 0:
                another = np.where(marking_columns!=o_column)[0][0]
                x_column = marking_columns[another]
            elif o_column == -1:
                o_column = marking_columns[0]
                x_column = marking_columns[1]
            else:
                raise ValueError("marking_columns = {} (rows = {})".format(marking_columns,rows))
            GM[current_row][o_column] = 1
            GM[current_row][x_column] = -1
            #---
            next_row = np.where(GM[:,x_column]==2)[0]
        return GM
    
    def permutation(self):
        GM = self.grid_diagram()
        entry = np.nditer(GM, flags=['multi_index'])
        sO, sX = [], []
        while not entry.finished:  
            idx = entry.multi_index
            if GM[idx] != 0:
                if GM[idx] == 1:
                    sO += [idx[1]]
                else:
                    sX += [idx[1]]
            entry.iternext()
        #---
        sigma_O = Permutation(sO)
        sigma_X = Permutation(sX)
        return sigma_O*(sigma_X.inverse())

    def graphic(self, figsize=(400, 400)):
        fig = go.Figure()
        SIZE = 10
    
        #--- Points
        moves = {'T': (1, SIZE*1j), 'L': (-1j, SIZE*(-1)), 'B': (1, SIZE*1j*(-1)), 'R': (1j, SIZE)}
        all_points_dict = {}
        for side in self.sides.values():
            num = side.number
            delta = SIZE/(num+1)
            #---
            complex_list = list(reversed([(-1)*delta*(k+1) for k in range(num)]))
            if side.label in ['L', 'R']:
                complex_list.append(0)
            complex_list += [delta*(k+1) for k in range(num)]
            complex_list = [v*moves[side.label][0]+moves[side.label][1] for v in complex_list]
            for k in range(len(side.points)):
                all_points_dict[side.points[k]] = complex_list[k]
            #---
            fig.add_trace(go.Scatter(
                x = [z.real for z in complex_list],
                y = [z.imag for z in complex_list],
                mode="markers",
            ))
     
        #--- Frame
        frame = go.layout.Shape(
                    type="rect",
                    x0=SIZE, y0=SIZE, x1=(-1)*SIZE, y1=(-1)*SIZE,
                    line=dict(color="RoyalBlue",),
                )
        #--- Segments
        my_shapes = [frame]
        for seg in self.segments:
            pnt0 = all_points_dict[seg.ends[0]]
            pnt1 = all_points_dict[seg.ends[1]]
            my_shapes.append(
                go.layout.Shape(
                    type="line",
                    x0=pnt0.real, y0=pnt0.imag,
                    x1=pnt1.real, y1=pnt1.imag,
                    line=dict(
                        color="LightSeaGreen",
                        width=3,
                    ),
                )
            )
        else: fig.update_layout(shapes=my_shapes)
     
        #--- Update axes properties
        rng = SIZE*1.2
        options = dict(range=[(-1)*rng, rng], showticklabels=False, showgrid=False, zeroline=False,)
        fig.update_xaxes(options)
        fig.update_yaxes(options)
        #--- Set figure size and background color
        fig.update_layout(width=figsize[0], height=figsize[1], plot_bgcolor="white", showlegend=False)
        
        return fig


# Functions

### get_diagram function

def get_diagram(matrix, figsize=(400,400)):
    fig = go.Figure()
    SIZE = 10
    delta = SIZE/len(matrix)

    def trans(pair):
        return (pair[1] - pair[0]*1j)*delta +(3/2+1/2*1j)*delta + SIZE*1j
    
    #--- Points ---
    corners = dict(points=[], marker=dict(size=5.0, color="Red"),)
    others = dict(points=[], marker=dict(size=2.0, color="RoyalBlue"),)

    entry = np.nditer(matrix, flags=['multi_index'])
    while not entry.finished:
        if entry[0]==0:
            others['points'].append(entry.multi_index)
        else:
            corners['points'].append(entry.multi_index)
        entry.iternext()

    for pdict in [others, corners]:
        z_list = [trans(pair) for pair in pdict['points']]
        fig.add_trace(go.Scatter(
            x = [z.real for z in z_list],
            y = [z.imag for z in z_list],
            mode="markers",
            marker=pdict['marker'],
        ))

    #--- Lines ---
    lines = []
    for k in range(len(matrix)):
        for i in range(2):  # 0: horizontal lines, 1: vertical lines
            z = [trans(pair) for pair in corners['points'] if pair[i] == k]
            if len(z) == 2:
                lines.append(
                    go.layout.Shape(
                        type="line",
                        x0=z[0].real, y0=z[0].imag,
                        x1=z[1].real, y1=z[1].imag,
                        line=dict(color="LightSeaGreen", width=1,),
                    ))
    else: fig.update_layout(shapes=lines)
               
    #--- Update axes properties
    options = dict(
        range=[0, SIZE+2*delta], 
        showticklabels=False,
        showgrid=False,
        zeroline=False,
    )
    fig.update_xaxes(options)
    fig.update_yaxes(options)
    #--- Set figure size and background color
    fig.update_layout(
        width=figsize[0], height=figsize[1],
    #     plot_bgcolor="white", 
        showlegend=False,
    )
    #---
    return fig


# ### square_random_generator function

def square_random_generator(max=10, verbose=False):
    while True:
        try:
            code = [np.random.randint(1,max) for k in range(4)]
            sqr = Square(tuple(code))
            break
        except ValueError as e:
            if verbose:
                print(f"Oops! [code={code}], {e}")
    return sqr

# ### count_number_of_components function

def cc(sqr):
    """Return the number of components of the quasi-cord associated with a given Square"""
    return len(pm.cycle_decomp(sqr.permutation()))

##################
### End of File
##################