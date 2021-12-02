from day import Day

sampleFile = open('../samples/day_01.txt', 'r')
problemFile = open('../problems/day_01.txt', 'r')


def convert_to_int(a):
    b = [0] * a.__len__()
    for x in range(len(a)):
        b[x] = int(a[x])
    return b


class Day01(Day):
    sample = convert_to_int(sampleFile.readlines())
    problem = convert_to_int(problemFile.readlines())
    part1_sample_ans = 7
    part2_sample_ans = 5

    def part1(self, a):
        count = 0
        for x in range(1, len(a)):
            if a[x] > a[x - 1]:
                count += 1
        return count

    def part2(self, a):
        count = 0
        for x in range(3, len(a)):
            if a[x] > a[x - 3]:
                count += 1
        return count

