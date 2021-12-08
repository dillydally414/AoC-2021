from day import Day

sampleFile = open('../samples/day_08.txt', 'r')
problemFile = open('../problems/day_08.txt', 'r')


class Day08(Day):
    sample = [[[val for val in side.split()] for side in line.split('|')] for line in sampleFile.readlines()]
    problem = [[[val for val in side.split()] for side in line.split('|')] for line in problemFile.readlines()]
    part1_sample_ans = 26
    part2_sample_ans = 61229

    def part1(self, a):
        count = 0
        for line in a:
            for output in line[1]:
                count += 1 if len(output) <= 4 or len(output) == 7 else 0
        return count

    def part2(self, a):
        tot = 0
        for line in a:
            input = line[0]
            input.sort(key=lambda s: len(s))  # sort in ascending order of length
            input = [set(str) for str in input]
            signal_mapping = [
                None,
                input[0],  # index 0 will have 2 vals -> 1
                None,
                None,
                input[2],  # index 2 will have 4 vals -> 4
                None,
                None,
                input[1],  # index 1 will have 3 vals -> 7
                input[9],  # index 9 will have 7 vals -> 8
                None
            ]

            two_three_five = input[3:6]
            for i in range(0, 3):
                if len(two_three_five[i] | two_three_five[(i + 1) % 3]) == 7:
                    signal_mapping[3] = two_three_five[(i + 2) % 3]
                    two_three_five.pop((i + 2) % 3)
                    break

            four_minus_one = signal_mapping[4] - signal_mapping[1]  # bd
            if len(four_minus_one - two_three_five[0]) == 0:
                signal_mapping[2] = two_three_five[1]
                signal_mapping[5] = two_three_five[0]
            else:
                signal_mapping[2] = two_three_five[0]
                signal_mapping[5] = two_three_five[1]

            zero_six_nine = input[6:9]
            for i in range(0, 3):
                if len(signal_mapping[1] | zero_six_nine[i]) == 7:
                    signal_mapping[6] = zero_six_nine[i]
                    zero_six_nine.pop(i)
                    break

            if len(signal_mapping[4] | zero_six_nine[0]) == 7:
                signal_mapping[0] = zero_six_nine[0]
                signal_mapping[9] = zero_six_nine[1]
            else:
                signal_mapping[0] = zero_six_nine[1]
                signal_mapping[9] = zero_six_nine[0]

            output = line[1]
            output_val = 0
            for val in output:
                output_val = output_val * 10 + signal_mapping.index(set(val))
            tot += output_val
        return tot
