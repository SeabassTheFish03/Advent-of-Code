f = open("6", "r")
raw_data = f.read()
f.close()

# Views a slice of the string. If the length of the raw input is the same as the set, then
# that means there were no duplicates, as the duplicates would be filtered out during the
# set conversion.
def pass_test(i,length):
	splice = raw_data[i:i+length]
	return len(splice)==len(set(splice))

# Part a, slice is 4 characters long
j = 0
while not pass_test(j,4):
	j += 1
print(j + 4)

# Part b, slice is 14 characters long
k = 0
while not pass_test(k,14):
	k += 1
print(k + 14)