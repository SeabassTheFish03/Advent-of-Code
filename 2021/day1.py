data = open('./inputs/day1_data.txt', 'r').read()


def part1(lines):
    increases = 0
    for i in range(len(lines)):
        if i > 0:
            if int(lines[i]) > int(lines[i - 1]):
                increases += 1

    return increases


print("Part 1: " + str(part1(data.split('\n'))))


def part2(lines):
    increases = 0
    sums = []
    for i in range(len(lines)):
        if i > 1:
            sums.append(int(lines[i - 2]) + int(lines[i - 1]) + int(lines[i]))
    return part1(sums)


print("Part 2: " + str(part2(data.split('\n'))))
