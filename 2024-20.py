from heapq import heappop, heappush


def parse_a(lines):
    return [list(line) for line in lines]
    

def parse_b(lines):
    return None


def parse_c(lines):
    return None


def turns(dy):
    if dy == 0:
        return ((1, 0), (-1, 0))
    
    return ((0, 1), (0, -1))


def solve_a(grid):
    t = 100
    start_altitude = 1000
    height = len(grid)
    width = len(grid[0])
    sy = 0
    sx = 0

    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == 'S':
                sy = y
                sx = x

    frontier = []
    bests = {}

    if sy > 0:
        heappush(frontier, (-start_altitude - t, start_altitude, t, sy, sx, -1, 0))
        bests[(sy, sx, -1, 0, t)] = start_altitude
    if sy < height-1:
        heappush(frontier, (-start_altitude - t, start_altitude, t, sy, sx, 1, 0))
        bests[(sy, sx, -1, 0, t)] = start_altitude
    if sx > 0:
        heappush(frontier, (-start_altitude - t, start_altitude, t, sy, sx, 0, -1))
        bests[(sy, sx, -1, 0, t)] = start_altitude
    if sx < width-1:
        heappush(frontier, (-start_altitude - t, start_altitude, t, sy, sx, 0, 1))
        bests[(sy, sx, -1, 0, t)] = start_altitude

    while frontier:
        _, altitude, time, y, x, dy, dx = heappop(frontier)

        if time == 0:
            return altitude

        ntime = time-1
        
        moves = [[y+dy, x+dx, dy, dx]]

        for ndy, ndx in turns(dy):
            moves.append([y+ndy, x+ndx, ndy, ndx])

        for ny, nx, ndy, ndx in moves:
            if 0 <= ny < height and 0 <= nx < width and grid[ny][nx] != '#':
                c = grid[ny][nx]
                daltitude = 1 if c == '+' else -2 if c == '-' else -1
                naltitude = altitude+daltitude

                if naltitude < 1:
                    continue

                h = -naltitude - ntime
                seenkey = (ny, nx, ndy, ndx, ntime)

                if seenkey not in bests or bests[seenkey] < naltitude:
                    bests[seenkey] = naltitude
                    heappush(frontier, (h, naltitude, ntime, ny, nx, ndy, ndx))
                    

def solve_b(grid):
    start_altitude = 10000
    checkpoint_target = 'ABC'
    height = len(grid)
    width = len(grid[0])
    sy = 0
    sx = 0

    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == 'S':
                sy = y
                sx = x
                
    bests = {}
    frontier = []

    if sy > 0:
        frontier.append((0, start_altitude, sy, sx, -1, 0, ''))
        bests[(sy, sx, -1, 0, 0, '')] = start_altitude
    if sy < height-1:
        frontier.append((0, start_altitude, sy, sx, 1, 0, ''))
        bests[(sy, sx, 1, 0, 0, '')] = start_altitude
    if sx > 0:
        frontier.append((0, start_altitude, sy, sx, 0, -1, ''))
        bests[(sy, sx, 0, -1, 0, '')] = start_altitude
    if sx < width-1:
        frontier.append((0, start_altitude, sy, sx, 0, 1, ''))
        bests[(sy, sx, 0, 1, 0, '')] = start_altitude

    latest = 0

    for t, altitude, y, x, dy, dx, checkpoints in frontier:
        if t > latest:
            latest = t
            print(t)

        if y == sy and x == sx and altitude >= start_altitude and checkpoints == checkpoint_target:
            return t
        
        moves = [[y+dy, x+dx, dy, dx]]

        for ndy, ndx in turns(dy):
            moves.append([y+ndy, x+ndx, ndy, ndx])

        for ny, nx, ndy, ndx in moves:
            if 0 <= ny < height and 0 <= nx < width and grid[ny][nx] != '#':
                c = grid[ny][nx]
                daltitude = 1 if c == '+' else -2 if c == '-' else -1
                naltitude = altitude+daltitude

                if naltitude < 1:
                    continue

                newcheck = str(checkpoints)

                if c.isalpha() and c != 'S':
                    cpos = checkpoint_target.find(c)

                    if c not in newcheck and len(newcheck) != cpos:
                        continue

                    if c not in newcheck:
                        newcheck += c

                seenkey = (ny, nx, ndy, ndx, t, newcheck)

                if seenkey not in bests or bests[seenkey] < naltitude:
                    bests[seenkey] = naltitude
                    frontier.append((t+1, naltitude, ny, nx, ndy, ndx, newcheck))


def solve_c(data):
    return None


def read_input(part):
    data = [line.rstrip() for line in open(f'input/2024-20{part}.txt').readlines()]

    return data


def main():
    dataa = parse_a(read_input('a'))
    datab = parse_a(read_input('b'))
    datac = parse_c(read_input('c'))

    return solve_a(dataa), solve_b(datab), solve_c(datac)


if __name__ == '__main__':
    print(main())
