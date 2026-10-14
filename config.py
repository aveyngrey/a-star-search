import pygame
import cell
import app

# list of pygame named colors:
# https://www.pygame.org/docs/ref/color_list.html
empty_color = pygame.Color("lightgray")
open_color = pygame.Color("purple")
closed_color = pygame.Color("lightpink")
start_color = pygame.Color("green")
goal_color = pygame.Color("yellow")
wall_color = pygame.Color("black")
path_color = pygame.Color("blue")
maze_generate_color = pygame.Color("red")

display_width = 750
rows = 100
fps = 60
steps_per_frame = 20

if __name__ == "__main__":
    cell.init_colors(empty_color, open_color, closed_color, start_color,
                     goal_color, wall_color, path_color, maze_generate_color)

    # makes it so (display_width % rows = 0) to ensure a perfect fit
    display_width = display_width - (display_width % rows)

    win = pygame.display.set_mode((display_width,display_width))
    pygame.display.set_caption("A* Search")
    app.main(win, rows, display_width, fps, steps_per_frame)
