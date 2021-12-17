from day import Day
from day_05 import Point

sampleFile = open('../samples/day_17.txt', 'r')
problemFile = open('../problems/day_17.txt', 'r')


def max_height_hits_target(x_velocity, y_velocity, top_left, bottom_right):
    curr = Point(0, 0)
    hits_target = False
    max_height = 0
    while (((curr.x <= bottom_right.x and x_velocity >= 0) or (curr.x >= top_left.x and x_velocity <= 0)) and
           ((curr.y <= top_left.y and y_velocity >= 0) or curr.y >= bottom_right.y)):
        curr = Point(curr.x + x_velocity, curr.y + y_velocity)
        y_velocity -= 1
        x_velocity += 1 if x_velocity < 0 else (-1 if x_velocity > 0 else 0)
        max_height = max(curr.y, max_height)
        hits_target = hits_target or (top_left.x <= curr.x <= bottom_right.x
                                      and bottom_right.y <= curr.y <= top_left.y)
    return max_height if hits_target else -1


class Day17(Day):
    sample = [[int(coord[coord.index("=") + 1:coord.index("..")]), int(coord[coord.index("..") + 2:])]
              for coord in sampleFile.readline().split(', ')]
    problem = [[int(coord[coord.index("=") + 1:coord.index("..")]), int(coord[coord.index("..") + 2:])]
               for coord in problemFile.readline().split(', ')]
    part1_sample_ans = 45
    part2_sample_ans = 112

    def part1(self, a):
        top_left = Point(a[0][0], a[1][1])
        bottom_right = Point(a[0][1], a[1][0])
        max_height = 0
        for x_velocity in range(min(0, min(a[0])), max(0, max(a[0])) + 1):
            for y_velocity in range(min(0, min(a[1])), max(0, max(a[1]), abs(min(a[1]))) + 1):
                max_height = max(max_height, max_height_hits_target(x_velocity, y_velocity, top_left, bottom_right))
        return max_height

    def part2(self, a):
        top_left = Point(a[0][0], a[1][1])
        bottom_right = Point(a[0][1], a[1][0])
        count = 0
        for x_velocity in range(min(0, min(a[0])), max(0, max(a[0])) + 1):
            for y_velocity in range(min(0, min(a[1])), max(0, max(a[1]), abs(min(a[1]))) + 1):
                if max_height_hits_target(x_velocity, y_velocity, top_left, bottom_right) > -1:
                    count += 1
        return count
