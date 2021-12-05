from day import Day

sampleFile = open('../samples/day_04.txt', 'r')
problemFile = open('../problems/day_04.txt', 'r')


class BingoCard(object):
    def __init__(self, card):
        self.card = card[:]

    def won(self, nums):
        if len(nums) < 5:
            return False
        for x in range(len(self.card)):
            true_x = True
            true_y = True
            for y in range(len(self.card)):
                true_x = true_x and self.card[x][y] in nums
                true_y = true_y and self.card[y][x] in nums
            if true_x or true_y:
                return True
        return False

    def sum(self, marked_numbers):
        return sum([sum([(lambda i: 0 if i in marked_numbers else i)(num) for num in row]) for row in self.card])


class Bingo(object):
    def __init__(self, file):
        file_contents = file.readlines()
        self.num_order = [int(str) for str in file_contents[0].strip().split(',')]
        bingo_cards = []
        for i in range(2, len(file_contents)):
            if i % 6 == 1:
                continue
            if i % 6 == 2:
                bingo_cards.append([])
            card = (i - 2) // 6
            bingo_cards[card].append([int(str) for str in file_contents[i].strip().split()])
        self.bingo_cards = []
        for i in range(len(bingo_cards)):
            self.bingo_cards.append(BingoCard(bingo_cards[i]))

    def winning_board_value(self):
        for i in range(len(self.num_order)):
            for card in self.bingo_cards:
                if card.won(self.num_order[0:i + 1]):
                    return card.sum(self.num_order[0:i + 1]) * self.num_order[i]
        return None

    def losing_board_value(self):
        not_won_yet = self.bingo_cards[:]
        for i in range(len(self.num_order)):
            for card in not_won_yet:
                if card.won(self.num_order[0:i + 1]):
                    if not_won_yet.__len__() == 1:
                        return card.sum(self.num_order[0:i + 1]) * self.num_order[i]
                    else:
                        not_won_yet.remove(card)
        return None


class Day04(Day):
    sample = Bingo(sampleFile)
    problem = Bingo(problemFile)
    part1_sample_ans = 4512
    part2_sample_ans = 1924

    def part1(self, a):
        return a.winning_board_value()

    def part2(self, a):
        return a.losing_board_value()
