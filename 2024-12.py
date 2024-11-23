def parse_a(lines):
    catapults = []
    targets = []

    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            if c == 'T':
                targets.append((y, x, 1))
            elif c == 'H':
                targets.append((y, x, 2))
            elif c.isalpha():
                catapults.append((c, y, x))

    targets.sort(key=lambda target: (target[1], target[0]))
    
    return catapults, targets
    

def parse_b(lines):
    return None


def parse_c(lines):
    meteors = [list(map(int, line.split())) for line in lines]
    height = max(meteor[1] for meteor in meteors)

    return [[height-meteor[1], meteor[0]] for meteor in meteors], height


def trajectory(y, x, power, floor):
    cells = []
    rising = power
    planing = power

    while y < floor:
        cells.append((y, x))
        x += 1

        if rising:
            y -= 1
            rising -= 1
        elif planing:
            planing -= 1
        else:
            y += 1

    return cells


def solve_a(catapults, targets):
    points = 0
    floor = max(target[0] for target in targets)

    for y, x, value in targets:
        result = 0

        for c, cy, cx in catapults:
            catval = ord(c) - ord('A') + 1

            for power in range(1, 40):
                for ty, tx in trajectory(cy, cx, power, floor+1):
                    if (ty, tx) == (y, x):
                        result = max(result, catval*power*value)
                        break

        if result == 0:
            print('panic!')
        
        points += result

    return points


def solve_b(data):
    return None


def solve_c(meteors, height):
    maxwait = 600
    maxpower = 1300
    score = 0
    catapults = [
        (height, 0, 1),
        (height-1, 0, 2),
        (height-2, 0, 3),
    ]

    highest_power = 0
    latest_delay = 0

    for mi, meteor in enumerate(meteors):
        print(mi, highest_power, latest_delay)
        my, mx = meteor
        origmy = my
        origmx = mx
        best = (10**6, 10**6)
        metrajectory = []
        
        while my <= height and mx >= 0:
            metrajectory.append((my, mx))
            my += 1
            mx -= 1

        for cy, cx, value in catapults:
            stoplook = len(metrajectory)
            for delay in range(maxwait):
                for power in range(1, maxpower):
                    path = trajectory(cy, cx, power, height+1)

                    for i in range(stoplook):
                        if i >= len(path):
                            break
                        
                        if i+delay >= len(metrajectory):
                            break
                        if metrajectory[i+delay] == path[i]:
                            
                            cmy, cmx = metrajectory[i]
                            # print('Hit!', i, cy, cx, cmy, cmx, origmy, origmx, value, power, delay, value*power)
                            candidate = (height-cmy, value*power)
                            if candidate < best:
                                best = candidate
                                highest_power = max(highest_power, power)
                                latest_delay = max(latest_delay, delay)
                            stoplook = i
                            break

        if best == (10**6, 10**6):
            print('panic!')

        score += best[1]

    return score


def read_input(part):
    data = [line.rstrip() for line in open(f'input/2024-12{part}.txt').readlines()]

    return data


def main():
    catapultsa, targetsa = parse_a(read_input('a'))
    catapultsb, targetsb = parse_a(read_input('b'))
    meteorsc, heightc = parse_c(read_input('c'))

    return solve_a(catapultsa, targetsa), solve_a(catapultsb, targetsb), solve_c(meteorsc, heightc)


if __name__ == '__main__':
    print(main())
