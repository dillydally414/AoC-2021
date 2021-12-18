from math import ceil, floor

from day import Day

sampleFile = open('../samples/day_18.txt', 'r')
problemFile = open('../problems/day_18.txt', 'r')


def parse_list(line):
    parsed = []
    level = 0
    middle_comma = -1
    for i in range(1, len(line) - 2):
        level += 1 if line[i] == '[' else -1 if line[i] == ']' else 0
        if level == 0 and line[i] == ',':
            middle_comma = i
            break
    left_side = line[1:middle_comma]
    right_side = line[middle_comma + 1:len(line) - 1]
    parsed.append(int(left_side) if len(left_side) == 1 else parse_list(left_side))
    parsed.append(int(right_side) if len(right_side) == 1 else parse_list(right_side))
    return parsed


def deep_copy(expr):
    return [
        expr[0] if isinstance(expr[0], int) else deep_copy(expr[0]),
        expr[1] if isinstance(expr[1], int) else deep_copy(expr[1])
    ]


def add_closest_left(value, expr, abcd):
    new_expr = deep_copy(expr)
    abcde_copy = abcd[:]
    abcde_copy.append(0)
    while sum(abcde_copy) > 0:
        abcde_copy[4] -= 1
        if abcde_copy[4] == -1:
            abcde_copy[4] = 1
            abcde_copy[3] -= 1
        if abcde_copy[3] == -1:
            abcde_copy[3] = 1
            abcde_copy[2] -= 1
        if abcde_copy[2] == -1:
            abcde_copy[2] = 1
            abcde_copy[1] -= 1
        if abcde_copy[1] == -1:
            abcde_copy[1] = 1
            abcde_copy[0] -= 1
        if abcde_copy[0] == -1:
            break
        if isinstance(expr[abcde_copy[0]], int):
            new_expr[abcde_copy[0]] += value
            return new_expr
        elif isinstance(expr[abcde_copy[0]][abcde_copy[1]], int):
            new_expr[abcde_copy[0]][abcde_copy[1]] += value
            return new_expr
        elif isinstance(expr[abcde_copy[0]][abcde_copy[1]][abcde_copy[2]], int):
            new_expr[abcde_copy[0]][abcde_copy[1]][abcde_copy[2]] += value
            return new_expr
        elif isinstance(expr[abcde_copy[0]][abcde_copy[1]][abcde_copy[2]][abcde_copy[3]], int):
            new_expr[abcde_copy[0]][abcde_copy[1]][abcde_copy[2]][abcde_copy[3]] += value
            return new_expr
        elif isinstance(expr[abcde_copy[0]][abcde_copy[1]][abcde_copy[2]][abcde_copy[3]][abcde_copy[4]], int):
            new_expr[abcde_copy[0]][abcde_copy[1]][abcde_copy[2]][abcde_copy[3]][abcde_copy[4]] += value
            return new_expr
    return new_expr


def add_closest_right(value, expr, abcd):
    new_expr = deep_copy(expr)
    abcde_copy = abcd[:]
    abcde_copy.append(1)
    while sum(abcde_copy) < 16:
        abcde_copy[4] += 1
        if abcde_copy[4] == 2:
            abcde_copy[4] = 0
            abcde_copy[3] += 1
        if abcde_copy[3] == 2:
            abcde_copy[3] = 0
            abcde_copy[2] += 1
        if abcde_copy[2] == 2:
            abcde_copy[2] = 0
            abcde_copy[1] += 1
        if abcde_copy[1] == 2:
            abcde_copy[1] = 0
            abcde_copy[0] += 1
        if abcde_copy[0] == 2:
            break
        if isinstance(expr[abcde_copy[0]], int):
            new_expr[abcde_copy[0]] += value
            return new_expr
        elif isinstance(expr[abcde_copy[0]][abcde_copy[1]], int):
            new_expr[abcde_copy[0]][abcde_copy[1]] += value
            return new_expr
        elif isinstance(expr[abcde_copy[0]][abcde_copy[1]][abcde_copy[2]], int):
            new_expr[abcde_copy[0]][abcde_copy[1]][abcde_copy[2]] += value
            return new_expr
        elif isinstance(expr[abcde_copy[0]][abcde_copy[1]][abcde_copy[2]][abcde_copy[3]], int):
            new_expr[abcde_copy[0]][abcde_copy[1]][abcde_copy[2]][abcde_copy[3]] += value
            return new_expr
        elif isinstance(expr[abcde_copy[0]][abcde_copy[1]][abcde_copy[2]][abcde_copy[3]][abcde_copy[4]], int):
            new_expr[abcde_copy[0]][abcde_copy[1]][abcde_copy[2]][abcde_copy[3]][abcde_copy[4]] += value
            return new_expr
    return new_expr


def explode(expr):
    left = -1
    right = -1
    abcd = []
    for a in range(2):
        if isinstance(expr[a], int):
            continue
        for b in range(2):
            if isinstance(expr[a][b], int):
                continue
            for c in range(2):
                if isinstance(expr[a][b][c], int):
                    continue
                for d in range(2):
                    if isinstance(expr[a][b][c][d], list):
                        left = expr[a][b][c][d][0]
                        abcd = [a, b, c, d]
                        right = expr[a][b][c][d][1]
                        break
                if left != -1:
                    break
            if left != -1:
                break
        if left != -1:
            break
    if left == -1:
        return expr
    new_expr = deep_copy(expr)
    new_expr[abcd[0]][abcd[1]][abcd[2]][abcd[3]] = 0
    new_expr = add_closest_left(left, new_expr, abcd)
    new_expr = add_closest_right(right, new_expr, abcd)
    return new_expr


def split(expr):
    new_expr = deep_copy(expr)
    for a in range(2):
        if isinstance(expr[a], int):
            if expr[a] >= 10:
                new_expr[a] = [floor(expr[a] / 2), ceil(expr[a] / 2)]
                return new_expr
            continue
        for b in range(2):
            if isinstance(expr[a][b], int):
                if expr[a][b] >= 10:
                    new_expr[a][b] = [floor(expr[a][b] / 2), ceil(expr[a][b] / 2)]
                    return new_expr
                continue
            for c in range(2):
                if isinstance(expr[a][b][c], int):
                    if expr[a][b][c] >= 10:
                        new_expr[a][b][c] = [floor(expr[a][b][c] / 2), ceil(expr[a][b][c] / 2)]
                        return new_expr
                    continue
                for d in range(2):
                    if expr[a][b][c][d] >= 10:
                        new_expr[a][b][c][d] = [floor(expr[a][b][c][d] / 2), ceil(expr[a][b][c][d] / 2)]
                        return new_expr
    return expr


def reduce(expr):
    prev_expr = deep_copy(expr)
    new_expr = explode(expr)
    while new_expr != prev_expr:
        prev_expr = deep_copy(new_expr)
        new_expr = explode(prev_expr)
    prev_expr = deep_copy(new_expr)
    new_expr = split(new_expr)
    while new_expr != prev_expr:
        prev_expr = deep_copy(new_expr)
        new_expr = reduce(prev_expr)
    return new_expr


def magnitude(pair):
    return 3 * (pair[0] if isinstance(pair[0], int) else magnitude(pair[0])) + \
           2 * (pair[1] if isinstance(pair[1], int) else magnitude(pair[1]))


class Day18(Day):
    sample = [parse_list(line.strip()) for line in sampleFile.readlines()]
    problem = [parse_list(line.strip()) for line in problemFile.readlines()]
    part1_sample_ans = 4140
    part2_sample_ans = 3993

    def part1(self, a):
        curr_expr = a[0]
        for i in range(1, len(a)):
            expr_2 = a[i]
            curr_expr = [curr_expr, expr_2]
            curr_expr = reduce(curr_expr)
        return magnitude(curr_expr)

    def part2(self, a):
        max_magnitude = 0
        for i in range(len(a)):
            for j in range(len(a)):
                max_magnitude = max(magnitude(reduce([a[i], a[j]])), magnitude(reduce([a[j], a[i]])), max_magnitude)
        return max_magnitude
