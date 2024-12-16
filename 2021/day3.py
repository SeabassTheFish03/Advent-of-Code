from bitstring import BitArray

data = open('./inputs/day3_data.txt', 'r').read()

lines = data.split('\n')


def more(data, i):
    ones = 0
    zeroes = 0
    for line in data:
        line = BitArray(bin=line)
        if int(line.bin[i]) == 1:
            ones += 1
        else:
            zeroes += 1

    if ones >= zeroes:
        return 1
    else:
        return 0


def scrub(arry, value):
    outArray = []
    for element in arry:
        if element != value:
            outArray.append(element)

    return outArray


def part1(data):
    gamma = BitArray(bin='000000000000')

    for i in range(12):
        gamma[i] = more(data, i)

    gamma1 = gamma.uint
    print(gamma1)
    gamma.invert()
    epsilon = gamma.uint

    return int(gamma1) * int(epsilon)

# This function does not work


def part2(data):
    oxyDat = data.copy()
    co2Dat = data.copy()

    for i in range(len(data[0])):
        m = more(data, i)
        for line in data:
            if int(line[i]) == m:
                if len(co2Dat) > 1:
                    co2Dat = scrub(co2Dat, line)
            else:
                if len(oxyDat) > 1:
                    oxyDat = scrub(oxyDat, line)

    oxy = int(oxyDat[0], 2)
    co2 = int(co2Dat[0], 2)
    return oxy * co2


print('Part 1: ' + str(part1(lines)))
print('Part 2: ' + str(part2(lines)))
# print(''.join(gamma))
# print(int(''.join(gamma), 2))
