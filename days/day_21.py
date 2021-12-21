from day import Day

sampleFile = open('../samples/day_21.txt', 'r')
problemFile = open('../problems/day_21.txt', 'r')


def parse(file_lines):
    p1 = file_lines[0].strip()
    p1 = int(p1[len(p1) - 1])
    p2 = file_lines[1].strip()
    p2 = int(p2[len(p2) - 1])
    return [p1, p2]


class Day21(Day):
    sample = parse(sampleFile.readlines())
    problem = parse(problemFile.readlines())
    part1_sample_ans = 739785
    part2_sample_ans = 444356092776315

    def part1(self, a):
        die = 1
        rolls = 0
        scores = [0, 0]
        player = -1
        while max(scores) < 1000:
            player = (player + 1) % 2
            moves = sum([((die + i - 1) % 10) + 1 for i in range(3)])
            a[player] = ((a[player] + moves - 1) % 10) + 1
            die = ((die + 2) % 10) + 1
            scores[player] += a[player]
            rolls += 3
        return min(scores) * rolls

    def part2(self, a):
        roll_chances = {  # 27 universes per turn
            3: 1,
            4: 3,
            5: 6,
            6: 7,
            7: 6,
            8: 3,
            9: 1,
        }
        games = {(tuple(a), (0, 0)): 1}  # (locations, score) -> count (how many games have this setup)
        wins = [0, 0]
        player = -1
        while len(games) > 0:
            player = (player + 1) % 2
            new_games = {}
            for game in games:
                for chance in roll_chances:
                    location = game[0][:]
                    score = game[1][:]
                    count = games[game]
                    new_location = ((location[player] + chance - 1) % 10) + 1
                    location = (location[0], new_location) if player == 1 else (new_location, location[1])
                    score = (score[0], score[1] + new_location) if player == 1 else (score[0] + new_location, score[1])
                    count *= roll_chances[chance]
                    if score[player] >= 21:
                        wins[player] += count
                    else:
                        new_games[(location, score)] = \
                            count + (new_games[(location, score)] if (location, score) in new_games else 0)
            games = new_games
        return max(wins)
