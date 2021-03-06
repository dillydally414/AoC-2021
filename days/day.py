import unittest
from abc import abstractmethod, abstractproperty


class Day(unittest.TestCase):
    @property
    @abstractmethod
    def sample(self):
        pass

    @property
    @abstractmethod
    def problem(self):
        pass

    @property
    @abstractmethod
    def part1_sample_ans(self):
        pass

    @property
    @abstractmethod
    def part2_sample_ans(self):
        pass

    @abstractmethod
    def part1(self, a):
        pass

    @abstractmethod
    def part2(self, a):
        pass

    def test_part1_sample(self):
        if self.part2_sample_ans is None:
            self.assertEqual(self.part1_sample_ans, self.part1(self.sample))

    def test_part1_problem(self):
        if self.part2_sample_ans is None:
            print("Part 1: " + str(self.part1(self.problem)))

    def test_part2_sample(self):
        if self.part2_sample_ans is None:
            return
        self.assertEqual(self.part2_sample_ans, self.part2(self.sample))

    def test_part2_problem(self):
        if self.part2_sample_ans is None:
            return
        print("Part 2: " + str(self.part2(self.problem)))
