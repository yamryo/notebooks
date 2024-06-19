from nanoword import *


# ## Virtual knot diagram

class Cell:
    def __init__(self, i: int, j: int, head: str, tail: str) -> None:
        self.row = i
        self.col = j
        self.head = head
        self.tail = tail
    def __str__(self) -> str: return f"{self.to_tpl()}"
    def __repr__(self) -> str: return f"(({self.row}, {self.col}), ({self.head}, {self.tail}))"
    def __eq__(self, other) -> bool:
        if not isinstance(other, type(self)): raise ValueError(f"{other=} is not a Cell, but a {type(other)}.")
        return self.to_tpl() == other.to_tpl()
    #---    
    def to_tpl(self) -> tuple[int]:
        return (self.row, self.col)
    #---
    def move(self, length: int) -> None:
        match self.head:
            case 'r':
                self.col += length
                self.tail = 'l'
            case 'l':
                self.col -= length
                self.tail = 'r'
            case 't':
                self.row -= length
                self.tail = 'b'
            case 'b':
                self.row += length
                self.tail = 't'
            case _:
                raise ValueError(f"{self.head=}")

#---------
class Diagram:
    PIECES = [
        {'label': 'ep', 'code': 0b0, 'tmb': ('', '.', '')}, 
        {'label': 'hz', 'code': 0b01, 'tmb': ('', '-----', '')},
        {'label': 'vt', 'code': 0b10, 'tmb': ('|', '|', '|')},
        {'label': 'vc', 'code': 0b11, 'tmb': ('|', '--+--', '|')}, 
        #---
        {'label': 'b-', 'code': 0b100, 'tmb': ('|', '---->', '↓')},
        {'label': 'b+', 'code': 0b101, 'tmb': ('|', '--|->', '↓')}, 
        {'label': 'a-', 'code': 0b110, 'tmb': ('↑', '--|->', '|')}, 
        {'label': 'a+', 'code': 0b111, 'tmb': ('↑', '---->', '|')}, 
        #---
        {'label': 'xx', 'code': 0b1000, 'tmb': ('', '*', '')},
        #---
        {'label': 'rb', 'code': 0b1100, 'tmb': ('', '  ┌--', '|')},
        {'label': 'rt', 'code': 0b1101, 'tmb': ('|','  └--', '')},
        {'label': 'lb', 'code': 0b1110, 'tmb': ('', '--┐  ', '|')},
        {'label': 'lt', 'code': 0b1111, 'tmb': ('|','--┘  ', '')},     
    ]

    def __init__(self, nw: Nanoword) -> None:
        self.nw = nw
        self.matrix = self.__get_matrix()

    def __get_matrix(self):
        s = self.nw.size // 2
        marr = np.zeros([3*s+2,3*s+2]).astype(int)
        for i, ltr in enumerate(self.nw.alphabet):
            marr[3*i+2][3*i+2] = [d['code'] for d in self.PIECES if d['label'] == ltr.sign].pop()
            marr[3*i+2][3*i+2+1] = 0b01
            marr[3*i+2][3*i+2-1] = 0b01
            marr[3*i+2-1][3*i+2] = 0b10
            marr[3*i+2+1][3*i+2] = 0b10
        return marr

    def __set_piece(self, arg: str | int) -> list[str]:
        if arg in [v['label'] for v in self.PIECES]:
            code = [v['code'] for v in self.PIECES if v['label'] == arg].pop()
        elif arg in [v['code'] for v in self.PIECES]:
            code = arg
        else:
            raise ValueError(f'Not implemented for {arg, type(arg)}')
        tmb = [d['tmb'] for d in self.PIECES if d['code'] == code].pop()
        return [f"{row:^5}" for row in tmb]

    def show(self) -> None:
        pieces_matrix = []
        for row in self.matrix:
            pieces_row = []
            for v in row:
                try:
                    pieces_row.append(self.__set_piece(v))
                except Exception as e:
                    print(f"{e=}")
                    pieces_row.append(self.__set_piece(0))
            pieces_matrix.append(pieces_row)
        for row in pieces_matrix:
            for i in range(3):
                print(''.join([cr[i] for cr in row]))
       
    def __approach_goal(self, cc: Cell, goal: Cell) -> Cell:
        marr = self.matrix
        match goal.tail:
            case 'l':
                # goal_zone = marr[goal.row, :goal.col]
                if cc.col >= goal.col:
                    # if cc.row == goal.row:
                    #     if cc.port in {'r', 'b'}:
                    #         print(f"Why? {cc.port=}")
                    #     else: 
                            
                    #         cc.move('up' if cc.port == 'b' else 'down')
                    #         dest = Cell(cc.row, goal.col - 1, 'r')
                    #     flag = 0
                    #     while not flag and dest.col >= 0:
                    #         if cc.row > goal.row:
                    #             next_route = marr[goal.row:cc.row+1, dest.col]
                    #         else:
                    #             next_route = marr[cc.row:goal.row+1, dest.col]
                    #         if set(next_route).issubset({0,1}):
                    #             flag = 1
                    #         else:
                    #             dest.col -= 1
                    #     else:
                    #         if dest.col < 0:
                    #             raise IndexError(f"{dest=} turned out to be negative!")
                    #     self.__go_straight(cc, 'left', dest)
                    # else:
                    pass
                elif cc.col < goal.col:
                    if cc.row == goal.row:
                        cc.head = 'r'
                        cc.go_straight(length=goal.col-cc.col)
                    else:
                        next_is_hori = (cc.head in {'t', 'b'})
                        cc_ind = cc.col if next_is_hori else cc.row
                        an_arr = marr[:, cc_ind] if next_is_hori else marr[cc_ind, :]
                        cc_zero_neighbor = []
                        ind_last = -1
                        for k, g in itertools.groupby(an_arr):
                            lg = list(g)
                            ind_first = ind_last + 1
                            ind_last = ind_first + len(lg) - 1
                            if k == 0:
                                print(f"{cc_ind=}, {(ind_first, ind_last)=}")
                                if ind_last == cc_ind - 1:
                                    cc_zero_neighbor.append(ind_first)
                                elif ind_first == cc_ind + 1:
                                    cc_zero_neighbor.append(ind_last)
                        if len(cc_zero_neighbor) == 1:
                            cc_zero_neighbor.append(cc_ind)
                        elif len(cc_zero_neighbor) == 0:
                            print(f"Dead end at {cc=}!!: {[list(g) for k,g in itertools.groupby(an_arr)]}")
                        
                        i, j = tuple(sorted(cc_zero_neighbor))
                        print(f"{(i,j)}")
                        if next_is_hori:
                            cc.head = 'r' if cc.col < j else 'l'
                            cc.move(length = 1)
                        else:                                
                            if goal.row in range(i,j+1):
                                cc.head = 'b' if cc.row < goal.row else 't'
                                cc.move(length=abs(goal.row - cc.row))
                            else:
                                cc.head = 'b' if cc.row < j else 't'
                                cc.move(length=1)
                    cc = goal
            case 't': 
                # goal_zone = marr[:goal.row, goal.col]
                cc = goal
            case 'b':
                # goal_zone = marr[goal.row, goal.col+1:]
                cc = goal
        return cc
            
    def create_route(self, start: Cell, goal: Cell):
        marr = self.matrix
        cc = start
        num = marr[start.to_tpl()]
        #-----
        # Take the first step 
        cc.move(length=1)
        marr[cc.to_tpl()] = num
        #-----
        # Find a route and draw lines to the goal
        while cc != goal:
            print(f"{cc=}")
            cc = self.__approach_goal(cc, goal)
            if cc != goal:
                marr[cc.to_tpl()] = num
            else:
                print(f"Yey!!, {cc=} is equal to {goal=}!")
        return self

#------------------------------------------------------------        
        # if dff > 0:
        #     match goal[1]:
        #         case 'l':
        #             if cc.row == goal[0]:
        #                 marr[cc.to_tpl()] = 0b1101
        #                 while cc.move('right').col != goal[0]:
        #                     marr[cc.to_tpl()] += 0b01
        #             else:
        #                 marr[cc.move('left').to_tpl()] = 0b1110   ### ここで、left 移動してよい場所を探したい!
        #                 while cc.move('down').row != goal[0]:
        #                     marr[cc.to_tpl()] += 0b10
        #                 marr[cc.to_tpl()] = 0b1101
        #         case 't':
        #             pass
        #         case 'b':
        #             pass
        #         case _:
        #             raise NotImplementedError(f"{goal[1]=} is not implemented")
        # else:  # i.e., dff < 0
        #     match goal[1]:
        #         case 'l':
        #             if cc.row == goal[0]:
        #                 marr[cc.move('down').to_tpl()] = 0b1110   ### ここで、left 移動してよい場所を探したい!
        #                 while cc.move('left').col != goal[0] -1:
        #                     marr[cc.to_tpl()] += 0b01
        #                 marr[cc.to_tpl()] = 0b1101
        #                 marr[cc.move('up').to_tpl()] = 0b1100
        #             else:
        #                 marr[cc.to_tpl()] += 0b01
        #                 marr[cc.move('left').to_tpl()] = 0b1101   ### ここで、left 移動してよい場所を探したい!
        #                 while cc.move('up').row != goal[0]:
        #                     marr[cc.to_tpl()] += 0b10
        #                 marr[cc.to_tpl()] = 0b1100
        #         case 't':
        #             pass
        #         case 'b':
        #             pass
        #         case _:
        #             raise NotImplementedError(f"{goal[1]=} is not implemented")
            
               
        #     if goal[1] == 'l':
        #         if dff > 0:
        #             marr[cc.to_tpl()] = 0b1101
        #             while cc.move('right').col < goal[0]:
        #                 marr[cc.to_tpl()] += 0b01
        #         else:
        #             marr[cc.move('down').to_tpl()] = 0b1110
        #             while cc.move('left').col >= goal[0]:
        #                 marr[cc.to_tpl()] += 0b01
        #             marr[cc.to_tpl()] = 0b1101
        #             marr[cc.move('up').to_tpl()] = 0b1100
        #     else:
        #         if dff > 0:
        #             marr[cc.move('down' if goal[1] == 'b' else 'up').to_tpl()] = 0b1101
        #             while cc.move('right').col < goal[0]:
        #                 marr[cc.to_tpl()] += 0b01
        #             marr[cc.to_tpl()] = 0b1111 ^ (goal[1] == 't')
        #         else:
        #             if goal[1] == 't':
        #                 marr[cc.to_tpl()] += 0b10
        #                 while marr[cc.to_tpl()] == 0b11:
        #                     marr[cc.move('up').to_tpl()] += 0b10
        #                 marr[cc.move('up').to_tpl()] = 0b1110
        #             else:
        #                 while marr[cc.move('down').to_tpl()] == 0b11:
        #                     marr[cc.to_tpl()] -= 0b10
        #                 marr[cc.to_tpl()] = 0b1110
        #             while cc.move('left').col > goal[0]:
        #                 marr[cc.to_tpl()] += 0b01
        #             marr[cc.to_tpl()] = 0b1101 ^ (goal[1] == 't')
        #             while cc.move('down' if goal[1] == 't' else 'up').row != goal[0]:
        #                 marr[cc.to_tpl()] += 0b10
        # else:
        #     while marr[cc.move('down' if start[1] == 'b' else 'up').to_tpl()] == 0b01:
        #          marr[cc.to_tpl()] += 0b10
        #     marr[cc.to_tpl()] = (0b1110 if dff < 0 else 0b1100) | (start[1] == 'b')
        #     while cc.move('right' if dff > 0 else 'left').col != goal[0]:
        #         marr[cc.to_tpl()] += 0b01
        #     #---
        #     if goal[1] == 'l':
        #         if dff > 0:
        #             marr[cc.move('left').to_tpl()] = 0b1110
        #             while cc.move('down').row != goal[0]:
        #                 marr[cc.to_tpl()] += 0b10
        #             marr[cc.to_tpl()] = 0b1101
        #             while cc.move('right').col < goal[0]:
        #                 marr[cc.to_tpl()] += 0b01
        #         else:
        #             marr[cc.to_tpl()] += 0b01
        #             while marr[cc.move('left').to_tpl()] == 0b10:
        #                 marr[cc.to_tpl()] += 0b01
        #             marr[cc.to_tpl()] = 0b1101
        #             while cc.move('up').row != goal[0]:
        #                 marr[cc.to_tpl()] += 0b10
        #             marr[cc.to_tpl()] = 0b1100
        #             while cc.move('right').col < goal[0]:
        #                 marr[cc.to_tpl()] += 0b01
        #     else:
        #         if dff > 0:
        #             if goal[1] == 't':
        #                 marr[cc.to_tpl()] = 0b1110
        #                 while cc.move('down').row != goal[0]:
        #                     marr[cc.to_tpl()] += 0b10
        #             else:
        #                 marr[cc.to_tpl()] += 0b01
        #                 while marr[cc.move('right').to_tpl()] == 0b10:
        #                     marr[cc.to_tpl()] += 0b01
        #                 marr[cc.to_tpl()] = 0b1110
        #                 while cc.move('down').row <= goal[0]:
        #                     marr[cc.to_tpl()] += 0b10
        #                 marr[cc.to_tpl()] = 0b1101
        #                 while cc.move('left').col > goal[0]:
        #                     marr[cc.to_tpl()] += 0b01
        #                 marr[cc.to_tpl()] = 0b1111
        #                 while cc.move('up').row < goal[0]:
        #                     marr[cc.to_tpl()] += 0b10
        #         else:
        #             if goal[1] == 'b':
        #                 marr[cc.to_tpl()] = 0b1101
        #                 while cc.move('up').row != goal[0]:
        #                     marr[cc.to_tpl()] += 0b10
        #             else:
        #                 marr[cc.to_tpl()] += 0b01
        #                 while marr[cc.move('left').to_tpl()] == 0b10:
        #                     marr[cc.to_tpl()] += 0b01
        #                 marr[cc.to_tpl()] = 0b1101
        #                 while cc.move('up').row >= goal[0]:
        #                     marr[cc.to_tpl()] += 0b10
        #                 marr[cc.to_tpl()] = 0b1100
        #                 while cc.move('right').col < goal[0]:
        #                     marr[cc.to_tpl()] += 0b01
        #                 marr[cc.to_tpl()] = 0b1110
        #                 while cc.move('down').row < goal[0]:
        #                     marr[cc.to_tpl()] += 0b10