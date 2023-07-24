elf_sums = list(map(lambda elf_cals: sum(elf_cals), map(lambda elf: map(lambda item: int(item), elf.split("\n")), open("day1.txt", "r").read().split("\n\n"))))
elf_sums.sort()

print("1a) Maximum calories carried by single elf: " + str(elf_sums[-1]))
print("1b) Total calories carried by top three elves: " + str(sum(elf_sums[-3:])))