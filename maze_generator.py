from cell import Cell
import random
import pygame

grid = []
generator_active = False
generator_path = []
neighbors = []

def init(grid: list[list[Cell]]) -> None:
    globals()["grid"] = grid
    global neighbors, generator_active, generator_path

    rows = len(grid)
    start = (0,0)
    goal = (rows - 1, rows - 1)
    for row in grid:
        for cell in row:
            if cell.get_pos() == start:
                cell.set_start()
            elif cell.get_pos() == goal:
                cell.set_goal()
            else:
                cell.set_wall()

    current_pos = (random.randrange(0, rows), random.randrange(0, rows))
    while current_pos == start or current_pos == goal:
        current_pos = (random.randrange(0, rows), random.randrange(0, rows))
    current_row, current_col = current_pos
    grid[current_row][current_col].reset()

    neighbors = wall_neighbors(current_pos)
    generator_path.append(start)
    generator_active = True
    

def step() -> None:
    global neighbors, generator_path, generator_active
    if neighbors:
        rand_index = random.randrange(0, len(neighbors))
        next_cell = neighbors[rand_index]
        next_cell.reset()
        generator_path.append(next_cell)
        neighbors = wall_neighbors(next_cell.get_pos())
    elif generator_path:
        pass
    else:
        generator_active = False

def is_active() -> bool:
    return generator_active

def wall_neighbors(pos: tuple[int, int]) -> list[Cell]:
    current_row, current_col = pos
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    neighbor_list = []
    for dr, dc in directions:
        neighbor_row, neighbor_col = current_row + dr, current_col + dc
        if not (0 <= neighbor_row < len(grid) and 0 <= neighbor_col < len(grid)):
            continue
        neighbor_cell = grid[neighbor_row][neighbor_col]
        if neighbor_cell.is_wall():
            for dr, dc in directions:
                row, col = neighbor_row + dr, neighbor_col + dc
                if not (0 <= row < len(grid) and 0 <= col < len(grid)):
                    continue
                if (row, col) != pos and grid[row][col].is_empty():
                    break
            else:
                neighbor_list.append(neighbor_cell)
    return neighbor_list
        
