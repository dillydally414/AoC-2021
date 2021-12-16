from functools import reduce
from day import Day

sampleFile = open('../samples/day_16.txt', 'r')
problemFile = open('../problems/day_16.txt', 'r')


hexa_to_bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}


def packet_versions(a, index):
    version = int(a[index:index + 3], 2)
    index += 3
    type = int(a[index:index + 3], 2)
    index += 3
    if type == 4:
        while a[index] != '0':
            index += 5
        index += 5
    else:
        length_type = int(a[index], 2)
        index += 1
        if length_type == 0:
            length = int(a[index:index + 15], 2)
            index += 15
            end_length = length + index
            while index < end_length:
                subpacket_version, index = packet_versions(a, index)
                version += subpacket_version
        else:
            num_subpackets = int(a[index:index + 11], 2)
            index += 11
            for i in range(num_subpackets):
                subpacket_version, index = packet_versions(a, index)
                version += subpacket_version
    return version, index


def packet_value(a, index):
    index += 3
    type = int(a[index:index + 3], 2)
    index += 3
    if type == 4:
        bits = ""
        while a[index] != '0':
            bits += a[index + 1:index + 5]
            index += 5
        bits += a[index + 1:index + 5]
        index += 5
        return int(bits, 2), index
    else:
        length_type = int(a[index], 2)
        index += 1
        subpacket_values = []
        if length_type == 0:
            length = int(a[index:index + 15], 2)
            index += 15
            end_length = length + index
            while index < end_length:
                subpacket_value, index = packet_value(a, index)
                subpacket_values.append(subpacket_value)
        else:
            num_subpackets = int(a[index:index + 11], 2)
            index += 11
            for i in range(num_subpackets):
                subpacket_value, index = packet_value(a, index)
                subpacket_values.append(subpacket_value)
        if type == 0: return sum(subpacket_values), index
        if type == 1: return reduce(lambda a, b: a * b, subpacket_values), index
        if type == 2: return min(subpacket_values), index
        if type == 3: return max(subpacket_values), index
        if type == 5: return (1 if subpacket_values[0] > subpacket_values[1] else 0), index
        if type == 6: return (1 if subpacket_values[0] < subpacket_values[1] else 0), index
        return (1 if subpacket_values[0] == subpacket_values[1] else 0), index


class Day16(Day):
    sample = reduce(lambda a, b: a + b, [hexa_to_bin[char] for char in sampleFile.readline().strip()])
    problem = reduce(lambda a, b: a + b, [hexa_to_bin[char] for char in problemFile.readline().strip()])
    part1_sample_ans = 20
    part2_sample_ans = 1

    def part1(self, a):
        return packet_versions(a, 0)[0]

    def part2(self, a):
        return packet_value(a, 0)[0]
