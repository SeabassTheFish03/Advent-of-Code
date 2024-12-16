from collections import Counter


with open('./inputs/day5_data.txt', 'r') as f:
    data = f.readlines()


def part1(raw_input: list[str]) -> int:
    # Assume the maximums at 1000
    x_max = 1000
    y_max = 1000

    field = [0] * (x_max * y_max)

    for line in raw_input:
        start_finish = line.split(" -> ")
        ranges = list(map(lambda x: list(map(lambda y: int(y), x.split(','))), start_finish))
        x1 = ranges[0][0]
        y1 = ranges[0][1]
        x2 = ranges[1][0]
        y2 = ranges[1][1]

        if y1 == y2:  # Horizontal
            for i in range(min(x1, x2), max(x1, x2) + 1):
                field[y1 * x_max + i] += 1
        elif x1 == x2:  # Vertical
            for j in range(min(y1, y2), max(y1, y2) + 1):
                field[j * x_max + x1] += 1

    counts = Counter(field)
    return sum([value for key, value in counts.items() if key > 0])


if __name__ == "__main__":
    print("Part 1:", part1(data))
