from nanoword import *                         


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

###End_of_file