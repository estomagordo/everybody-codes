def parse_a(lines):
    return int(lines[0])
    

def parse_b(lines):
    return None


def parse_c(lines):
    return None


def solve_a(n):
    level = 1
    used = 0

    while used < n:
        used += (level - 1) * 2 + 1
        level += 1

    return (used-n) * ((level - 2) * 2 + 1)


def solve_b(priests):
    acolytes = 1111
    n = 20240000

    level = 2
    used = 1
    prevthick = 1

    while used < n:
        thickness = (prevthick * priests) % acolytes
        used += ((level - 1) * 2 + 1) * thickness
        level += 1
        prevthick = thickness

    return (used-n) * ((level - 2) * 2 + 1)


def solve_c(data):
    return None


def read_input(part):
    data = [line.rstrip() for line in open(f'input/2024-8{part}.txt').readlines()]

    return data


def main():
    dataa = parse_a(read_input('a'))
    datab = parse_a(read_input('b'))
    datac = parse_c(read_input('c'))

    return solve_a(dataa), solve_b(datab), solve_c(datac)


if __name__ == '__main__':
    print(main())
