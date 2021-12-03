from day import Day

sampleFile = open('../samples/day_01.txt', 'r')
problemFile = open('../problems/day_01.txt', 'r')


def convert_to_int(a):
    b = [0] * a.__len__()
    for x in range(len(a)):
        b[x] = int(a[x])
    return b


def count_greater(a, shift):
    count = 0
    for x in range(shift, len(a)):
        if a[x] > a[x - shift]:
            count += 1
    return count


class Day01(Day):
    sample = convert_to_int(sampleFile.readlines())
    problem = convert_to_int(problemFile.readlines())
    part1_sample_ans = 7
    part2_sample_ans = 5

    def part1(self, a):
        return count_greater(a, 1)

    def part2(self, a):
        return count_greater(a, 3)
