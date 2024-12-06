# 1:47:22
from collections import defaultdict
import json
import numpy as np

UP = "^"
RIGHT = ">"
LEFT = "<"
DOWN = "V"

DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

class LoopError(Exception):
    pass

class EscapeError(Exception):
    pass

class Solver():
    def __init__(self, grid: np.ndarray):
        self.grid = grid
        self.current_position = self._get_guard_position()
        self.current_direction = UP

        self.marked_squares = defaultdict()
        self.directional_marked_squares = defaultdict()

        current_position_str = str(self.current_position)
        self.marked_squares[current_position_str] = True

    def _next_direction(self):
        return DIRECTIONS[(DIRECTIONS.index(self.current_direction) + 1) % 4]

    def _get_guard_position(self):
        pos = np.where(self.grid == "^")
        return [pos[0][0], pos[1][0]]
    
    def _is_caught_in_loop(self):
        current_position_str = str(self.current_position)
        return (current_position_str + self.current_direction) in self.directional_marked_squares
    
    def _move_guard(self):
        if self.current_direction == UP:
            if self.current_position[0] == 0:
                raise EscapeError()

            if self.grid[self.current_position[0] - 1, self.current_position[1]] != "#":
                self.current_position = [self.current_position[0] - 1, self.current_position[1]]
            else:
                self.current_direction = self._next_direction()

        if self.current_direction == LEFT:
            if self.current_position[1] == 0:
                raise EscapeError()

            if self.grid[self.current_position[0], self.current_position[1] - 1] != "#":
                self.current_position = [self.current_position[0], self.current_position[1] - 1]
            else:
                self.current_direction = self._next_direction()

        if self.current_direction == DOWN:
            if self.current_position[0] == len(self.grid) - 1:
                raise EscapeError()
            
            if self.grid[self.current_position[0] + 1, self.current_position[1]] != "#":
                self.current_position = [self.current_position[0] + 1, self.current_position[1]]
            else:
                self.current_direction = self._next_direction()

        if self.current_direction == RIGHT:
            if self.current_position[1] == len(self.grid) - 1:
                raise EscapeError()

            if self.grid[self.current_position[0], self.current_position[1] + 1] != "#":
                self.current_position = [self.current_position[0], self.current_position[1] + 1]
            else:
                self.current_direction = self._next_direction()

        current_position_str = str(self.current_position)
        self.marked_squares[current_position_str] = True
        if self._is_caught_in_loop():
            raise LoopError()

        self.directional_marked_squares[current_position_str + self.current_direction] = True


    def run_until_escape(self):
        while True:
            try:
                self._move_guard()
            except LoopError:
                return False
            except EscapeError:
                return True


if __name__ == "__main__":
    f = open("./input.txt", "r")
    input = f.read()
    orig_grid = np.array([[d for d in line] for line in  input.splitlines()])
    
    solver = Solver(orig_grid)
    solver.run_until_escape()
    num_visited_squares = len(solver.marked_squares)
    print(f"{num_visited_squares = }")

    num_loops = 0
    for [i, j] in [json.loads(squ) for squ in solver.marked_squares]:
        grid_copy = np.copy(orig_grid)
        if grid_copy[i, j] == ".":
            grid_copy[i, j] = "#"
        else:
            continue

        res = Solver(grid_copy).run_until_escape()
        if res is False:
            num_loops += 1

    print(f"{num_loops = }")
