import pygame
from cell import Cell

pygame.init()
WIN = pygame.display.set_mode((700,700))
pygame.display.set_caption("A* Search")
clock = pygame.time.Clock()

def make_grid(rows: int, width: int) -> list[list[Cell]]:
        grid = []
        cell_width = width // rows
        for row in range(rows):
            grid.append([])
            for col in range(rows):
                cell = Cell(row, col, cell_width, rows)
                grid[row].append(cell)
        return grid

def draw_grid(win, rows, width):
    cell_width = width // rows
    for i in range(rows):
        pygame.draw.line(win, pygame.Color("black"), (0, i * cell_width), (width, i * cell_width))
    for j in range(rows):
        pygame.draw.line(win, pygame.Color("black"), (j * cell_width, 0), (j * cell_width, width))

def draw(win, grid, rows, width):
    win.fill("white")

    for row in grid:
        for cell in row:
            cell.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    cell_width = width // rows
    x, y = pos

    row = y // cell_width
    col = x // cell_width

    if row >= rows:
        row = rows - 1
    elif row < 0:
        row = 0

    if col >= rows:
        col = rows - 1
    elif col < 0:
        col = 0

    return row, col

def main(win, rows, width):
    grid = make_grid(rows, width)

    # keep track of start and goal cells
    start = None
    goal = None

    running = True
    started = False

    final_grid = None # grid once player submits it

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not started:
            if pygame.mouse.get_pressed()[0]: # left click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows, width)
                cell = grid[row][col]
                if not start and cell != goal:
                    start = cell
                    cell.set_start()
                elif not goal and cell != start:
                    goal = cell
                    cell.set_goal()
                elif cell != start and cell != goal:
                    cell.set_wall()
            elif pygame.mouse.get_pressed()[2]: # right click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows, width)
                cell = grid[row][col]
                if cell == start:
                    start = None
                elif cell == goal:
                    goal = None
                cell.reset()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                started = True
                final_grid = tuple(tuple(row) for row in grid)

        if started:
            pass


        WIN.fill("gray")

        draw(win, grid, rows, width)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main(WIN, 21, 700)
