def string_and(strings):
		sets = list(map(lambda string: set(string), strings))
		return sets[0].intersection(*sets[1:]).pop()
def prioritize(character):
	if (value := ord(character)) > 64 and value < 97:
		return value - 38
	return ord(character) - 96

rucks = open("day3.txt").read().split("\n")

print("3a) Total Priority for split rucks: " + str(sum(map(lambda ruck: prioritize(string_and((ruck[:int(len(ruck)/2)], ruck[int(len(ruck)/2):]))), rucks))))
print("3b) Total Priority for groups of 3: " + str(sum(map(lambda group: prioritize(string_and(group)), [(rucks[i], rucks[i+1], rucks[i+2]) for i in range(0, len(rucks), 3)]))))