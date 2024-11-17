from collections import defaultdict


def parse_a(lines):
    matrix = [list(map(int, line.split())) for line in lines]

    return [[row[x] for row in matrix] for x in range(4)]
    

def parse_b(lines):
    return None


def parse_c(lines):
    return None


def solve_a(cols):
    rounds = 10

    for round in range(rounds):
        clapcol = round % 4
        dancecol = (round+1) % 4
        clapper = cols[clapcol][0]
        cols[clapcol] = cols[clapcol][1:]
        insert_pos = clapper-1 if clapper <= len(cols[dancecol]) else 2 * len(cols[dancecol]) - clapper + 1
        cols[dancecol] = cols[dancecol][:insert_pos] + [clapper] + cols[dancecol][insert_pos:]

    return ''.join(str(col[0]) for col in cols)


def solve_b(cols):
    target = 2024
    counts = defaultdict(int)
    round = 0

    while True:
        clapcol = round % 4
        dancecol = (round+1) % 4
        clapper = cols[clapcol][0]
        cols[clapcol] = cols[clapcol][1:]
        insert_pos = clapper-1 if clapper <= len(cols[dancecol]) else 2 * len(cols[dancecol]) - clapper + 1
        cols[dancecol] = cols[dancecol][:insert_pos] + [clapper] + cols[dancecol][insert_pos:]
        number = int(''.join(str(col[0]) for col in cols))
        counts[number] += 1
        round += 1

        if counts[number] == target:
            return round * number


def solve_c(cols):
    rounds = 10**6
    seen = set()

    for round in range(rounds):
        clapcol = round % 4
        dancecol = (round+1) % 4
        clapper = cols[clapcol][0]
        cols[clapcol] = cols[clapcol][1:]
        clapper_cut = clapper % (2*len(cols[dancecol]))
        if clapper_cut == 0:
            clapper_cut = 2 * len(cols[dancecol])
        insert_pos = clapper_cut-1 if clapper_cut <= len(cols[dancecol]) else 2 * len(cols[dancecol]) - clapper_cut + 1
        cols[dancecol] = cols[dancecol][:insert_pos] + [clapper] + cols[dancecol][insert_pos:]
        number = int(''.join(str(col[0]) for col in cols))
        seen.add(number)

    return max(seen)


def read_input(part):
    data = [line.rstrip() for line in open(f'input/2024-5{part}.txt').readlines()]

    return data


def main():
    dataa = parse_a(read_input('a'))
    datab = parse_a(read_input('b'))
    datac = parse_a(read_input('c'))

    return solve_a(dataa), solve_b(datab), solve_c(datac)


if __name__ == '__main__':
    print(main())