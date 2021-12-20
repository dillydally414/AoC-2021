from day import Day

sampleFile = open('../samples/day_20.txt', 'r')
problemFile = open('../problems/day_20.txt', 'r')


def parse(file_lines):
    algorithm = [char == '#' for char in file_lines[0].strip()]
    image = [[char == '#' for char in line.strip()] for line in file_lines[2:]]
    return [algorithm, image]


def neighbor_val(a, unknown_pixel_val, row, col):
    neighbors = ""
    for i in range(row - 1, row + 2):
        if i < 0 or i >= len(a):
            neighbors += "111" if unknown_pixel_val else "000"
            continue
        for j in range(col - 1, col + 2):
            if j < 0 or j >= len(a[i]):
                neighbors += "1" if unknown_pixel_val else "0"
            else:
                neighbors += "1" if a[i][j] else "0"
    return int(neighbors, 2)


def enhance(algorithm, image, unknown_pixel_val):
    image = [[unknown_pixel_val] + line[:] + [unknown_pixel_val] for line in image]
    image = [[unknown_pixel_val] * len(image[0])] + image + [[unknown_pixel_val] * len(image[0])]
    image_copy = [line[:] for line in image]
    for i in range(len(image)):
        for j in range(len(image[i])):
            image_copy[i][j] = algorithm[neighbor_val(image, unknown_pixel_val, i, j)]
    return image_copy


class Day20(Day):
    sample = parse(sampleFile.readlines())
    problem = parse(problemFile.readlines())
    part1_sample_ans = 35
    part2_sample_ans = 3351

    def part1(self, a):
        alg = a[0]
        img = a[1]
        img = enhance(alg, img, False)
        img = enhance(alg, img, alg[0])
        return sum([line.count(True) for line in img])

    def part2(self, a):
        alg = a[0]
        img = a[1]
        for i in range(50):
            img = enhance(alg, img, False if i % 2 == 0 else alg[0])
        return sum([line.count(True) for line in img])
