elf_sums = list(map(lambda elf_cals: sum(elf_cals), map(lambda elf: map(lambda item: int(item), elf.split("\n")), open("1").read().split("\n\n"))))
elf_sums.sort()
print(elf_sums[-1],sum(elf_sums[-3:]))