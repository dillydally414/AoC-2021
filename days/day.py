import unittest
from abc import abstractmethod, abstractproperty


class Day(unittest.TestCase):
    @abstractproperty
    def sample(self):
        pass

    @abstractproperty
    def problem(self):
        pass

    @abstractproperty
    def part1_sample_ans(self):
        pass

    @abstractproperty
    def part2_sample_ans(self):
        pass

    @abstractmethod
    def part1(self, a):
        pass

    @abstractmethod
    def part2(self, a):
        pass

    def test_part1_sample(self):
        self.assertEqual(self.part1(self.sample), self.part1_sample_ans)

    def test_part1_problem(self):
        print("Part 1: " + str(self.part1(self.problem)))

    def test_part2_sample(self):
        self.assertEqual(self.part2(self.sample), self.part2_sample_ans)

    def test_part2_problem(self):
        print("Part 2: " + str(self.part2(self.problem)))
