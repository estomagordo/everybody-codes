from collections import Counter


def parse_a(lines):
    turns = list(map(int, lines[0].split(',')))
    n = len(turns)
    strips = [[] for _ in range(n)]
    step = 4

    for line in lines[2:]:
        for i in range(n):
            if len(line) > step * i and line[step * i] != ' ':
                strips[i].append(line[step*i:step*i+3])

    return turns, strips
    

def parse_b(lines):
    return None


def parse_c(lines):
    return None


def solve_a(turns, strips):
    steps = 100
    n = len(turns)

    print(' '.join(strips[i][(turns[i] * steps) % len(strips[i])] for i in range(n)))


def solve_b(turns, strips):
    def tally(sequence):
        c = Counter()

        for s in sequence:
            c[s[0]] += 1
            c[s[2]] += 1

        return sum(max(0, v-2) for v in c.values())

    m = 202420242024
    n = len(turns)
    positions = [0 for _ in range(n)]
    seen = set()
    points = []

    while True:
        t = tuple(positions)

        if t in seen:
            break

        seen.add(t)
        points.append(tally([strips[i][positions[i]] for i in range(n)]))

        for i in range(n):
            positions[i] = (positions[i] + turns[i]) % len(strips[i])

    p = len(points)
    full_cycle = sum(points)
    cycle_count = m // p
    overshoot = m % p
    overshoot_points = sum(points[:overshoot])

    return full_cycle * cycle_count + overshoot_points


def solve_c(turns, strips):
    def tally(sequence):
        c = Counter()

        for s in sequence:
            c[s[0]] += 1
            c[s[2]] += 1

        return sum(max(0, v-2) for v in c.values())

    m = 2
    n = len(turns)
    positions = [0 for _ in range(n)]
    seen = set()
    points = []

    while True:
        t = tuple(positions)

        if t in seen:
            break

        seen.add(t)
        points.append(tally([strips[i][positions[i]] for i in range(n)]))

        for i in range(n):
            positions[i] = (positions[i] + turns[i]) % len(strips[i])

    p = len(points)
    full_cycle = sum(points)
    cycle_count = m // p
    overshoot = m % p
    overshoot_points = sum(points[:overshoot])

    return full_cycle * cycle_count + overshoot_points


def read_input(part):
    data = [line.rstrip() for line in open(f'input/2024-16{part}.txt').readlines()]

    return data


def main():
    turnsa, stripsa = parse_a(read_input('a'))
    turnsb, stripsb = parse_a(read_input('b'))
    turnsc, stripsc = parse_a(read_input('c'))

    return solve_a(turnsa, stripsa), solve_b(turnsb, stripsb), solve_c(turnsc, stripsc)


if __name__ == '__main__':
    print(main())
