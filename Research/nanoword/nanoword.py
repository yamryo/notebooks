#!/usr/bin/env python
# coding: utf-8

# # Importing modules

import math
import numpy as np
import random

import itertools
from typing import Literal
import plotly.graph_objects as go

# # Nanoword Class and other supporting classes

# ## Sign class

class Sign(str):
    LABELS_ab = ['a', 'b']  # the second strand in a crossing is going (a) up and (b) down.
    LABELS_pm = ['+', '-']  # the sign of a crossing
    LABELS = [''.join(t) for t in itertools.product(LABELS_ab, LABELS_pm)]
            # = ['a+', 'a-', 'b+', 'b-']
    R = {'a': set(['a+', 'b-']), 'b': set(['b+', 'a-'])}
    
    def __new__(cls, s: Literal['a+', 'a-', 'b+', 'b-']):
        if not s in cls.LABELS: raise ValueError(f"{s} is not in {cls.LABELS}")
        self = super().__new__(cls, s)
        return self

    def __init__(self, s: str):
        self.pm: int = 1 if '+' in self else -1
        self.ab: Literal['a', 'b'] = 'a' if 'a' in self else 'b'
        self.gen: Literal['a', 'b'] = 'a' if self in self.R['a'] else 'b'
    #---
    def tau(self):
        return type(self)((self.R[self.gen] - {self}).pop())

    def iota(self):
        result = self.replace('+', '-') if self.pm == 1 else self.replace('-', '+')
        return type(self)(result)
    #---    
    @classmethod
    def asterisk(cls, signA, signB) -> int:
        return 0 if signB in cls.R[signA.gen] else 1


# ## Letter class

class Letter:
    ALL_CHARS = [chr(i) for i in range(ord('A'), ord('Z')+1)]

    def __init__(self, char: str, sign: Sign | str) -> None:
        if type(char) is not str or not len(char) == 1: raise ValueError(f"{char} is not a letter")
        self.char = char
        self.sign = sign if isinstance(sign, Sign) else Sign(sign)
    
    def __eq__(self, other) -> bool:
        if type(other) is not type(self): raise ValueError(f"{other} is not a letter")
        return True if (self.char == other.char and self.sign == self.sign) else False        

    def __str__(self) -> str:
        return f"{self.char}, {self.sign}"
    
    def __repr__(self) -> str:
        return f"({self.char},{self.sign})"


# ## Nanoword class

class Nanoword:
    def __init__(self, word: str, alphabet: list[Letter]) -> None:
        '''
        word <-- a Gauss-word on alphabet
        alphabet <-- a list of letters
        '''
        self.word: str = word
        self.size: int = len(word)
        self.alphabet: list[Letter] = alphabet
        self.chars: list[str] = [l.char for l in self.alphabet]
        self.validation_check()

    def validation_check(self) -> None:
        if not self.is_gauss_word(): raise ValueError(f"{self.word} is not a Gauss word.")
        if not set(self.chars) == set(self.word): 
            raise ValueError(f"The charactors in the alphabet: {self.chars} does not match with the word {self.word}")
        
    def is_gauss_word(self) -> bool:
        '''
        Check the word is a Gauss word or not.
        '''
        return all([(self.word.count(char)==2) for char in self.word])
    #---        
    @classmethod
    def random_generator(cls, num_of_crossings: int = 3):
        if num_of_crossings > 26: raise ValueError(f"{num_of_crossings} must be less than or equal to 26")
        chars = Letter.ALL_CHARS[:num_of_crossings]
        word = ''.join(random.sample(chars+chars, 2*len(chars)))
        labels = random.choices(Sign.LABELS, k=num_of_crossings)
        alph = [Letter(c, s) for c, s in zip(chars, labels)]
        return cls(word, alph)
    #---
    def __str__(self) -> str:
        return self.word
    
    def __eq__(self, other) -> bool:
        if len(self.alphabet) == len(other.alphabet):
            result = all([(l in other.alphabet) for l in self.alphabet])
        else:
            result = False
        return self.word == other.word and result

    def diagram(self, size: int = 400) -> go.Figure:
        fig = go.Figure()
        w = 1.6
        fig.update_xaxes(range=[-w, w], showgrid=False, showticklabels=False, zeroline=False)
        fig.update_yaxes(range=[-w, w], showgrid=False, showticklabels=False)
        fig.update_layout(plot_bgcolor="white", margin=dict(t=0, b=0, l=1.0, r=1.0))
        # Set figure size
        fig.update_layout(width=size, height=size)
        #-- End points of chords --
        s = int(self.size/2)
        points_data = []
        for i, c in enumerate(self.word):
            points_data.append({'letter': [l for l in self.alphabet if l.char == c].pop(), 
                                'coord': (math.cos(i*math.pi/s), math.sin(i*math.pi/s))})
        fig.add_trace(go.Scatter(
            x = [p['coord'][0] for p in points_data],
            y = [p['coord'][1] for p in points_data],
            mode="markers", marker=dict(size=8.0, color="RoyalBlue"), showlegend=False,
        ))
        def margin(coord: tuple):
            r = math.sqrt(coord[0]**2 + coord[1]**2)
            length = 0.3 if size > 200 else 0.35
            return tuple((v/r)*length for v in coord)
        fig.add_trace(go.Scatter(
            x = [p['coord'][0]+margin(p['coord'])[0] for p in points_data],
            y = [p['coord'][1]+margin(p['coord'])[1] for p in points_data],
            mode="text", text=[p['letter'] for p in points_data], showlegend=False,
        ))
        #-- Chords --
        chords = []
        for ltr in self.alphabet:
            coords = [p['coord'] for p in points_data if p['letter'] == ltr]
            chords.append(dict(type="path",
                              path="M {},{} Q 0,0 {},{}".format(
                                  coords[0][0],coords[0][1],coords[1][0], coords[1][1]),
                              line_color="orange",))
        else: fig.update_layout(shapes=chords)
        #-- The start point --
        posi = 0.35
        fig.add_trace(go.Scatter(
            x = [math.cos((-posi)*math.pi/s)], y = [math.sin((-posi)*math.pi/s)],
            mode="markers", marker=dict(size=12.0, symbol="arrow", angle=(180/s)*posi*1.1, color="LightSeaGreen"), showlegend=False,
        ))
        #-- The big circle --
        fig.add_shape(type="circle",
                      xref="x", yref="y",
                      x0=-1.0, y0=-1.0, x1=1.0, y1=1.0,
                      line_color="LightSeaGreen",)
        return fig

    #--- Building an invariant ---#
    def n(self, ltrA: Letter):
        A = ltrA.char
        def func(ltrB: Letter) -> Sign:
            result = ltrB.sign
            B = ltrB.char
            arr = self.arrangement(ltrA, ltrB)
            if arr == 1:
                result = ltrB.sign
            elif arr == -1:
                result = ltrB.sign.tau()
            else:
                result = None
            return result
        return func
        
    def self_linking_original(self, ltrA:Letter) -> dict[str, int, str, int]:
        result_signs = []
        for ltrB in self.alphabet:
            result = self.n(ltrA)(ltrB)
            if result is not None:
                if Sign.asterisk(ltrA.sign, ltrB.sign) == 1:
                    result = result.iota()
                result_signs.append(result)
        result_dict = {'R(a)': 0, 'R(b)': 0}
        for s in result_signs:
            if result is not None:
                result_dict[f"R({s.gen})"] += s.pm
        return result_dict

    def section_original(self, sign:Sign) -> list[dict]:
        result_list = []
        for ltr in self.alphabet:
            if ltr.sign == sign:
                sl = self.self_linking_original(ltr)
                if not (sl['R(a)'] == 0 and sl['R(b)'] == 0):
                    result_list.append(sl)
        return result_list
        
    #---
    def arrangement(self, ltrA: Letter, ltrB: Letter) -> int:
        A, B = ltrA.char, ltrB.char
        arr = "".join([c for c in self.word if c in [A, B]])
        if arr == A+B+A+B:
            nn = 1
        elif arr == B+A+B+A:
            nn = -1
        else:
            nn = 0
        return nn      
    
    def lk(self, ltrA: Letter, ltrB: Letter) -> int:
        A, B = ltrA.char, ltrB.char 
        nn = self.arrangement(ltrA, ltrB)
        return nn*(1-2*Sign.asterisk(ltrA.sign, ltrB.sign))
        
    def self_linking(self, ltrA: Letter) -> dict[str, int, str, int]:
        result_dict = {'a': 0, 'b': 0}
        degree = sum([ltrB.sign.pm * self.lk(ltrA, ltrB) for ltrB in self.alphabet])
        result_dict[f"{ltrA.sign.gen}"] = degree
        return result_dict
                    
    def section(self, sign: Sign) -> list[dict]:
        result_list = []
        for ltr in self.alphabet:            
            if ltr.sign == sign:
                sl = self.self_linking(ltr)
                if not (sl['a'] == 0 and sl['b'] == 0):
                    result_list.append(sl)
        return result_list
    
    def self_linking_function(self, x: str) -> dict[str, str, str, list[dict[str, int, str, int]]]:
        output = {'var': x, 'd&c': []}
        for label in Sign.R[x]:
            s = Sign(label)
            sec = self.section(s)
            for r_dict in sec:
                deg = r_dict[f"{x}"]
                new_dandc = [{'deg': deg, 'coeff': dc['coeff'] + s.pm} 
                             if dc['deg'] == deg else dc for dc in output['d&c']]
                if new_dandc == output['d&c']:
                    output['d&c'].append({'deg': deg, 'coeff': s.pm})
                else:
                    output['d&c'] = new_dandc
        output['d&c'] = sorted([dc for dc in output['d&c'] if dc['coeff'] != 0], key=lambda x: x['deg'])
        return output
    
    def sl_polynomial(self, x: str) -> str:
        slfx = self.self_linking_function(x)
        mstr = ''.join(f"+({dc['coeff']}){x}^{dc['deg']}" for dc in slfx['d&c'])
        return mstr[1:]
    
    def ab_polynomials(self) -> tuple[str]:
        return tuple(self.sl_polynomial(x) for x in ['a', 'b'])
    
    #--- n-writhe ---#
    def signs_on_word(self) -> list[tuple[Letter, int]]:
        sow = []
        for i, c in enumerate(self.word):
            ltr = [l for l in self.alphabet if l.char == c][0]
            is_first = (not c in self.word[:i])
            is_in_Ra = (ltr.sign.gen == 'a')
            pm = ltr.sign.pm*(-1) if (not is_first ^ is_in_Ra) else ltr.sign.pm
            sow.append((ltr, pm))
        return sow

    def ind(self, ltr: Letter) -> int:
        sw = self.signs_on_word()
        inds = [i for i, x in enumerate(sw) if x[0] == ltr]
        e = 1 if ltr.sign.gen == 'a' else -1
        return sum([s for l, s in sw[inds[0]+1:inds[1]]])*e

    def writhe_polynomial(self) -> str:
        alph_w_ind = [{'letter': ltr, 'ind': self.ind(ltr)} for ltr in self.alphabet]
        inds = [x['ind'] for x in alph_w_ind]
        J = [{'n': ind, 'c': 0} for ind in set(inds)]
        for elm in J:
            for d in alph_w_ind:
                if d['ind'] == elm['n']:
                    elm['c'] += d['letter'].sign.pm
        if not [d for d in J if d['n'] == 0]:
            J.append({'n': 0, 'c': 0})
        wpoly = ""
        for d in sorted(J, key=lambda x: x['n'], reverse=True):
            if d['n'] != 0:
                if d['c'] != 0:
                    wpoly += f"+({d['c']})t^{d['n']}"
            else:
                s = sum([d['c'] for d in J if not d['n'] == 0])
                wpoly += f"+({-s})"
        return wpoly[1:]


# ## Reidemeister moves

class R:
    Homotopy_data = {('a+', 'a+', 'a+'), ('a-', 'a-', 'a-'), ('a+', 'a+', 'a-'), ('a-', 'a-', 'a+'), ('a-', 'a+', 'a+'), ('a+', 'a-', 'a-'),
                     ('b+', 'b+', 'b+'), ('b-', 'b-', 'b-'), ('b+', 'b+', 'b-'), ('b-', 'b-', 'b+'), ('b-', 'b+', 'b+'), ('b+', 'b-', 'b-')}
    
    @classmethod
    def I(cls, nw: Nanoword, reverse: bool=False, char: str=None, letter: Letter=None, index: int=None) -> Nanoword:
        if not reverse:
            result = cls.__rmi(nw, char=char)
        else:
            result = cls.__rmi_inv(nw, letter=letter, index=index)
        return result
                
    @classmethod
    def II(cls, nw: Nanoword, reverse: bool = False, chars: list = None, letters: list = None, indices: list = None) -> Nanoword:
        if not reverse:
            result = cls.__rmii(nw, chars=chars)
        else:
            result = cls.__rmii_inv(nw, letters=letters, indices=indices)
        return result
    
    @classmethod
    def III(cls, nw:Nanoword) -> Nanoword:
        return cls.__rmiii(nw)

    #---
    @classmethod
    def __rmi(cls, nw: Nanoword, char: str = None):
        result = None
        if char:
            new_word = nw.word.replace(char+char,'')
            if len(new_word) < nw.size:
                new_alphabet = [l for l in nw.alphabet if not l.char == char]
                result = Nanoword(new_word, new_alphabet)
        else:
            for c in nw.chars:
                result = cls.__rmi(nw, char=c)
                if result:
                    break
        return result
        
    @classmethod
    def __rmi_inv(cls, nw: Nanoword, letter: str = None, index: int = None):
        result = None
        if letter is None:
            remaining_chars = [c for c in Letter.ALL_CHARS if c not in nw.chars]
            try:
                letter = Letter(remaining_chars[0], random.sample(Sign.LABELS, k=1)[0])
            except Exception as e:
                print(e)
        if index is None: 
            index = random.randint(0, nw.size)
        #---
        if letter.char not in nw.chars:
            c = letter.char
            new_word = nw.word[:index]+c+c+nw.word[index:]
            new_alphabet = nw.alphabet + [letter]
            result = Nanoword(new_word, new_alphabet)
        else:
            raise ValueError(f"{letter.char} must not be in the alphabet of this nanoword")
        return result        
        
    @classmethod
    def __rmii(cls, nw: Nanoword, chars: str = None):
        result = None
        if chars:
            if len(chars) != 2: raise ValueError(f"{chars} are not a pair of characters")
            letters = [l for l in nw.alphabet if l.char in chars]
            if len(letters) != 2: raise ValueError(f"{chars} are not included in the alphabet")
            if letters[0].sign.tau() == letters[1].sign:
                ll = ''.join(chars)
                new_word = nw.word.replace(ll, '').replace(ll, '').replace(ll[::-1], '')
                if len(new_word) == len(nw.word) - 4:
                    new_alphabet = [v for v in nw.alphabet if not v in letters]
                    result = Nanoword(new_word, new_alphabet)
        else:
            for succ in zip(nw.word, nw.word[1:]+nw.word[:1]):
                if not succ[0] == succ[1]:
                    result = cls.__rmii(nw, chars=list(succ))
                    if result:
                        break
        return result
    
    @classmethod
    def __rmii_inv(cls, nw: Nanoword, letters: list[Letter] = None, indices: tuple[int, int] = None):
        result = None
        if letters is None:
            remaining_chars = [c for c in Letter.ALL_CHARS if c not in nw.chars]
            try:
                letters = [Letter(remaining_chars[0], 'a+'), Letter(remaining_chars[1], 'b-')]
            except Exception as e:
                print(e)
        if indices is None: 
            indices = sorted([random.randint(0, nw.size) for _ in range(2)])
        #---
        if len(letters) == 2 and ({l.char for l in letters} & set(nw.chars)) == set() and letters[0].sign.tau() == letters[1].sign:
            succ = ''.join([l.char for l in letters])
            succ_opposite = succ[::-1] if random.randint(0,1) == 0 else succ
            new_word = nw.word[:indices[0]] + succ + nw.word[indices[0]:indices[1]] + succ_opposite + nw.word[indices[1]:]
            new_alphabet = nw.alphabet + letters
            result = Nanoword(new_word, new_alphabet)
        else:
            raise ValueError(f"{letters} are invalid. Must be a pair of letters that are not in the alphabet of this nanoword.")
        return result

    @classmethod
    def __rmiii(cls, nw: Nanoword):
        w = nw.word
        w_ext = w + w[0]
        rmiii_crossings = []
        all_trios = [trio for trio in itertools.combinations(list(range(nw.size)),3) 
                     if trio[0]+1 < trio[1] and trio[1]+1 < trio[2] and trio[2]+1 < trio[0]+nw.size]
        for trio in all_trios:
            three_succs = [w[trio[i]] + w_ext[trio[i]+1] for i in [0,1,2]]
            if three_succs[0][0] == three_succs[1][0] and three_succs[1][1] == three_succs[2][1] and three_succs[2][0] == three_succs[0][1]:
                three_chars = three_succs[0]+three_succs[1][1]
                three_letters = [[l for l in nw.alphabet if l.char == char].pop() for char in three_chars]
                three_signs = tuple([l.sign for l in three_letters])
                if three_signs in R.Homotopy_data:
                    rmiii_crossings.append(trio)
        if rmiii_crossings:
            trio = random.choice(rmiii_crossings)
            s = nw.size
            for i in trio:
                rotated = w[i:] + w[:i]
                fliped = rotated[:2][::-1] + rotated[2:]
                w = fliped[s-i:] + fliped[:s-i]
            result = Nanoword(w, nw.alphabet)
        else:
            result = None
        return result

## End of File