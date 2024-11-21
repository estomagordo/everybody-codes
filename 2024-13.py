from heapq import heappop, heappush


def parse_a(lines):
    return [list(line) for line in lines]
    

def parse_b(lines):
    return None


def parse_c(lines):
    return None


def solve_a(maze):
    height = len(maze)
    width = len(maze[0])
    sy = -1
    sx = -1
    ey = -1
    ex = -1

    for y in range(height):
        for x in range(width):
            if maze[y][x] == 'S':
                sy = y
                sx = x
            if maze[y][x] == 'E':
                ey = y
                ex = x

    def cell_level(y, x):
        if maze[y][x].isdigit():
            return int(maze[y][x])

        return 0

    frontier = [(0, sy, sx)]
    bestat = {(sy, sx): 0}
    
    while True:
        t, y, x = heappop(frontier)

        if y == ey and x == ex:
            return t
        
        level = cell_level(y, x)
        steps = [
            [y-1, x],
            [y+1, x],
            [y, x-1],
            [y, x+1],
        ]
        
        for dy, dx in steps:
            if 0 <= dy < height and 0 <= dx < width and maze[dy][dx] != '#':
                otherlevel = cell_level(dy, dx)
                diff = abs(level-otherlevel)
                diff = min(diff, 10-diff)
                newtime = t+diff+1

                if (dy, dx) in bestat and bestat[(dy, dx)] < newtime:
                    continue

                bestat[(dy, dx)] = newtime
                
                heappush(frontier, (t+diff+1, dy, dx))


def solve_b(data):
    return None


def solve_c(maze):
    height = len(maze)
    width = len(maze[0])
    starts = set()
    ey = -1
    ex = -1

    for y in range(height):
        for x in range(width):
            if maze[y][x] == 'S':
                starts.add((y, x))
            if maze[y][x] == 'E':
                ey = y
                ex = x

    def cell_level(y, x):
        if maze[y][x].isdigit():
            return int(maze[y][x])

        return 0

    frontier = [(0, ey, ex)]
    bestat = {(ey, ex): 0}
    
    while True:
        t, y, x = heappop(frontier)

        if (y, x) in starts:
            return t
        
        level = cell_level(y, x)
        steps = [
            [y-1, x],
            [y+1, x],
            [y, x-1],
            [y, x+1],
        ]
        
        for dy, dx in steps:
            if 0 <= dy < height and 0 <= dx < width and maze[dy][dx] != '#':
                otherlevel = cell_level(dy, dx)
                diff = abs(level-otherlevel)
                diff = min(diff, 10-diff)
                newtime = t+diff+1

                if (dy, dx) in bestat and bestat[(dy, dx)] < newtime:
                    continue

                bestat[(dy, dx)] = newtime
                
                heappush(frontier, (t+diff+1, dy, dx))


def read_input(part):
    data = [line.rstrip() for line in open(f'input/2024-13{part}.txt').readlines()]

    return data


def main():
    dataa = parse_a(read_input('a'))
    datab = parse_a(read_input('b'))
    datac = parse_a(read_input('c'))

    return solve_a(dataa), solve_a(datab), solve_c(datac)


if __name__ == '__main__':
    print(main())
