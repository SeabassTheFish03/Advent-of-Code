from functools import reduce

if __name__ == "__main__":
    with open("inputs/day25.txt", "r") as f:
        possibilities = f.read().split("\n\n")

    line_len = possibilities[0].find("\n")

    locks = []
    keys = []

    for item in possibilities:
        converted = [-1, -1, -1, -1, -1]

        for i in range(len(item)):
            if item[i] == "#":
                converted[i % (line_len + 1)] += 1

        if item[0] == "#":
            locks.append(converted)
        else:
            keys.append(converted)

    # First key is position in list
    # Second key is the number in position
    positions = {x: {y: [] for y in range(6)} for x in range(5)}

    for i, lock in enumerate(locks):
        for x in range(line_len):
            positions[x][lock[x]].append(i)

    count = 0
    for key in keys:
        possible_locks = set(range(len(locks)))
        for i, pin in enumerate(key):
            possible_locks.intersection_update(
                set(reduce(
                    lambda a, b: a.union(b),
                    [set(positions[i][x]) for x in range(6 - pin)]
                ))
            )
        count += len(possible_locks)

    print("Part 1:", count)
