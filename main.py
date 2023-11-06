from enum import Enum, auto
import random
import math


class GameState(Enum):
    # states
    DRAW = auto()
    ON = auto()
    OVER = auto()


class Mark(Enum):
    # marks
    X = auto()
    O = auto()
    EMPTY = auto()


class Board:
    # initialize the board
    def __init__(self):
        self.cell = [[Mark.EMPTY for i in range(3)] for j in range(3)]
        self.is_first_player = True

    # define state
    def state(self):
        if self.won():
            return GameState.OVER
        elif len(self.possible_moves()) == 0:
            return GameState.DRAW
        else:
            return GameState.ON

    # moves
    def possible_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.cell[i][j] == Mark.EMPTY:
                    moves.append((i, j))
        return moves

    # marking
    def make_move(self, move):
        if self.cell[move[0]][move[1]] == Mark.EMPTY:
            if self.is_first_player:
                self.cell[move[0]][move[1]] = Mark.X
            else:
                self.cell[move[0]][move[1]] = Mark.O
            self.is_first_player = not self.is_first_player

    # judge
    def won(self):
        def check_cells(x, y, dx, dy):
            if self.cell[x][y] == Mark.EMPTY:
                return False
            for i in range(3):
                if self.cell[x][y] != self.cell[x + i * dx][y + i * dy]:
                    return False
            return True

        for i in range(3):
            if check_cells(i, 0, 0, 1):
                return True
            if check_cells(0, i, 1, 0):
                return True

        if check_cells(0, 0, 1, 1):
            return True
        if check_cells(0, 2, 1, -1):
            return True

    # rewind
    def rewind(self, move):
        self.cell[move[0]][move[1]] = Mark.EMPTY
        self.is_first_player = not self.is_first_player

    def __str__(self):
        board_str = ""
        for i in range(3):
            for j in range(3):
                if self.cell[i][j] == Mark.X:
                    board_str += "X"
                elif self.cell[i][j] == Mark.O:
                    board_str += "O"
                else:
                    board_str += "/"
            board_str += "\n"
        return board_str


board = Board()

# random
"""
while True:
    if board.state() == GameState.OVER or board.state() == GameState.DRAW:
        break
    print("先手" if board.is_first_player else "後手")
    next_move = random.choice(board.possible_moves())
    board.make_move(next_move)

    print(board)
"""


# minimax
def minimax(board):
    # draw: 0, win: 1, lose: -1
    if board.state() == GameState.DRAW:
        return 0
    elif board.state() == GameState.OVER:
        return -1

    best_score = -math.inf

    for move in board.possible_moves():
        board.make_move(move)
        score = -minimax(board)
        board.rewind(move)
        if score > best_score:
            best_score = score

    return best_score


# first: minimax, second: random
"""
while True:
    if board.state() == GameState.OVER or board.state() == GameState.DRAW:
        break

    print("先手" if board.is_first_player else "後手")
    best_score = -math.inf
    best_move = None


    if board.is_first_player:
        move_dict = {}
        for move in board.possible_moves():
            board.make_move(move)
            score = -minimax(board)
            move_dict[move] = score
            board.rewind(move)
            if score > best_score:
                best_score = score
                best_move = move
        next_move = best_move
        print(move_dict)
    else:
        next_move = random.choice(board.possible_moves())


    board.make_move(next_move)
    print(board)
"""

# minimax vs minimax
"""
while True:
    if board.state() == GameState.OVER or board.state() == GameState.DRAW:
        break

    print("先手" if board.is_first_player else "後手")
    best_score = -math.inf
    best_move = None

    if board.is_first_player:
        move_dict = {}
        for move in board.possible_moves():
            board.make_move(move)
            score = -minimax(board)
            move_dict[move] = score
            board.rewind(move)
            if score > best_score:
                best_score = score
                best_move = move
        next_move = best_move
        print(move_dict, best_move)

    else:
        # best_score = -best_score
        move_dict = {}
        for move in board.possible_moves():
            board.make_move(move)
            score = -minimax(board)
            move_dict[move] = score
            board.rewind(move)
            if score > best_score:
                best_score = score
                best_move = move
        next_move = best_move
        print(move_dict, best_move)

    board.make_move(next_move)
    print(board)
"""


# alpha-beta
def alpha_beta(board, alpha, beta):
    if board.state() == GameState.DRAW:
        return 0
    elif board.state() == GameState.OVER:
        return -1

    for move in board.possible_moves():
        board.make_move(move)
        score = -alpha_beta(board, alpha=-beta, beta=-alpha)
        if score > alpha:
            alpha = score
        board.rewind(move)
        if alpha >= beta:
            return alpha

    return alpha


"""
# alpha-beta vs random
while True:
    if board.state() == GameState.OVER or board.state() == GameState.DRAW:
        break

    print("先手" if board.is_first_player else "後手")
    # best_score = -math.inf
    best_move = None
    alpha = -math.inf
    # 先手の場合はalpha-beta法を用いて最善手を選択する
    if board.is_first_player:
        # 全ての可能な手について評価関数を計算し，最大の評価関数を持つ手を選択する
        move_dict = {}
        for move in board.possible_moves():
            board.make_move(move)
            score = -alpha_beta(board, alpha=-math.inf, beta=-alpha)
            move_dict[move] = score
            board.rewind(move)
            if score > alpha:
                best_move = move
                alpha = score
        next_move = best_move
        print(move_dict)
    else:
        # 後手の場合はランダムに手を選択する
        next_move = random.choice(board.possible_moves())
    board.make_move(next_move)
    print(board)
"""

# alpha-beta vs human
"""
  0 1 2
0 / / /
1 / / /
2 / / /
"""

while True:
    if board.state() == GameState.OVER or board.state() == GameState.DRAW:
        break

    print("先手" if board.is_first_player else "後手")
    # best_score = -math.inf
    best_move = None
    alpha = -math.inf
    # 先手の場合はalpha-beta法を用いて最善手を選択する
    if board.is_first_player:
        # 全ての可能な手について評価関数を計算し，最大の評価関数を持つ手を選択する
        move_dict = {}
        for move in board.possible_moves():
            board.make_move(move)
            score = -alpha_beta(board, alpha=-math.inf, beta=-alpha)
            move_dict[move] = score
            board.rewind(move)
            if score > alpha:
                best_move = move
                alpha = score
        next_move = best_move
        print(move_dict)
    else:
        # 後手の場合はランダムに手を選択する
        while True:
            next_move = (int(input("your turn. x:")), int(input("y:")))
            if next_move in board.possible_moves():
                break
            else:
                print("you cannot put your mark at this place.")
    board.make_move(next_move)
    print(board)
