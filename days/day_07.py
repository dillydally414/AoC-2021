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
        costs = [(i * (i + 1) / 2) for i in range(0, max(a) + 1)]
        fuel = costs[max(a)] * len(a)
        for center in range(min(a), max(a)):
            fuel = min(fuel, sum(costs[abs(num - center)] for num in a))
        return fuel
