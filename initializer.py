from os import path
from sys import argv

program_file = lambda day: f"""def parse_a(lines):
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


def read_input(day, part):
    data = [line.rstrip() for line in open(f'input/2024-{day}{{part}}.txt').readlines()]

    return data


def main():
    dataa = parse_a(read_input('a'))
    datab = parse_b(read_input('b'))
    datac = parse_c(read_input('c'))

    return solve_a(dataa), solve_b(datab), solve_c(datac)


if __name__ == '__main__':
    print(main())
"""

if __name__ == '__main__':
    day = argv[1]
    
    program = f'2024-{day}.py'

    if not path.isfile(program):
        with open(program, 'w') as g:
            g.write(program_file(day))

    for variant in 'abc':
        inp = f'input/2024-{day}{variant}.txt'

        if not path.isfile(inp):
            with open(inp, 'w') as g:
                g.write('')