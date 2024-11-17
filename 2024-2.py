def solve_a(words, texts):
    return sum(text.count(word) for word in words for text in texts)


def solve_b(words, texts):
    used_symbols = set()

    for word in words:
        symbols = [word, ''.join(word[::-1])]

        for j, text in enumerate(texts):

            for i in range(len(text) - len(word) + 1):
                if text[i:i+len(word)] in symbols:
                    for k in range(len(word)):
                        used_symbols.add((j, i+k))
    
    return len(used_symbols)


def solve_c(words, texts):
    height = len(texts)
    width = len(texts[0])

    used_symbols = set()
    matrix = [text*2 for text in texts]
    # matrix = matrix*7

    for word in words:
        wordlen = len(word)
        symbols = [word, ''.join(word[::-1])]

        for y in range(height):
            for x in range(width):
                if matrix[y][x:x+wordlen] in symbols:
                    for j in range(x, x+wordlen):
                        reduction = 0 if j < width else width
                        used_symbols.add((y, j-reduction))
                if y + wordlen > len(matrix):
                    continue
                if ''.join(matrix[y+i][x] for i in range(wordlen)) in symbols:
                    for i in range(y, min(y+wordlen, height)):
                        used_symbols.add((i, x))
    
    assert all(0 <= pair[0] < height for pair in used_symbols)
    assert all(0 <= pair[1] < width for pair in used_symbols)
    # for s in sorted(used_symbols):print(s)
    return len(used_symbols)


def read_data(part):
    data = [line.rstrip() for line in open(f'input/2024-2{part}.txt').readlines()]

    words = data[0].split(':')[1].split(',')
    text = data[2:]

    return words, text


if __name__ == '__main__':
    wordsa, texta = read_data('a')
    wordsb, textb = read_data('b')
    wordsc, textc = read_data('c')

    print(solve_a(wordsa, texta))
    print(solve_b(wordsb, textb))
    print(solve_c(wordsc, textc))

# 11976 11942

