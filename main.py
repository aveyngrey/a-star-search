import heapq

def distance(point1: tuple[int, int], 
             point2: tuple[int, int]) -> int:
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def astar(grid: tuple[tuple[int, ...]], 
          start: tuple[int, int], 
          goal: tuple[int, int]) -> list[tuple[int, int]]:
    return [(0,0)]

def print_grid(grid: tuple[tuple[int, ...], ...], 
               path: list[tuple[int, int]], 
               start: tuple[int, int], 
               goal: tuple[int, int]) -> None:
    path_set = set(path) if path else set()
    
    for r in range(len(grid)):
        line = ""
        for c in range(len(grid[r])):
            coord = (r, c)
            if coord == start:
                line += " S "
            elif coord == goal:
                line += " G "
            elif coord in path_set:
                line += " * "
            elif grid[r][c] == 1:
                line += " ■ "
            else:
                line += " . "
        print(line)


if __name__ == "__main__":
    map = (
        (0, 0, 0, 0, 0, 1, 0, 0),
        (0, 1, 0, 1, 0, 0, 0, 1),
        (0, 1, 0, 1, 0, 1, 1, 0),
        (0, 1, 1, 1, 0, 0, 0, 0),
        (0, 0, 0, 1, 1, 0, 1, 0),
        (0, 1, 0, 1, 0, 0, 1, 0),
        (0, 1, 0, 1, 0, 1, 1, 1),
        (0, 1, 0, 1, 0, 0, 0, 0),
    )
    start = (0,0)
    goal = (7,7)
    path = [(0,0),(0,1),(0,2),(0,3),(0,4)]
    print_grid(map, path, start, goal)