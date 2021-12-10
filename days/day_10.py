from day import Day

sampleFile = open('../samples/day_10.txt', 'r')
problemFile = open('../problems/day_10.txt', 'r')

opening = {'(', '[', '{', '<'}
closing = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
points_1 = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
points_2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


class Day10(Day):
    sample = [list(line.strip()) for line in sampleFile.readlines()]
    problem = [list(line.strip()) for line in problemFile.readlines()]
    part1_sample_ans = 26397
    part2_sample_ans = 288957

    def part1(self, a):
        errors = 0
        for line in a:
            chars = []
            for char in line:
                if char in opening:
                    chars.append(char)
                else:
                    c = chars.pop(len(chars) - 1)
                    if closing[c] != char:
                        errors += points_1[char]
                        break
        return errors

    def part2(self, a):
        scores = []
        for line in a:
            chars = []
            corrupt = False
            for char in line:
                if char in opening:
                    chars.append(char)
                else:
                    c = chars.pop(len(chars) - 1)
                    if closing[c] != char:
                        corrupt = True
                        break
            if not corrupt:
                score = 0
                chars.reverse()
                for open in chars:
                    score = score * 5 + points_2[closing[open]]
                scores.append(score)
        scores.sort()
        return scores[len(scores) / 2]
