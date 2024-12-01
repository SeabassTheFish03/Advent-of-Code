from collections import Counter


if __name__ == "__main__":
    with open("inputs/day1.txt", "r") as f:
        lines = f.readlines()

    left = []
    right = []

    for line in lines:
        splitted = line.strip().split("   ")
        left.append(int(splitted[0]))
        right.append(int(splitted[1]))

    left.sort()
    right.sort()

    running_total = 0
    for i in range(len(left)):
        running_total += abs(left[i] - right[i])

    print("Part 1:", running_total)

    right_totals = Counter(right)
    similarity = sum([x * right_totals[x] for x in left])

    print("Part 2:", similarity)
