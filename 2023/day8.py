def part1(graph, directions):
    current = "AAA"
    count = 0
    while current != "ZZZ":
        next_move = directions.pop(0)

        if next_move == 'L':
            current = graph[current][0]
        else:
            current = graph[current][1]

        directions.append(next_move)
        count += 1

    print("Part 1:", count)


def part2(graph, directions):
    current = []
    len_directions = len(directions)  # For fewer queries

    for key in graph.keys():
        if key[2] == 'A':
            current.append(key)

    range_cache = range(len(current))

    def verify():
        for entry in current:
            if entry[2] != 'Z':
                return False
        return True

    count = 0
    while not verify():
        next_move = directions[count % len_directions]
        for i in range_cache:
            if next_move == 'L':
                current[i] = graph[current[i]][0]
            else:
                current[i] = graph[current[i]][1]

        count += 1

    print(count)


if __name__ == "__main__":
    with open("inputs/day8.txt", "r") as f:
        lines = f.readlines()

    dirs = list(lines[0].strip())
    graph = dict()

    for line in lines[2:]:
        start = line[0:3]
        left = line[7:10]
        right = line[12:15]

        graph[start] = (left, right)

    part1(graph, dirs.copy())
    part2(graph, dirs.copy())
