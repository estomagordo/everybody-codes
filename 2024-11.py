from collections import Counter


def parse_a(lines):
    evolutions = {}

    for line in lines:
        termite, following = line.split(':')
        evolutions[termite] = following.split(',')

    return evolutions
    

def parse_b(line):
    return None


def parse_c(lines):
    return None


def solve_a(evolutions, days, start):
    population = Counter([start])

    for day in range(days):
        newpop = Counter()

        for k, v in population.items():
            for transition in evolutions[k]:
                newpop[transition] += v

        population = newpop

    return sum(population.values())


def solve_b(data):
    return None


def solve_c(evolutions):
    lowest = 10**100
    highest = 0

    for key in evolutions:
        score = solve_a(evolutions, 20, key)
        lowest = min(lowest, score)
        highest = max(highest, score)

    return highest-lowest


def read_input(part):
    data = [line.rstrip() for line in open(f'input/2024-11{part}.txt').readlines()]

    return data


def main():
    dataa = parse_a(read_input('a'))
    datab = parse_a(read_input('b'))
    datac = parse_a(read_input('c'))

    return solve_a(dataa, 4, 'A'), solve_a(datab, 10, 'Z'), solve_c(datac)


if __name__ == '__main__':
    print(main())
