def parse_a(lines):
    return [list(map(int, line.split())) for line in lines]
    

def parse_b(lines):
    return None


def parse_c(lines):
    return None


def solve_a(data):
    height = len(data)
    rounds = 10
    clapper = data[0][0]
    shout = []

    for round in range(rounds):
        col = (round+1) % 4
        shout = list(data[0])
        new_clapper = clapper if clapper == 1 else data[0][col]

        shout[col] = new_clapper
        print(round, shout)
        insert_pos = max(0, clapper-2) if clapper <= height else (height*2 - clapper)

        for row in range(insert_pos):
            data[row][col] = data[row+1][col]

        data[max(0, insert_pos)][col] = clapper
        
        clapper = new_clapper

    print(''.join(str(person) for person in shout))


def solve_b(data):
    return None


def solve_c(data):
    return None


def read_input(part):
    data = [line.rstrip() for line in open(f'input/2024-5{part}.txt').readlines()]

    return data


def main():
    dataa = parse_a(read_input('a'))
    datab = parse_b(read_input('b'))
    datac = parse_c(read_input('c'))

    return solve_a(dataa), solve_b(datab), solve_c(datac)


if __name__ == '__main__':
    print(main())
