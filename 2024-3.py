def parse_a(lines):
    return None
    

def parse_b(lines):
    return None


def parse_c(lines):
    return None


def solve_a(data):
    return None


def solve_b(data):
    return None


def solve_c(data):
    return None


def read_input(part):
    data = [line.rstrip() for line in open(f'input/2024-2{part}.txt').readlines()]

    return data


def main():
    dataa = parse_a(read_input('a'))
    datab = parse_a(read_input('b'))
    datac = parse_a(read_input('c'))

    return solve_a(dataa), solve_b(datab), solve_c(datac)


if __name__ == '__main__':
    print(main())
