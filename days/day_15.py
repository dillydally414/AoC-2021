from day import Day
from day_05 import Point
from heapq import *

sampleFile = open('../samples/day_15.txt', 'r')
problemFile = open('../problems/day_15.txt', 'r')


def get_neighbors(size, point):
    [row, col] = [point.x, point.y]
    neighbors = set()
    for i in range(max(0, row - 1), min(row + 2, size.x)):
        neighbors.add(Point(i, col))
    for j in range(max(0, col - 1), min(col + 2, size.y)):
        neighbors.add(Point(row, j))
    neighbors.remove(point)
    return neighbors


def dijkstras(graph, weights, start, end):
    dist = {start: 0}
    queue = [(0, [start.x, start.y])]
    while len(queue) > 0:
        u = heappop(queue)[1]
        u = Point(u[0], u[1])
        if u == end:
            return dist[end]
        for neighbor in graph[u]:
            new_dist = weights[neighbor] + dist[u]
            if neighbor not in dist or new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heappush(queue, (dist[neighbor], [neighbor.x, neighbor.y]))
    return dist[end]


class Day15(Day):
    sample = [[int(c) for c in line.strip()] for line in sampleFile.readlines()]
    problem = [[int(c) for c in line.strip()] for line in problemFile.readlines()]
    part1_sample_ans = 40
    part2_sample_ans = 315

    def part1(self, a):
        graph = {}
        weights = {}
        a_size = Point(len(a), len(a[0]))
        for row in range(len(a)):
            for col in range(len(a[row])):
                graph[Point(row, col)] = get_neighbors(a_size, Point(row, col))
                weights[Point(row, col)] = a[row][col]
        start = Point(0, 0)
        end = Point(a_size.x - 1, a_size.y - 1)
        return dijkstras(graph, weights, start, end)

    def part2(self, a):
        graph = {}
        weights = {}
        a_new_size = Point(len(a) * 5, len(a[0]) * 5)
        for row in range(len(a) * 5):
            for col in range(len(a[row % len(a)]) * 5):
                graph[Point(row, col)] = get_neighbors(a_new_size, Point(row, col))
                weights[Point(row, col)] = (((a[row % len(a)][col % len(a[row % len(a)])]
                                            + (row // len(a) + col // len(a[row % len(a)]))) - 1) % 9) + 1
        start = Point(0, 0)
        end = Point(a_new_size.x - 1, a_new_size.y - 1)
        return dijkstras(graph, weights, start, end)
