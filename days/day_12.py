from day import Day

sampleFile = open('../samples/day_12.txt', 'r')
problemFile = open('../problems/day_12.txt', 'r')


def paths_between(graph, s, t, visited):
    if s == t:
        return [[]]
    paths_from_out_neighbors = []
    for out_neighbor in graph[s]:
        if out_neighbor.lower() == out_neighbor and out_neighbor in visited:
            continue
        new_visited = {out_neighbor}
        new_visited.update(visited)
        out_neighbor_paths = paths_between(graph, out_neighbor, t, new_visited)
        for path in out_neighbor_paths:
            path.insert(0, out_neighbor)
            paths_from_out_neighbors.append(path)
    return paths_from_out_neighbors


def paths_between_v2(graph, s, t, visited):
    if s == t:
        return [[]]
    paths_from_out_neighbors = []
    for out_neighbor in graph[s]:
        if (out_neighbor.lower() == out_neighbor and out_neighbor in visited and 2 in visited.values()) or out_neighbor == 'start':
            continue
        new_visited = {}
        new_visited.update(visited)
        if out_neighbor.lower() == out_neighbor:
            new_visited[out_neighbor] = visited[out_neighbor] + 1 if out_neighbor in visited else 1
        out_neighbor_paths = paths_between_v2(graph, out_neighbor, t, new_visited)
        for path in out_neighbor_paths:
            path.insert(0, out_neighbor)
            paths_from_out_neighbors.append(path)
    return paths_from_out_neighbors


class Day12(Day):
    sample = [line.strip().split('-') for line in sampleFile.readlines()]
    problem = [line.strip().split('-') for line in problemFile.readlines()]
    part1_sample_ans = 226
    part2_sample_ans = 3509

    def part1(self, a):
        caves = {}
        for path in a:
            if path[0] not in caves:
                caves[path[0]] = []
            if path[1] not in caves:
                caves[path[1]] = []
            caves[path[0]].append(path[1])
            caves[path[1]].append(path[0])
        return len(paths_between(caves, 'start', 'end', {'start'}))

    def part2(self, a):
        caves = {}
        for path in a:
            if path[0] not in caves:
                caves[path[0]] = []
            if path[1] not in caves:
                caves[path[1]] = []
            caves[path[0]].append(path[1])
            caves[path[1]].append(path[0])
        return len(paths_between_v2(caves, 'start', 'end', {'start': 1}))
