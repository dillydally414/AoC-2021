from day import Day
from day_05 import Point

sampleFile = open('../samples/day_09.txt', 'r')
problemFile = open('../problems/day_09.txt', 'r')


def find_basin(basin, a):
    new_basin = basin.copy()
    for location in basin:
        [row, col] = [location.x, location.y]
        if row > 0 and a[row - 1][col] < 9:
            new_basin.add(Point(row - 1, col))
        if row < len(a) - 1 and a[row + 1][col] < 9:
            new_basin.add(Point(row + 1, col))
        if col > 0 and a[row][col - 1] < 9:
            new_basin.add(Point(row, col - 1))
        if col < len(a[row]) - 1 and a[row][col + 1] < 9:
            new_basin.add(Point(row, col + 1))
    return basin if basin == new_basin else find_basin(new_basin, a)


class Day09(Day):
    sample = [[int(num) for num in list(line.strip())] for line in sampleFile.readlines()]
    problem = [[int(num) for num in list(line.strip())] for line in problemFile.readlines()]
    part1_sample_ans = 15
    part2_sample_ans = 1134

    def part1(self, a):
        tot = 0
        for row in range(len(a)):
            for col in range(len(a[row])):
                height = a[row][col]
                tot += (height + 1) if (row == 0 or a[row - 1][col] > height) and (
                        row == len(a) - 1 or a[row + 1][col] > height) and (
                                               col == 0 or a[row][col - 1] > height) and (
                                               col == len(a[row]) - 1 or a[row][col + 1] > height) else 0
        return tot

    def part2(self, a):
        largest_basins = [0, 0, 0]
        for row in range(len(a)):
            for col in range(len(a[row])):
                height = a[row][col]
                if (row == 0 or a[row - 1][col] > height) and (
                        row == len(a) - 1 or a[row + 1][col] > height) and (
                        col == 0 or a[row][col - 1] > height) and (
                        col == len(a[row]) - 1 or a[row][col + 1] > height):
                    basin = find_basin({Point(row, col)}, a)
                    if len(basin) > largest_basins[0]:
                        largest_basins[0] = len(basin)
                    largest_basins.sort()

        return largest_basins[0] * largest_basins[1] * largest_basins[2]
