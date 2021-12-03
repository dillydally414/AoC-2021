from day import Day

sampleFile = open('../samples/day_03.txt', 'r')
problemFile = open('../problems/day_03.txt', 'r')


def count_ones(a, index):
    one_count = 0
    for s in a:
        one_count += 1 if s[index] == '1' else -1
    return one_count


class Day03(Day):
    sample = [str.strip() for str in sampleFile.readlines()]
    problem = [str.strip() for str in problemFile.readlines()]
    part1_sample_ans = 198
    part2_sample_ans = 230

    def part1(self, a):
        eps = ""
        gamma = ""
        for x in range(len(a[0])):
            bit = '1' if count_ones(a, x) >= 0 else '0'
            eps += bit
            gamma += '1' if bit == '0' else '0'
        return int(eps, 2) * int(gamma, 2)

    def part2(self, a):
        oxy = a[:]
        oxy_rating = -1
        for x in range(len(a[0])):
            oxy_bit = '1' if count_ones(oxy, x) >= 0 else '0'
            oxy = filter(lambda s: s[x] == oxy_bit, oxy)
            if oxy.__len__() == 1:
                oxy_rating = int(oxy[0], 2)
                break

        co2 = a[:]
        co2_rating = -1
        for x in range(len(a[0])):
            co2_bit = '0' if count_ones(co2, x) >= 0 else '1'
            co2 = filter(lambda s: s[x] == co2_bit, co2)
            if co2.__len__() == 1:
                co2_rating = int(co2[0], 2)
                break

        return oxy_rating * co2_rating
