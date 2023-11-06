from enum import Enum, auto

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
                    moves.append((i,j))
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

board = Board
print(board)
 