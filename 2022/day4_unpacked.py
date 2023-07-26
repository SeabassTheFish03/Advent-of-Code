f = open("4", "r")
input_ranges = f.readlines()
f.close()

# Map each line from "x-y,w-z" to ((x, y), (w, z))
divided_ranges_as_strings = []
for ranges in input_ranges:
	divided_ranges_as_strings.append(ranges.strip().split(","))

comprehended_ranges = [] # List[((int, int), (int, int))]
for range_strs in divided_ranges_as_strings:
	for i, string in enumerate(range_strs):
		range_strs[i] = string.split("-")
	comprehended_ranges.append(((int(range_strs[0][0]), int(range_strs[0][1])), (int(range_strs[1][0]), int(range_strs[1][1]))))

# Checks if it's fully contained. If left isn't less than right it flips and tries again
def fully_contains(rng):
	left, right = rng[0], rng[1]
	if left[0] <= right[0]:
		return left[1] >= right[1] or left[0] == right[0]
	return fully_contains((right, left))

# Queries overlap, and if left isn't less than right it flips them and tries again
def overlap(rng):
	left, right = rng[0], rng[1]
	if left[0] <= right[0]:
		return left[1] >= right[0]
	return overlap((right, left))

print("4a) Ranges where one fully contains the other: " + str(sum(fully_contains(obj) for obj in comprehended_ranges)))
print("4b) Ranges where there is overlap: " + str(sum(overlap(obj) for obj in comprehended_ranges)))