from collections import defaultdict


def parse_a(lines):
    key = lines[0]
    grid = [list(line) for line in lines[2:]]

    return key, grid
    

def parse_b(lines):
    return None


def parse_c(lines):
    return None


def rotate(g, y, x, clockwise):
    if clockwise:
        g[y-1][x-1], g[y-1][x], g[y-1][x+1], g[y][x+1], g[y+1][x+1], g[y+1][x], g[y+1][x-1], g[y][x-1] = g[y][x-1], g[y-1][x-1], g[y-1][x], g[y-1][x+1], g[y][x+1], g[y+1][x+1], g[y+1][x], g[y+1][x-1]
    else:
        g[y-1][x-1], g[y-1][x], g[y-1][x+1], g[y][x+1], g[y+1][x+1], g[y+1][x], g[y+1][x-1], g[y][x-1] = g[y-1][x], g[y-1][x+1], g[y][x+1], g[y+1][x+1], g[y+1][x], g[y+1][x-1], g[y][x-1], g[y-1][x-1]


def solve_a(key, grid, times=1):
    height = len(grid)
    width = len(grid[0])
    n = len(key)

    for _ in range(times):
        pos = 0

        for y in range(1, height-1):
            for x in range(1, width-1):
                clockwise = key[pos % n] == 'R'
                rotate(grid, y, x, clockwise)
                pos += 1

    for row in grid:
        if '>' in row:
            return ''.join(row[row.index('>')+1:row.index('<')])


def solve_b(data):
    return None


def solve_c(key, grid):
    m = 1048576000
    height = len(grid)
    width = len(grid[0])
    n = len(key)
    iterations = 0
    wordseen = defaultdict(list)
    modseen = defaultdict(list)

    while True:
        pos = 0

        for y in range(1, height-1):
            for x in range(1, width-1):
                clockwise = key[pos % n] == 'R'
                rotate(grid, y, x, clockwise)
                pos += 1

        iterations += 1

        for row in grid:
            if '>' in row and '<' in row:
                if row.index('>') < row.index('<'):
                    word = ''.join(row[row.index('>')+1:row.index('<')])
                    if '.' not in word and ';' not in word:
                        mod = m%iterations
                        wordseen[word].append(mod)
                        modseen[mod].append(iterations)
                        print(iterations, mod, word, wordseen[word], modseen[mod])


def read_input(part):
    data = [line.rstrip() for line in open(f'input/2024-19{part}.txt').readlines()]

    return data


def main():
    keya, grida = parse_a(read_input('a'))
    keyb, gridb = parse_a(read_input('b'))
    keyc, gridc = parse_a(read_input('c'))

    return solve_a(keya, grida), solve_a(keyb, gridb, 100), solve_c(keyc, gridc)


if __name__ == '__main__':
    print(main())

# length and first correct - 698EXO2365278225
# same 698EEE2365278225