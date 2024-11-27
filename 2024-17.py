from heapq import heappop, heappush
from itertools import combinations


def parse_a(lines):
    return [list(line) for line in lines]
    

def parse_b(lines):
    return None


def parse_c(lines):
    return None


def solve_a(grid):
    stars = {(y, x): [] for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] == '*'}

    for a, b in combinations(stars, 2):
        distance = abs(a[0]-b[0]) + abs(a[1]-b[1])
        heappush(stars[a], (distance, b))
        heappush(stars[b], (distance, a))

    first = list(stars.keys())[0]
    seen = {first}
    length = 0
    edges = stars[first]

    while len(seen) < len(stars):
        distance, destination = heappop(edges)

        if destination not in seen:
            length += distance
            seen.add(destination)

            for new_distance, new_destination in stars[destination]:
                heappush(edges, (new_distance, new_destination))

    return length + len(stars)


def solve_b(data):
    return None


def solve_c(grid):
    stars = {(y, x): [] for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] == '*'}

    for a, b in combinations(stars, 2):
        distance = abs(a[0]-b[0]) + abs(a[1]-b[1])
        heappush(stars[a], (distance, b))
        heappush(stars[b], (distance, a))

    first = list(stars.keys())[0]
    seen = {first}
    currseen = {first}
    length = 0
    edges = stars[first]
    constellations = []
    limit = 6

    while len(seen) < len(stars):
        distance, destination = heappop(edges)
        
        if distance >= limit:
            constellations.append(length + len(currseen))
            newfirst = [star for star in stars.keys() if star not in seen][0]
            length = 0
            seen.add(newfirst)
            currseen = {newfirst}
            edges = stars[newfirst]
            continue

        if destination not in seen:
            length += distance
            seen.add(destination)
            currseen.add(destination)

            for new_distance, new_destination in stars[destination]:
                heappush(edges, (new_distance, new_destination))

    constellations.append(length + len(currseen))
    
    constellations.sort()

    return constellations[-3]*constellations[-2]*constellations[-1]


def read_input(part):
    data = [line.rstrip() for line in open(f'input/2024-17{part}.txt').readlines()]

    return data


def main():
    dataa = parse_a(read_input('a'))
    datab = parse_a(read_input('b'))
    datac = parse_a(read_input('c'))

    return solve_a(dataa), solve_a(datab), solve_c(datac)


if __name__ == '__main__':
    print(main())
