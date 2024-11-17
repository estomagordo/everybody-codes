def parse_a(lines):
    return [int(line) for line in lines]
    

def parse_b(lines):
    return None


def parse_c(lines):
    return None


def solve_a(data):
    minimum = min(data)

    return sum(nail-minimum for nail in data)


def solve_b(data):
    return None


def solve_c(data):
    n = len(data)
    average = sum(data) // n

    def calculate(target):
        return sum(abs(nail-target) for nail in data)
    
    return min(calculate(target) for target in range(average-50000, average+200000))


def read_input(part):
    data = [line.rstrip() for line in open(f'input/2024-4{part}.txt').readlines()]

    return data


def main():
    dataa = parse_a(read_input('a'))
    datab = parse_a(read_input('b'))
    datac = parse_a(read_input('c'))

    return solve_a(dataa), solve_a(datab), solve_c(datac)


if __name__ == '__main__':
    print(main())