from day import Day
from day_05 import Point

sampleFile = open('../samples/day_13.txt', 'r')
problemFile = open('../problems/day_13.txt', 'r')


def fold(points, fold):
    new_points = set()
    for point in points:
        if fold[0] == 'x':
            if point.x < fold[1]:
                new_points.add(point)
            else:
                new_points.add(Point(2 * fold[1] - point.x, point.y))
        else:
            if point.y < fold[1]:
                new_points.add(point)
            else:
                new_points.add(Point(point.x, 2 * fold[1] - point.y))
    return new_points


class Day13(Day):
    sample = [line.strip() for line in sampleFile.readlines()]
    problem = [line.strip() for line in problemFile.readlines()]
    part1_sample_ans = 17
    part2_sample_ans = 0

    def part1(self, a):
        points = set()
        folds = []
        for line in a:
            if ',' in line:
                p = line.split(',')
                points.add(Point(int(p[0]), int(p[1])))
            else:
                if len(line) == 0:
                    continue
                if 'x' in line:
                    folds.append(['x', int(line.split('=')[1])])
                else:
                    folds.append(['y', int(line.split('=')[1])])
        points = fold(points, folds[0])
        return len(points)

    def part2(self, a):
        points = set()
        folds = []
        for line in a:
            if ',' in line:
                p = line.split(',')
                points.add(Point(int(p[0]), int(p[1])))
            else:
                if len(line) == 0:
                    continue
                if 'x' in line:
                    folds.append(['x', int(line.split('=')[1])])
                else:
                    folds.append(['y', int(line.split('=')[1])])
        for instr in folds:
            points = fold(points, instr)
        max_x = 0
        max_y = 0
        for point in points:
            max_x = max(max_x, point.x)
            max_y = max(max_y, point.y)
        code = [['.' for i in range(max_x + 1)] for j in range(max_y + 1)]
        for point in points:
            code[point.y][point.x] = '#'
        for line in code:
            print(line)
        return 0
