from collections import defaultdict


def parse_a(lines):
    tree = defaultdict(list)

    for line in lines:
        root, paths = line.split(':')
        
        for node in paths.split(','):
            tree[root].append(node)

    return tree
    

def parse_b(lines):
    return None


def parse_c(lines):
    return None


def solve_a(tree):
    root = 'RR'
    path_lengths = defaultdict(list)
    frontier = [(root, [root])]

    for node, path in frontier:
        if node == '@':
            path_lengths[len(path)].append(''.join(path))
            continue

        for next in tree[node]:
            dpath = list(path)
            dpath.append(next)
            frontier.append((next, dpath))

    for k, v in path_lengths.items():
        if len(v) == 1:
            return v[0]


def solve_b(tree):
    root = 'RR'
    path_lengths = defaultdict(list)
    frontier = [(root, [root])]

    for node, path in frontier:
        if node == '@':
            path_lengths[len(path)].append(''.join(p[0] for p in path))
            continue

        for next in tree[node]:
            dpath = list(path)
            dpath.append(next)
            frontier.append((next, dpath))

    for k, v in path_lengths.items():
        if len(v) == 1:
            return v[0]


def solve_c(tree):
    root = 'RR'
    path_lengths = defaultdict(list)
    frontier = [(root, [root])]

    for node, path in frontier:
        if node == '@':
            path_lengths[len(path)].append(''.join(p[0] for p in path))
            continue

        for next in tree[node]:
            if next in ['ANT', 'BUG']:
                continue
            
            dpath = list(path)
            dpath.append(next)
            frontier.append((next, dpath))

    for k, v in path_lengths.items():
        if len(v) == 1:
            return v[0]


def read_input(part):
    data = [line.rstrip() for line in open(f'input/2024-6{part}.txt').readlines()]

    return data


def main():
    dataa = parse_a(read_input('a'))
    datab = parse_a(read_input('b'))
    datac = parse_a(read_input('c'))
    print(len(datab), len(datac))

    return solve_a(dataa), solve_b(datab), solve_c(datac)


if __name__ == '__main__':
    print(main())
