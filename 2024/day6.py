def next_board(current_board, line_len, counter):
    while True:
        for x in ["<", ">", "^", "V"]:
            if x in current_board:
                orientation = x
                guard = current_board.find(x)

        if orientation == "<":
            if guard % line_len == 0:
                raise StopIteration()

            next_stop = guard - 1
            if current_board[next_stop] == "#":
                orientation = "^"
                next_stop = guard
        elif orientation == ">":
            if guard % line_len == line_len - 1:
                raise StopIteration()

            next_stop = guard + 1
            if current_board[next_stop] == "#":
                orientation = "V"
                next_stop = guard
        elif orientation == "V":
            if guard + line_len > len(current_board):
                raise StopIteration()

            next_stop = guard + line_len
            if current_board[next_stop] == "#":
                orientation = "<"
                next_stop = guard
        elif orientation == "^":
            if guard - line_len < 0:
                raise StopIteration()

            next_stop = guard - line_len
            if current_board[next_stop] == "#":
                orientation = ">"
                next_stop = guard

        # Make the new board
        new_board = list(current_board)
        new_count = counter
        new_board[guard] = "X"

        if new_board[next_stop] == ".":
            new_count += 1
        new_board[next_stop] = orientation
        yield "".join(new_board), new_count


if __name__ == "__main__":
    with open("inputs/day6.txt", "r") as f:
        board = f.read()

    line_len = board.find("\n") + 1

    current_board = board
    count = 0
    b, c = next(next_board(current_board, line_len, count))

    while True:
        current_board = b
        count = c
        try:
            b, c = next(next_board(current_board, line_len, count))
        except RuntimeError:
            break

    print("Part 1:", count + 1)
