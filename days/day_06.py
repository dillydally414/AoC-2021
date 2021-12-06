from day import Day
import re

sampleFile = open('../samples/day_06.txt', 'r')
problemFile = open('../problems/day_06.txt', 'r')


def update(a):
    updated = [0] * len(a)
    updated[8] = a[0]
    updated[6] = a[0]
    for i in range(1, len(updated)):
        updated[i - 1] += a[i]
    return updated[:]


class Day06(Day):
    sample = [int(str) for str in sampleFile.readline().split(',')]
    problem = [int(str) for str in problemFile.readline().split(',')]
    part1_sample_ans = 5934
    part2_sample_ans = 26984457539

    def part1(self, a):
        curr_count = [a.count(num) for num in range(9)]
        for x in range(80):
            curr_count = update(curr_count)
        return sum(curr_count)

    def part2(self, a):
        curr_count = [a.count(num) for num in range(9)]
        for x in range(256):
            curr_count = update(curr_count)
        return sum(curr_count)
