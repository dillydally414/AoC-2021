from day import Day
from day_05 import Point

sampleFile = open('../samples/day_11.txt', 'r')
problemFile = open('../problems/day_11.txt', 'r')


def get_neighbors(a, octopus):
    [row, col] = [octopus.x, octopus.y]
    neighbors = set()
    for i in range(max(0, row - 1), min(row + 2, len(a))):
        for j in range(max(0, col - 1), min(col + 2, len(a[i]))):
            neighbors.add(Point(i, j))
    neighbors.remove(octopus)
    return neighbors


def flash(flashing, flashed, a):
    new_flashing = set()
    for octopus in flashing:
        neighbors = get_neighbors(a, octopus)
        for neighbor in neighbors:
            if neighbor not in new_flashing | flashed | flashing:
                a[neighbor.x][neighbor.y] += 1
                if a[neighbor.x][neighbor.y] > 9:
                    new_flashing.add(neighbor)
    return flashing | flashed if len(new_flashing) == 0 else flash(new_flashing, flashing | flashed, a)


def step(a):
    new_a = [row[:] for row in a]
    flashing = set()
    for row in range(len(a)):
        for col in range(len(a[row])):
            new_a[row][col] += 1
            if new_a[row][col] > 9:
                flashing.add(Point(row, col))
    flashing = flash(flashing, set(), new_a)
    for octopus in flashing:
        new_a[octopus.x][octopus.y] = 0
    return [new_a, len(flashing)]


class Day11(Day):
    sample = [[int(c) for c in list(line.strip())] for line in sampleFile.readlines()]
    problem = [[int(c) for c in list(line.strip())] for line in problemFile.readlines()]
    part1_sample_ans = 1656
    part2_sample_ans = 195

    def part1(self, a):
        a_copy = [row[:] for row in a]
        tot = 0
        for i in range(100):
            [a_copy, count] = step(a_copy)
            tot += count
        return tot

    def part2(self, a):
        a_copy = [row[:] for row in a]
        i = 0
        while not all([all([(num == 0) for num in row]) for row in a_copy]):
            [a_copy, count] = step(a_copy)
            i += 1
        return i
