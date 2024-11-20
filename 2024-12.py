def parse_a(lines):
    catapults = []
    targets = []

    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            if c == 'T':
                targets.append((y, x, 1))
            elif c == 'H':
                targets.append((y, x, 2))
            elif c.isalpha():
                catapults.append((c, y, x))

    targets.sort(key=lambda target: (target[1], target[0]))
    
    return catapults, targets
    

def parse_b(lines):
    return None


def parse_c(lines):
    return None


def trajectory(y, x, power, floor):
    cells = []
    rising = power
    planing = power

    while y < floor:
        cells.append((y, x))
        x += 1

        if rising:
            y -= 1
            rising -= 1
        elif planing:
            planing -= 1
        else:
            y += 1

    return cells


def solve_a(catapults, targets):
    points = 0
    floor = max(target[0] for target in targets)

    for y, x, value in targets:
        result = 0

        for c, cy, cx in catapults:
            catval = ord(c) - ord('A') + 1

            for power in range(1, 40):
                cells = trajectory(cy, cx, power, floor+1)
                for ty, tx in cells:
                    if (ty, tx) == (y, x):
                        result = max(result, catval*power*value)
                        break

        if result == 0:
            print('panic!')
        
        points += result

    return points


def solve_b(data):
    return None


def solve_c(data):
    return None


def read_input(part):
    data = [line.rstrip() for line in open(f'input/2024-12{part}.txt').readlines()]

    return data


def main():
    catapultsa, targetsa = parse_a(read_input('a'))
    catapultsb, targetsb = parse_a(read_input('b'))
    datac = parse_c(read_input('c'))

    return solve_a(catapultsa, targetsa), solve_a(catapultsb, targetsb), solve_c(datac)


if __name__ == '__main__':
    print(main())
