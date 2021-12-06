from day import Day
import re

sampleFile = open('../samples/day_05.txt', 'r')
problemFile = open('../problems/day_05.txt', 'r')


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return self.x * self.y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return other.x == self.x and other.y == self.y


class Line(object):
    def __init__(self, line):
        split = re.split(',| -> ', line)
        self.x1 = int(split[0])
        self.y1 = int(split[1])
        self.x2 = int(split[2])
        self.y2 = int(split[3].strip())
        self.vertical = self.x1 == self.x2
        self.horizontal = self.y1 == self.y2
        self.diagonal = not self.vertical and not self.horizontal
        if self.diagonal:
            self.points = [
                Point(
                    self.x1 + (i if self.x1 < self.x2 else -i),
                    self.y1 + (i if self.y1 < self.y2 else -i)
                ) for i in range(abs(self.x1 - self.x2) + 1)
            ]
        elif self.vertical:
            self.points = [Point(self.x1, y) for y in range(min(self.y1, self.y2), max(self.y1, self.y2) + 1)]
        else:
            self.points = [Point(x, self.y1) for x in range(min(self.x1, self.x2), max(self.x1, self.x2) + 1)]


class Day05(Day):
    sample = [Line(coords) for coords in sampleFile.readlines()]
    problem = [Line(coords) for coords in problemFile.readlines()]
    part1_sample_ans = 5
    part2_sample_ans = 12

    def part1(self, a):
        lines = filter(lambda line: not line.diagonal, a)
        diagram = dict()
        for line in lines:
            for point in line.points:
                if point in diagram:
                    diagram[point] = 1
                else:
                    diagram[point] = 0
        return sum(diagram.values())

    def part2(self, a):
        diagram = dict()
        for line in a:
            for point in line.points:
                if point in diagram:
                    diagram[point] = 1
                else:
                    diagram[point] = 0
        return sum(diagram.values())
