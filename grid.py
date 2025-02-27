import random as r

from minesweeper_types import MS


class Grid:
    def __init__(self, columns=10, rows=10, mines=10):

        self.grid       = [[MS.Empty for _ in range(columns)] for _ in range(rows)]
        self.hidden     = [[True for _ in range(columns)] for _ in range(rows)]
        self.flags      = [[False for _ in range(columns)] for _ in range(rows)]
        self.flag_count = 0
        self.mine_count = mines
        self.rows       = rows     if rows > 0     else 1
        self.columns    = columns  if columns > 0  else 1

        for _ in range(mines):
            while True:
                # Choose a random position for the mine
                x = r.randint(0, columns-1)
                y = r.randint(0, rows-1)

                # If there is a mine there already, choose another place
                if self.grid[y][x] != MS.Empty: continue

                self.grid[y][x] = MS.Mine
                break

        for x in range(columns):
            for y in range(rows):
                if self.grid[y][x] == MS.Empty:
                    # We are using the Enum's value lookup feature
                    #   to shorten our code. Since MS(0) == MS.Empty
                    #   and MS(n) for 0 < n <= 8 gives us the corresppnding number
                    self.grid[y][x] = MS(self._count_neighbors(x, y))

    def _count_neighbors(self, x, y):
        neighbors = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == j == 0: continue # We want to check the neighbors, not the block itself
                
                # It shouldn't be out of bounds
                if x + i < 0                or y + j < 0            : continue
                if x + i > self.columns-1   or y + j > self.rows-1  : continue

                if self.grid[y+j][x+i] == MS.Mine: neighbors += 1

        return neighbors

    def uncover(self, x, y):
        if x < 0 or y < 0 or x >= self.columns or y >= self.rows: return
        if not self.hidden[y][x]: return

        self.hidden[y][x]   = False
        self.flags[y][x]    = False

        if self.grid[y][x] == MS.Empty:

            self.uncover(x+1, y+1)
            self.uncover(x+1, y)
            self.uncover(x+1, y-1)
            self.uncover(x, y+1)
            self.uncover(x, y)
            self.uncover(x, y-1)
            self.uncover(x-1, y+1)
            self.uncover(x-1, y)
            self.uncover(x-1, y-1)

    def flag(self, x, y):
        if self.hidden[y][x]:
            # Toggle the flag at (x, y)
            self.flag_count += 1 if self.flags[y][x] == False else -1
            self.flags[y][x] ^= True

### By Radin ###
