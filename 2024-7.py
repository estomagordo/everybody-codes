from collections import defaultdict


def parse_a(lines):
    plans = defaultdict(list)

    for line in lines:
        name, plan = line.split(':')
        plans[name] = plan.split(',')

    return plans
    

def parse_b(lines):
    return None


def parse_c(lines):
    return None


def solve_a(plans):
    duration = 10
    runs = {}

    for name, plan in plans.items():
        essence = 0
        power = 10

        for step in range(duration):
            instruction = plan[step % len(plan)]

            if instruction == '+':
                power += 1
            if instruction == '-' and power > 0:
                power -= 1

            essence += power

        runs[essence] = name

    out = []

    for essence in sorted(runs.keys(), reverse=True):
        out.append(runs[essence])

    return ''.join(out)


def solve_b(plans):
    track = """S-=++=-==++=++=-=+=-=+=+=--=-=++=-==++=-+=-=+=-=+=+=++=-+==++=++=-=-=--
-                                                                     -
=                                                                     =
+                                                                     +
=                                                                     +
+                                                                     =
=                                                                     =
-                                                                     -
--==++++==+=+++-=+=-=+=-+-=+-=+-=+=-=+=--=+++=++=+++==++==--=+=++==+++-"""

    matrix = track.split('\n')
    
    height = len(matrix)
    width = len(matrix[0])

    runs = {}

    for name, plan in plans.items():
        essence = 0
        power = 10
        loops = 0
        steps = 0
        y = 0
        x = 1

        while loops < 10:
            instruction = plan[steps % len(plan)]
            terrain = matrix[y][x]

            if terrain == '+':
                power += 1
            elif terrain == '-':
                power -= 1
            elif instruction == '+':
                power += 1
            elif instruction == '-' and power > 0:
                power -= 1

            essence += power

            if y == 0:
                if x < width-1:
                    x += 1
                else:
                    y += 1
            elif y == height-1:
                if x > 0:
                    x -= 1
                else:
                    y -= 1
            elif x == 0:
                y -= 1
            else:
                y += 1

            if y == 0 and x == 1:
                loops += 1

            steps += 1

        runs[essence] = name

    out = []

    for essence in sorted(runs.keys(), reverse=True):
        out.append(runs[essence])

    return ''.join(out)


def solve_c(rival):
    track = """S+= +=-== +=++=     =+=+=--=    =-= ++=     +=-  =+=++=-+==+ =++=-=-=--
- + +   + =   =     =      =   == = - -     - =  =         =-=        -
= + + +-- =-= ==-==-= --++ +  == == = +     - =  =    ==++=    =++=-=++
+ + + =     +         =  + + == == ++ =     = =  ==   =   = =++=       
= = + + +== +==     =++ == =+=  =  +  +==-=++ =   =++ --= + =          
+ ==- = + =   = =+= =   =       ++--          +     =   = = =--= ==++==
=     ==- ==+-- = = = ++= +=--      ==+ ==--= +--+=-= ==- ==   =+=    =
-               = = = =   +  +  ==+ = = +   =        ++    =          -
-               = + + =   +  -  = + = = +   =        +     =          -
--==++++==+=+++-= =-= =-+-=  =+-= =-= =--   +=++=+++==     -=+=++==+++-"""

    matrix = track.split('\n')
    
    height = len(matrix)
    width = len(matrix[0])

    def play(plan):
        essence = 0
        power = 10
        loops = 0
        steps = 0
        y = 0
        x = 1
        dy = 0
        dx = 1

        while loops < 2024:
            instruction = plan[steps % len(plan)]
            terrain = matrix[y][x]

            if terrain == '+':
                power += 1
            elif terrain == '-':
                power -= 1
            elif instruction == '+':
                power += 1
            elif instruction == '-' and power > 0:
                power -= 1

            essence += power

            if dx == 1:
                if x < width - 1 and matrix[y][x+1] != ' ':
                    x += 1
                elif y > 0 and matrix[y-1][x] != ' ':
                    dx = 0
                    dy = -1
                    y -= 1
                else:
                    dx = 0
                    dy = 1
                    y += 1
            elif dx == -1:
                if x > 0 and matrix[y][x-1] != ' ':
                    x -= 1
                elif y > 0 and matrix[y-1][x] != ' ':
                    dx = 0
                    dy = -1
                    y -= 1
                else:
                    dx = 0
                    dy = 1
                    y += 1
            elif dy == 1:
                if y < height - 1 and matrix[y+1][x] != ' ':
                    y += 1
                elif x > 0 and matrix[y][x-1] != ' ':
                    dy = 0
                    dx = -1
                    x -= 1
                else:
                    dy = 0
                    dx = 1
                    x += 1
            elif dy == -1:
                if y > 0 and matrix[y-1][x] != ' ':
                    y -= 1
                elif x > 0 and matrix[y][x-1] != ' ':
                    dy = 0
                    dx = -1
                    x -= 1
                else:
                    dy = 0
                    dx = 1
                    x += 1

            if y == 0 and x == 1:
                loops += 1

            steps += 1

        return essence

    rival_score = play(rival)
    print('rival score', rival_score)
    better_count = 0

    def explore_plans(plan):
        nonlocal better_count
        if len(plan) == 11:
            essence = play(plan)

            if essence > rival_score:
                better_count += 1
                print(plan, better_count)
            
            return
        
        moves = []

        if plan.count('+') < 5:
            moves.append('+')
        if plan.count('-') < 3:
            moves.append('-')
        if plan.count('=') < 3:
            moves.append('=')

        for move in moves:
            plan.append(move)
            explore_plans(plan)
            plan.pop()

    explore_plans([])

    return better_count


def read_input(part):
    data = [line.rstrip() for line in open(f'input/2024-7{part}.txt').readlines()]

    return data


def main():
    dataa = parse_a(read_input('a'))
    datab = parse_a(read_input('b'))
    datac = parse_a(read_input('c'))

    return solve_a(dataa), solve_b(datab), solve_c(datac['A'])


if __name__ == '__main__':
    print(main())
