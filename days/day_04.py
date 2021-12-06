from day import Day

sampleFile = open('../samples/day_04.txt', 'r')
problemFile = open('../problems/day_04.txt', 'r')


class BingoCard(object):
    def __init__(self, card):
        self.card = card[:]
        self.marked = [[False for j in range(len(card[i]))] for i in range(len(card))]

    def mark(self, num):
        for i in range(len(self.card)):
            for j in range(len(self.card[i])):
                if num == self.card[i][j]:
                    self.marked[i][j] = True
                    return

    def won(self):
        for x in range(len(self.marked)):
            true_x = True
            true_y = True
            for y in range(len(self.marked[x])):
                true_x = true_x and self.marked[x][y]
                true_y = true_y and self.marked[y][x]
            if true_x or true_y:
                return True
        return False

    def sum(self):
        return sum([
            sum([
                (lambda c: 0 if self.marked[row][c] else self.card[row][c])(col)
                for col in range(len(self.card[row]))
            ]) for row in range(len(self.card))
        ])


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
        for num in self.num_order:
            for card in self.bingo_cards:
                card.mark(num)
                if card.won():
                    return card.sum() * num
        return None

    def losing_board_value(self):
        not_won_yet = self.bingo_cards[:]
        for num in self.num_order:
            not_won_yet_updated = not_won_yet[:]
            for card in not_won_yet_updated:
                card.mark(num)
                if card.won():
                    if not_won_yet.__len__() == 1:
                        return card.sum() * num
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
