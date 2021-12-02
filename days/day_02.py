from day import Day

sampleFile = open('../samples/day_02.txt', 'r')
problemFile = open('../problems/day_02.txt', 'r')


class Day02(Day):
    sample = sampleFile.readlines()
    problem = problemFile.readlines()
    part1_sample_ans = 150
    part2_sample_ans = 900

    def part1(self, a):
        x_pos = 0
        depth_pos = 0
        for x in range(len(a)):
            val = int(a[x][a[x].index(' ') + 1:])
            if a[x].startswith('up'):
                depth_pos -= val
            elif a[x].startswith('down'):
                depth_pos += val
            else:
                x_pos += val
        return x_pos * depth_pos

    def part2(self, a):
        aim = 0
        x_pos = 0
        depth_pos = 0
        for x in range(len(a)):
            val = int(a[x][a[x].index(' ') + 1:])
            if a[x].startswith('up'):
                aim -= val
            elif a[x].startswith('down'):
                aim += val
            else:
                x_pos += val
                depth_pos += val * aim
        return x_pos * depth_pos

