import re

if __name__ == "__main__":
    with open("inputs/day3.txt", "r") as f:
        data = f.read()

    pattern = r"mul\((\d+),(\d+)\)"

    running_total = 0
    for match in re.finditer(pattern, data):
        running_total += int(match[1]) * int(match[2])

    print("Part 1:", running_total)

    enabled = True
    running_total = 0

    # 12 is the length of the mul() command with max-length numbers (3 digits)
    for i in range(len(data) - 12):
        slice = data[i:i + 13]

        if re.match(r"do\(\)", slice) is not None:
            enabled = True
        if re.match(r"don't\(\)", slice) is not None:
            enabled = False

        match = re.match(pattern, slice)
        if match is not None and enabled:
            running_total += int(match[1]) * int(match[2])

    # Need to mop up the remaining slice
    match = re.search(pattern, data[-12:])
    if match is not None and enabled:
        running_total += int(match[1]) * int(match[2])

    print("Part 2:", running_total)
