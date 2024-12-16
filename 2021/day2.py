data = open('./inputs/day2_data.txt', 'r').read()


def part1(lines):
    horizontal = 0
    vertical = 0
    for line in lines:
        splitted = line.split(' ')
        command = splitted[0]
        value = splitted[1]
        if command == 'forward':
            horizontal += int(value)
        elif command == 'up':
            vertical -= int(value)
        elif command == 'down':
            vertical += int(value)

    return horizontal * vertical


def part2(lines):
    aim = 0
    horizontal = 0
    vertical = 0
    for line in lines:
        splitted = line.split(' ')
        command = splitted[0]
        value = int(splitted[1])
        if command == 'forward':
            horizontal += value
            vertical += value * aim
        elif command == 'up':
            aim -= value
        elif command == 'down':
            aim += value

    return horizontal * vertical


print('Part 1: ' + str(part1(data.split('\n'))))
print('Part 2: ' + str(part2(data.split('\n'))))
