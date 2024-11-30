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


def distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


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
    checkpoint_locations = {}

    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == 'S':
                sy = y
                sx = x
            elif c.isalpha():
                checkpoint_locations[c] = (y, x)

    remaining_distances = [distance((sy, sx), checkpoint_locations['C'])]
    remaining_distances.append(remaining_distances[-1] + distance(checkpoint_locations['B'], checkpoint_locations['C']))
    remaining_distances.append(remaining_distances[-1] + distance(checkpoint_locations['A'], checkpoint_locations['B']))

    def heuristic(y, x, altitude, checkpoints):
        checkpoint_count = len(checkpoints)
        remaining_distance = 0

        if checkpoint_count == 3:
            remaining_distance = distance((y, x), (sy, sx))
        if checkpoint_count == 2:
            remaining_distance = distance((y, x), checkpoint_locations['C']) + remaining_distances[0]
        if checkpoint_count == 1:
            remaining_distance = distance((y, x), checkpoint_locations['B']) + remaining_distances[1]
        if checkpoint_count == 0:
            remaining_distance = distance((y, x), checkpoint_locations['A']) + remaining_distances[2]

        altitude_difference = max(0, start_altitude-altitude)

        return max(remaining_distance, altitude_difference)
                
    bests = {}
    frontier = []

    if sy > 0:
        h = heuristic(sy, sx, start_altitude, '')
        heappush(frontier, (h, 0, start_altitude, sy, sx, -1, 0, ''))
        bests[(sy, sx, -1, 0, 0, '')] = h
    if sy < height-1:
        h = heuristic(sy, sx, start_altitude, '')
        heappush(frontier, (h, 0, start_altitude, sy, sx, 1, 0, ''))
        bests[(sy, sx, 1, 0, 0, '')] = h
    if sx > 0:
        h = heuristic(sy, sx, start_altitude, '')
        heappush(frontier, (h, 0, start_altitude, sy, sx, 0, -1, ''))
        bests[(sy, sx, 0, -1, 0, '')] = h
    if sx < width-1:
        h = heuristic(sy, sx, start_altitude, '')
        heappush(frontier, (h, 0, start_altitude, sy, sx, 0, 1, ''))
        bests[(sy, sx, 0, 1, 0, '')] = h

    latest = 0

    while frontier:
        h, t, altitude, y, x, dy, dx, checkpoints = heappop(frontier)

        if t > latest:
            latest = t
            print(t, len(frontier), altitude)

        if h == t:
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

                newh = t + heuristic(ny, nx, naltitude, newcheck) + 1
                seenkey = (ny, nx, ndy, ndx, naltitude, newcheck)

                if seenkey not in bests or bests[seenkey] > newh:
                    bests[seenkey] = newh
                    heappush(frontier, (newh, t+1, naltitude, ny, nx, ndy, ndx, newcheck))


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
