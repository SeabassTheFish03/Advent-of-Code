f = open("3", "r")
rucks = f.read().split("\n")
f.close()

# Finds the common character between a collection of strings
def string_and(strings):
		sets = list(map(lambda string: set(string), strings))
		return sets[0].intersection(*sets[1:]).pop()

# Gives the priority for characters as defined by the problem statement
def prioritize(character):
	if (value := ord(character)) > 64 and value < 97:
		return value - 38
	return ord(character) - 96

split_rucks = []
for ruck in rucks:
	split_rucks.append((ruck[:int(len(ruck)/2)],ruck[int(len(ruck)/2):])) # Splits the string into two equal pieces

common_within_rucks = []
for split_ruck in split_rucks:
	common_within_rucks.append(string_and(split_ruck)) # Finds the common item and adds it to the list

prioritized = []
for common_item in common_within_rucks:
	prioritized.append(prioritize(common_item)) # Give it a priority and add it to a list of priorities

grouped_by_3 = [(rucks[i], rucks[i+1], rucks[i+2]) for i in range(0, len(rucks), 3)] # Tuples of three rucks

# From here, very similar process
common_within_group = []
for group in grouped_by_3:
	common_within_group.append(string_and(group))

prioritized_groups = []
for common_thing in common_within_group:
	prioritized_groups.append(prioritize(common_thing))

print("3a) Total Priority for split rucks: " + str(sum(prioritized)))
print("3b) Total Priority for groups of 3: " + str(sum(prioritized_groups)))