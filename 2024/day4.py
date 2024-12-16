if __name__ == "__main__":
    with open("inputs/day4_example.txt", "r") as f:
        data = f.read()

    focus = 0
    word = "XMAS"

    line_len = data.find("\n") + 1

    def down(dex):
        try:
            return "".join([data[dex + x * line_len] for x in range(4)])
        except IndexError:
            return "...."

    def right(dex):
        try:
            return "".join(data[dex:dex + 4])
        except IndexError:
            return "...."

    def bltr(dex):
        try:
            return "".join([data[dex + x - x * line_len] for x in range(4)])
        except IndexError:
            return "...."

    def tlbr(dex):
        try:
            return "".join([data[dex + x + x * line_len] for x in range(4)])
        except IndexError:
            return "...."

    count = 0
    for i in range(len(data)):
        if data[i] != "X" and data[i] != "S":
            continue

        d = down(i)
        r = right(i)
        slash = bltr(i)
        backslash = tlbr(i)

        if d == "XMAS" or d == "SAMX":
            # print("Down", d, i)
            count += 1

        if r == "XMAS" or r == "SAMX":
            # print("Right", r, i)
            count += 1

        if slash == "XMAS" or slash == "SAMX":
            # print("Slash", slash, i)
            count += 1

        if backslash == "XMAS" or backslash == "SAMX":
            print([i + x + x * line_len for x in range(4)])
            # print("Backslash", backslash, i)
            count += 1

    print("Part 1:", count)
