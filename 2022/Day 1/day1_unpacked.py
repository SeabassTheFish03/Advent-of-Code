f = open("1", "r")
input_text = f.read()
f.close()

# Split each chunk of text into its own item
elves = input_text.split("\n\n")

# Split each individual elf into its food items
elves_split_by_food = []
for elf in elves:
	elves_split_by_food.append(elf.split("\n"))

# Summing all the food items by elf
elf_sums = []
for elf_food_list in elves_split_by_food:
	intified = [int(item) for item in elf_food_list]
	elf_sums.append(sum(intified))

elf_sums.sort() # Useful for part b

# We know the maximum will be the last element in the list since we sorted it
print("1a) Maximum calories carried by a single elf: " + str(elf_sums[-1]))

# Here is why we sorted earlier. We can grab the last 3 with the assurance they are
# the top 3 calorie holders
print("1b) Total calories carried by top three elves: " + str(sum(elf_sums[-3:])))