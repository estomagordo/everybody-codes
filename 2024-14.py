from functools import cache


def parse_a(lines):
    directions = {
        'R': (1, 0, 0),
        'L': (-1, 0, 0),
        'U': (0, 1, 0),
        'D': (0, -1, 0),
        'F': (0, 0, 1),
        'B': (0, 0, -1),
    }

    trees = []

    for line in lines:
        instructions = []

        for instruction in line.split(','):
            direction = instruction[0]
            length = int(instruction[1:])
            instructions.append((directions[direction], length))

        trees.append(instructions)

    return trees
    

def parse_b(lines):
    return None


def parse_c(lines):
    return None


def solve_a(trees):
    extremes = [
        [0, 0],
        [0, 0],
        [0, 0]
    ]

    position = [0, 0, 0]

    for direction, length in trees[0]:
        for i in range(3):
            position[i] += direction[i] * length
            extremes[i][0] = min(extremes[i][0], position[i])
            extremes[i][1] = max(extremes[i][1], position[i])

    return extremes[1][1] - extremes[1][0]


def solve_b(trees):
    seen = set()

    for tree in trees:
        position = [0, 0, 0]

        for direction, length in tree:
            for _ in range(length):
                for i in range(3):
                    position[i] += direction[i]
                seen.add(tuple(position))
    
    return len(seen)

def solve_c(trees):
    leaves = set()
    seen = set()

    for tree in trees:
        position = [0, 0, 0]

        for direction, length in tree:
            for _ in range(length):
                for i in range(3):
                    position[i] += direction[i]
                seen.add(tuple(position))

        leaves.add(tuple(position))

    @cache
    def distance(start, goal):
        used = {start}
        frontier = [(0, start)]

        for d, pos in frontier:
            if pos == goal:
                print(d)
                return d
            
            used.add(pos)
            
            for delta in (-1, 1):
                for dimension in range(3):
                    step = list(pos)
                    step[dimension] += delta
                    t = tuple(step)

                    if t in seen and t not in used:
                        frontier.append((d+1, t))

    height = max(leaf[1] for leaf in leaves)
    best = 10**6
    print(height, len(leaves))
    print(leaves)

    for y in range(height+1):
        start = (0, y, 0)
        score = sum(distance(start, leaf) for leaf in leaves)
        best = min(best, score)

    return best


def read_input(part):
    data = [line.rstrip() for line in open(f'input/2024-14{part}.txt').readlines()]

    return data


def main():
    dataa = parse_a(read_input('a'))
    datab = parse_a(read_input('b'))
    datac = parse_a(read_input('c'))

    return solve_a(dataa), solve_b(datab), solve_c(datac)


if __name__ == '__main__':
    print(main())
