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


def solve_c(priests):
    acolytes = 5
    n = 160

    level = 2
    used = 1
    prevthick = 1
    removal = 0
    layers = [[1]]

    while used-removal < n:
        thickness = (prevthick * priests) % acolytes + acolytes
        width = ((level - 1) * 2 + 1)
        used += width * thickness
        level += 1
        prevthick = thickness
        layer = [thickness]

        for i in range(1, width-1):
            layer.append(thickness + layers[-1][i-1])

        layer.append(thickness)
        layers.append(layer)

        removal = 0

        for height in layer[1:-1]:
            removal += (priests * width * height) % acolytes

    return used-removal-n
    # return (used-n) * ((level - 2) * 2 + 1)


def read_input(part):
    data = [line.rstrip() for line in open(f'input/2024-8{part}.txt').readlines()]

    return data


def main():
    dataa = parse_a(read_input('a'))
    datab = parse_a(read_input('b'))
    datac = parse_a(read_input('c'))

    return solve_a(dataa), solve_b(datab), solve_c(datac)


if __name__ == '__main__':
    print(main())
