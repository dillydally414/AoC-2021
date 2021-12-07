from day import Day

sampleFile = open('../samples/day_07.txt', 'r')
problemFile = open('../problems/day_07.txt', 'r')


class Day07(Day):
    sample = [int(str) for str in sampleFile.readline().split(',')]
    problem = [int(str) for str in problemFile.readline().split(',')]
    part1_sample_ans = 37
    part2_sample_ans = 168

    def part1(self, a):
        crabs = sorted(a)
        median = crabs[len(crabs) / 2]
        fuel = sum(abs(num - median) for num in a)
        return fuel

    def part2(self, a):
        mean = sum(a) / (float(len(a)))
        mean_floor = int(mean)
        mean_ceil = mean_floor + 1
        costs = [(i * (i + 1) / 2) for i in range(0, max(a) + 1)]
        mean_floor_fuel = sum(costs[abs(num - mean_floor)] for num in a)
        mean_ceil_fuel = sum(costs[abs(num - mean_ceil)] for num in a)
        return min(mean_floor_fuel, mean_ceil_fuel)
