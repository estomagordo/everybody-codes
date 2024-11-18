from collections import Counter


def obtain_password(grid):
    written = []

    while any('.' in row for row in grid):
        for y, row in enumerate(grid):
            for x, character in enumerate(row):
                if character == '.':
                    rowlets = set(c for c in row if c != '.')
                    collets = set(line[x] for line in grid if line[x] != '.')
                    combination = rowlets&collets

                    if len(combination) == 1:
                        putting = list(combination)[0]
                        grid[y][x] = putting
                        written.append((y, x, putting))

    return ''.join(t[2] for t in sorted(written))


def advanced_update(grid):
    written = []

    for y, row in enumerate(grid):
        for x, character in enumerate(row):
            if character == '.':
                rowlets = set(c for c in row if c != '.')
                collets = set(line[x] for line in grid if line[x] != '.')
                combination = rowlets&collets

                if len(combination) == 1:
                    putting = list(combination)[0]
                    grid[y][x] = putting
                    written.append((y, x, putting))

    for y, row in enumerate(grid):
        for x, character in enumerate(row):
            if character == '.':
                rowc = Counter(c for c in row)
                colc = Counter(line[x] for line in grid)

                if rowc['.'] == 1 and colc['.'] == 1 and rowc['?'] == 1 and colc['?'] == 1:
                    target = ''

                    for c in rowc:
                        if c not in '.?' and rowc[c] == 1:
                            target = c
                    if not target:
                        for c in colc:
                            if c not in '.?' and colc[c] == 1:
                                target = c

                    if not target:
                        continue

                    written.append((y, x, target))
                    grid[y][x] = target

                    for yy in range(8):
                        if grid[yy][x] == '?':
                            written.append((yy, x, target))
                            grid[yy][x] = target

                    for xx in range(8):
                        if grid[y][xx] == '?':
                            written.append((y, xx, target))
                            grid[y][xx] = target
                    
    
    return written


def score_password(password):
    return sum((i+1) * (ord(c)-ord('A')+1) for i, c in enumerate(password))


def parse_a(lines):
    return [list(line) for line in lines]
    

def parse_b(lines):
    grid_height = 8
    grid_width = 8
    height = len(lines)
    width = len(lines[0])
    grids = []

    for y in range(0, height, grid_height+1):
        for x in range(0, width, grid_width+1):
            grids.append([list(lines[y+i][x:x+grid_width]) for i in range(grid_height)])

    return grids


def parse_c(lines):
    return [list(line) for line in lines]


def solve_a(grid):
    return obtain_password(grid)


def solve_b(grids):
    def score_grid(grid):
        return score_password(obtain_password(grid))
        
    return sum(score_grid(grid) for grid in grids)


def solve_c(megagrid):
    height = len(megagrid)
    width = len(megagrid[0])
    grid_height = 8
    grid_width = 8
    changed = True

    while changed:
        changed = False

        for y in range(0, height, grid_height):
            for x in range(0, width, grid_width):
                updates = advanced_update([row[x:x+grid_width] for row in megagrid[y:y+grid_height]])
                
                if updates:
                    changed = True
                    for dy, dx, c in updates:
                        megagrid[y+dy][x+dx] = c

    score = 0

    for y in range(0, height, grid_height):
        for x in range(0, width, grid_width):
            password = ''.join(''.join(row[x+2:x+6]) for row in megagrid[y+2:y+6])
            
            if '.' not in password:
                score += score_password(password)

    return score


def read_input(part):
    data = [line.rstrip() for line in open(f'input/2024-10{part}.txt').readlines()]

    return data


def main():
    dataa = parse_a(read_input('a'))
    datab = parse_b(read_input('b'))
    datac = parse_c(read_input('c'))

    return solve_a(dataa), solve_b(datab), solve_c(datac)


if __name__ == '__main__':
    print(main())
