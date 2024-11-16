from itertools import batched


def solve(s, batch_size):
    enemies = { 'x': 0, 'A': 0, 'B': 1, 'C': 3, 'D': 5 }
    bonus = { 0: 0, 1: 0, 2: 2, 3: 6 }

    def calculate_batch(batch):
        enemy_count = sum(c != 'x' for c in batch)
        return sum(enemies[enemy] for enemy in batch) + bonus[enemy_count]
    
    return sum(calculate_batch(batch) for batch in batched(s, batch_size))


if __name__ == '__main__':
    data = open('input/2024-1.txt').readlines()

    print(solve(data[0].rstrip(), 1))
    print(solve(data[1].rstrip(), 2))
    print(solve(data[2].rstrip(), 3))