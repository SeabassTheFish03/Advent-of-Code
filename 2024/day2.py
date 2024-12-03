if __name__ == "__main__":
    with open("inputs/day2.txt", "r") as f:
        reports = f.readlines()

    def unsafe_increasing(left, right):
        return left - right < -3 or left - right >= 0

    def unsafe_decreasing(left, right):
        return left - right > 3 or left - right <= 0

    def check_levels(levels):
        if levels[0] < levels[1]:
            for i in range(len(levels) - 1):
                if unsafe_increasing(levels[i], levels[i + 1]):
                    return i
        elif levels[0] > levels[1]:
            for i in range(len(levels) - 1):
                if unsafe_decreasing(levels[i], levels[i + 1]):
                    return i
        else:
            return 0

        return -1

    # Part 1
    safe = 0
    for line in reports:
        levels = [int(x) for x in line.split(" ")]
        if check_levels(levels) == -1:
            safe += 1

    print("Part 1:", safe)

    # Part 2
    safe = 0
    remedial = []
    for line in reports:
        levels = [int(x) for x in line.split(" ")]

        if (offender := check_levels(levels)) == -1:
            safe += 1
        else:
            new_left = levels.copy()
            new_right = levels.copy()
            new_left.pop(offender)
            new_right.pop(offender + 1)
            levels.pop(0)
            remedial.append((new_left, new_right, levels))

    for (levels_l, levels_r, levels_s) in remedial:
        if check_levels(levels_l) == -1 or check_levels(levels_r) == -1 or check_levels(levels_s) == -1:
            safe += 1

    print("Part 2:", safe)
