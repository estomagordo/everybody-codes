def neighbours(y, x):
    return [
        [y-1, x],
        [y+1, x],
        [y, x-1],
        [y, x+1],
    ]

def eight_neighbours(y, x):
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dy or dx:
                yield((y+dy, x+dx))


def parse_a(lines):
    return [list(line) for line in lines]


def solve_a(matrix):
    height = len(matrix)
    width = len(matrix[0])

    count = 0
    iteration = 1

    while True:
        target = '#' if iteration == 1 else str(iteration-1)
        updates = []

        for y in range(1, height-1):
            for x in range(1, width-1):
                if matrix[y][x] != target:
                    continue

                surrounded = all(matrix[ny][nx] == target for ny, nx in neighbours(y, x))
                
                if iteration == 1 or surrounded:
                    updates.append((y, x))

        if not updates:
            break

        for y, x in updates:
            matrix[y][x] = str(iteration)
            count += 1

        iteration += 1

    return count


def solve_c(matrix):
    height = len(matrix)
    width = len(matrix[0])

    count = 0
    iteration = 1

    while True:
        target = '#' if iteration == 1 else str(iteration-1)
        updates = []

        for y in range(height):
            for x in range(width):
                if matrix[y][x] != target:
                    continue
                
                surrounded = 0 < y < height-1 and 0 < x < width-1 and all(matrix[ny][nx] == target for ny, nx in eight_neighbours(y, x))
                
                if iteration == 1 or surrounded:
                    updates.append((y, x))

        if not updates:
            break

        for y, x in updates:
            matrix[y][x] = str(iteration)
            count += 1

        iteration += 1

    return count


def read_input(part):
    data = [line.rstrip() for line in open(f'input/2024-3{part}.txt').readlines()]

    return data


def main():
    dataa = parse_a(read_input('a'))
    datab = parse_a(read_input('b'))
    datac = parse_a(read_input('c'))

    return solve_a(dataa), solve_a(datab), solve_c(datac)


if __name__ == '__main__':
    print(main())