# -*- mode:python;coding:utf-8 -*-
import curses
import random
import time
from typing import Any

# セル空間サイズ。この値は画面サイズによって初期化し直される
WIDTH = 80
HEIGHT = 40

def empty_space() -> list[int]:
    u'''空のセル空間を作る。'''
    return [0 for _ in range(WIDTH * HEIGHT)]

def index(x: int, y: int) -> int:
    u'''周期的境界条件。
    empty_space が返すセル空間は一次元配列なので、これをアクセスするにあたって
    座標 (x,y) を一次元配列のインデックスに変換する。
    '''
    if x < 0: x += WIDTH
    if x >= WIDTH: x -= WIDTH
    if y < 0: y += HEIGHT
    if y >= HEIGHT: y -= HEIGHT
    return y * WIDTH + x

def is_alive(cell: int) -> bool:
    u'''セル状態が「生」ならば True を、「死」状態なら False を返す
    '''
    return True if (cell & 1) != 0 else False
def count_alive_neighbours(cells: list[int], x: int, y: int) -> int:
    u'''セル状態が「生」の隣接セルの数の和を返す
    '''
    return sum([(1 if is_alive(cells[index(x + dx, y + dy)]) else 0)
                for dx in range(-1, 2)
                for dy in range(-1, 2)
                if dx != 0 or dy != 0])
def get_promoters(cells: list[int], prev: list[int], x: int, y: int) -> dict[int, int]:
    u'''着目している点 (x,y) の更新について、更新隣接セルの種類ごとのカウント数を返す。'''
    promoters: dict[int, int] = dict()
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            i = index(x + dx, y + dy)
            c = cells[i]
            if is_alive(c) == is_alive(prev[i]):
                continue
            cell_type = c & 0xfe
            if cell_type == 0:  # 色なしの隣接セルは無視する
                continue
            if cell_type in promoters:
                promoters[cell_type] += 1
            else:
                promoters[cell_type] = 1
    return promoters
def get_promoter(cells: list[int], prev: list[int], x: int, y: int) -> int:
    u'''着目している点 (x,y) の更新の原因となったセルの種類を決定する。
    決定は直近に更新があった隣接セルの種類の多数決によって行う。
    多数決での決定が不可能な場合は候補からランダムにチョイス。'''
    promoters = get_promoters(cells, prev, x, y)
    i_max = [i for i, count in promoters.items() if count == max(promoters.values())]
    if len(i_max)==1:
        return i_max[0]
    # elif len(i_max) > 0:
    #     cell_type = cells[index(x,y)] & 0xfe
    #     return cell_type if cell_type in i_max else random.sample(i_max, 1)[0]
    return 0
    
def next_cells(cells: list[int], prev: list[int]) -> list[int]:
    u'''現在のセル空間(cells)、直前のセル空間(prev) を元に次ステップのセル空間を返す。'''
    next_cells = empty_space()
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            count = count_alive_neighbours(cells, x, y)
            i = index(x, y)
            is_next_alive = (
                (count == 2 or count == 3) if is_alive(cells[i]) else
                (count == 3))
            if is_next_alive == is_alive(cells[i]):
                next_cells[i] = cells[i]
            else:
                cell_type = get_promoter(cells, prev, x, y)
                if not cell_type:
                    # 更新の原因となった種別が決定不可能な場合には元のまま
                    cell_type = cells[i] & 0xfe
                next_cells[i] = ((1 if is_next_alive else 0) | cell_type)
    return next_cells

def char_of(cell: int) -> str:
    return ('.' if cell == 0 else
            '+' if cell == 1 else
            '.' if cell == 2 else
            '&' if cell == 3 else
            '.' if cell == 4 else
            '$' if cell == 5 else
            '.' if cell == 6 else
            '*' if cell == 7 else
            '.' if cell == 8 else
            '#' if cell == 9 else
            ' ' + str(cell) + ' ')
def color_of(cell: int) -> int:
    cell_type = cell & 0x0e
    return cell_type >> 1

def dump_simple(cells: list[int]) -> None:
    for y in range(0, HEIGHT):
        print(''.join([char_of(cells[index(x, y)]) for x in range(WIDTH)]))

def dump_curses(cells: list[int], screen: Any) -> list[tuple]:
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            cell = cells[index(x, y)]
            screen.addstr(y + 1, x + 1, char_of(cell),
                          curses.color_pair(color_of(cell)))

def main(screen: Any) -> None:
    global WIDTH, HEIGHT
    # ---- 初期化
    # セル空間サイズを画面サイズに合わせる
    rows, cols = screen.getmaxyx()
    HEIGHT = rows - 8
    WIDTH = cols - 2
    # ランダムな初期状態
    prev = empty_space()
    cells = empty_space()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            i = index(x, y)
            if x < WIDTH / 2:
                if y < HEIGHT / 2:
                    cell_type = 1 << 1
                else:
                    cell_type = 2 << 1
            else:
                if y < HEIGHT / 2:
                    cell_type = 3 << 1
                else:
                    cell_type = 4 << 1
            if random.randrange(0,3) == 0:
                cells[i] = 1 | cell_type
            else:
                cells[i] = 0 | cell_type
    # ---- 色の設定
    curses.start_color()
    curses.use_default_colors()
    #for i in range(0, curses.COLORS):
    #    curses.init_pair(i + 1, i, -1)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.curs_set(0)
    # ---- 初期状態の表示
    screen.clear()
    screen.addstr(HEIGHT+1, 1, "genesis")
    dump_curses(cells, screen)
    screen.refresh()
    time.sleep(1)
    # ---- メインループ
    loop_count = 0
    pprev = empty_space()
    while True:
        screen.clear()
        screen.addstr(0, 1, str(RS))
        screen.addstr(HEIGHT+1, 1, str(loop_count))
        loop_count += 1
        dump_curses(cells, screen)
        #---
        data = {'RED': [0,0,0], 'GREEN': [0,0,0], 'CYAN': [0,0,0], 'BLUE': [0,0,0]}
        colors = list(data.keys())
        for i, c in enumerate(cells):
            cc = color_of(c)
            data[colors[cc-1]][0] += 1
            if c in {3,5,7,9}:
                data[colors[cc-1]][1] += 1
                if pprev[i] != c:
                    data[colors[cc-1]][2] += 1
        cc_str = ''.join([
            f" {k:<8}{data[k][0]:>5},{data[k][1]:>5},{round(100*data[k][2]/data[k][1], 1) if data[k][1] > 0 else 0.0:>6}%\n" 
            for k in data])
        screen.addstr(HEIGHT+3, 0, cc_str)
        if all([(round(100*data[k][2]/data[k][1], 1) if data[k][1] > 0 else 0.0) == 0.0 for k in data]):
            screen.getch()  # キー入力を待つ
        #---
        screen.refresh()
        pprev, prev, cells = prev, cells, next_cells(cells, prev)
        time.sleep(0.01)

RS = 6
random.seed(RS)
curses.wrapper(main)