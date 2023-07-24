# Getting the data
f = open('day4_data.txt', 'r')
data = f.read()
f.close()

# Comprehending the data
lines = data.split('\n\n')

# The first data value is the list of numbers that are read off
numbers = [int(num) for num in lines[0].split(',')]

# All subsequent data is possible boards (prune the last one because it's an empty list)
bds = lines[1:-1]

def filter_for_spaces(row):
    if '' in row:
        return [x for i,x in enumerate(row) if row[i]!='']
    return row

def check_row(row):
    for value in row:
        if not value[1]:
            return False
    return True

def check_col(board, col):
    for row in board:
        if not row[col][1]:
            return False
    return True

def check_win(board):
    for i in range(len(board[0])):
        if not check_col(board, i):
            return False
    for row in board:
        if not check_row(row):
            return False
    return True

def score(board, called):
    sum = 0
    for row in board:
        for value in row:
            if not value[1]:
                sum += value[0]

    return sum*called

# Doing a little string comprehension to change the board into a two-dimensional array
for i in range(len(bds)):
    # Now, every board is a list of board rows
    bds[i] = bds[i].split('\n')
    for j in range(len(bds[i])):
        # Every board row here is being replaced with another list with each number as an element
        bds[i][j] = filter_for_spaces(bds[i][j].split(' '))
        for k in range(len(bds[i][j])):
            # Giving every number a corresponding "selected" value in another list!
            bds[i][j][k] = [int(bds[i][j][k]), False]

# This is where the fun begins
def part1(numbers, boards) -> str:
    itrs = 0
    tracking = []
    for number in numbers:
        for board in boards:
            for row in board:
                for value in row:
                    if not value[1]:
                        value[1] = (value[0] == number)

        if itrs > 4:
            for board in boards:
                for i in range(len(boards[0])):
                    if check_col(board, i):
                        if board not in [x[0] for x in tracking]:
                            tracking.append([board, score(board, number)])

                for row in board:
                    if check_row(row):
                        if board not in [x[0] for x in tracking]:
                            tracking.append([board, score(board, number)])
        itrs += 1
    return str(tracking[0][1])

def part2(numbers, boards) -> str:
    # WET Code, don't judge
    tracking = []
    for number in numbers:
        for board in [x for x in boards if x not in [y[0] for y in tracking]]:
            for row in board:
                for value in row:
                    if not value[1]:
                        value[1] = (value[0] == number)
            if check_win(board):
                tracking.append([board, score(board, number)])
    print(tracking[-1])
    return str(tracking[-1][1])

#print('Part 1: ' + part1(numbers, list(bds)))
print('Part 2: ' + part2(numbers, list(bds)))
