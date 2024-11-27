def parse_a(lines):
    return [list(line) for line in lines]
    

def parse_b(lines):
    return None


def parse_c(lines):
    return None


def solve_a(grid):
    height = len(grid)
    width = len(grid[0])
    sy = 0
    sx = 0

    while grid[0][sx] == '#':
        sx += 1

    seen = {(sy, sx)}
    frontier = [(0, sy, sx)]

    def okay(y, x):
        return (y, x) not in seen and 0 <= y < height and 0 <= x < width and grid[y][x] != '#'

    for d, y, x in frontier:
        if grid[y][x] == 'H':
            return 2*d
        
        for my, mx in ((y+1, x), (y-1, x), (y, x+1), (y, x-1)):
            if okay(my, mx):
                seen.add((my, mx))
                frontier.append((d+1, my, mx))

def solve_b(grid):
    height = len(grid)
    width = len(grid[0])

    all_herbs = set()

    for row in grid:
        for c in row:
            if c.isalpha():
                all_herbs.add(c)
    
    sy = 0
    sx = 0

    while grid[0][sx] == '#':
        sx += 1

    seen = {('', sy, sx)}
    frontier = [(set(), 0, sy, sx)]

    def okay(found, y, x):
        return (found, y, x) not in seen and 0 <= y < height and 0 <= x < width and grid[y][x] not in '~#'

    for found, d, y, x in frontier:
        if y == sy and x == sx and len(found) == len(all_herbs):
            return d
        
        if grid[y][x].isalpha():
            found.add(grid[y][x])
        
        foundkey = ''.join(sorted(found))

        for my, mx in ((y+1, x), (y-1, x), (y, x+1), (y, x-1)):
            if okay(foundkey, my, mx):
                newfound = set(found)
                seen.add((foundkey, my, mx))
                frontier.append((newfound, d+1, my, mx))


def solve_c(data):
    return None


def read_input(part):
    data = [line.rstrip() for line in open(f'input/2024-15{part}.txt').readlines()]

    return data


def main():
    dataa = parse_a(read_input('a'))
    datab = parse_a(read_input('b'))
    datac = parse_a(read_input('c'))

    return solve_a(dataa), solve_b(datab), solve_b(datac)


if __name__ == '__main__':
    print(main())
