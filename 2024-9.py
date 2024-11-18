from functools import cache
from heapq import heappop, heappush


@cache
def calculate(beetles, sparkballs):
    def h(balls):
        return balls // beetles[-1] + (balls % beetles[-1] > 0)
    
    frontier = [(h(sparkballs), 0, sparkballs)]
    seen = set()

    while True:
        ideal, steps, balls = heappop(frontier)

        if ideal == steps:
            return steps
        
        if balls in seen:
            continue
        
        seen.add(balls)

        for beetle in beetles:
            if beetle > balls or (balls-beetle) in seen:
                continue

            heappush(frontier, (steps+1 + h(balls-beetle), steps+1, balls-beetle))


def parse_a(lines):
    return [int(line) for line in lines]
    

def parse_b(lines):
    return None


def parse_c(lines):
    return None


def solve_a(sparkballs):
    beetles = [1, 3, 5, 10]

    def calc(sparkball):
        count = 0

        while sparkball > 0:
            for beetle in beetles[::-1]:
                if beetle <= sparkball:
                    sparkball -= beetle
                    count += 1
                    break

        return count
    
    return sum(calc(sparkball) for sparkball in sparkballs)


def solve_b(sparkballs):
    beetles = (1, 3, 5, 10, 15, 16, 20, 24, 25, 30)
    
    return sum(calculate(beetles, sparkball) for sparkball in sparkballs)


def solve_c(sparkballs):
    beetles = (1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101)

    maxdiff = 100

    def calc(sparkball):
        a = sparkball//2
        b = sparkball-a

        best_score = calculate(beetles, a) + calculate(beetles, b)

        while True:
            a -= 1
            b += 1

            if b-a > maxdiff:
                break

            best_score = min(best_score, calculate(beetles, a) + calculate(beetles, b))

        return best_score
    
    return sum(calc(sparkball) for sparkball in sparkballs)


def read_input(part):
    data = [line.rstrip() for line in open(f'input/2024-9{part}.txt').readlines()]

    return data


def main():
    dataa = parse_a(read_input('a'))
    datab = parse_a(read_input('b'))
    datac = parse_a(read_input('c'))

    return solve_a(dataa), solve_b(datab), solve_c(datac)


if __name__ == '__main__':
    print(main())
