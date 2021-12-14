from day import Day
from string import ascii_uppercase

sampleFile = open('../samples/day_14.txt', 'r')
problemFile = open('../problems/day_14.txt', 'r')


class Day14(Day):
    sample = [sampleFile.readline().strip(), [line.strip() for line in sampleFile.readlines()[1:]]]
    problem = [problemFile.readline().strip(), [line.strip() for line in problemFile.readlines()[1:]]]
    part1_sample_ans = 1588
    part2_sample_ans = 2188189693529

    def part1(self, a):
        rules = {}
        for mapping in a[1]:
            rule = mapping.split(' -> ')
            rules[rule[0]] = rule[1]
        curr = a[0]
        for loop in range(10):
            next = ""
            for i in range(len(curr) - 1):
                next = next + curr[i] + (rules[curr[i:i + 2]] if curr[i:i + 2] in rules else '')
            curr = next + curr[len(curr) - 1]
        max_count = 0
        min_count = len(curr)
        for letter in ascii_uppercase:
            max_count = max(max_count, curr.count(letter))
            min_count = min(min_count, curr.count(letter)) if letter in curr else min_count
        return max_count - min_count

    def part2(self, a):
        rules = {}
        for mapping in a[1]:
            rule = mapping.split(' -> ')
            rules[rule[0]] = [rule[0][0] + rule[1], rule[1] + rule[0][1]]
        curr_count = {}
        for i in range(len(a[0]) - 1):
            curr_count[a[0][i:i + 2]] = (1 + curr_count[a[0][i:i + 2]]) if a[0][i:i + 2] in curr_count else 1
        for loop in range(40):
            next_count = {}
            for pair in curr_count.keys():
                res = rules[pair]
                next_count[res[0]] = curr_count[pair] + (next_count[res[0]] if res[0] in next_count else 0)
                next_count[res[1]] = curr_count[pair] + (next_count[res[1]] if res[1] in next_count else 0)
            curr_count = next_count
        letter_counts = {}
        for pair in curr_count.keys():
            letter_counts[pair[0]] = curr_count[pair] + (letter_counts[pair[0]] if pair[0] in letter_counts else 0)
            letter_counts[pair[1]] = curr_count[pair] + (letter_counts[pair[1]] if pair[1] in letter_counts else 0)
        letter_counts[a[0][0]] += 1  # To account for all other letters being counted twice
        letter_counts[a[0][len(a[0]) - 1]] += 1
        return (max(letter_counts.values()) - min(letter_counts.values())) / 2
