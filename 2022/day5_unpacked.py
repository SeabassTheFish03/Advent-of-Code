import re
import copy

f = open("5", "r")
raw = f.read()
f.close()

starting, movements = raw.split("\n\n")

removed_last_line = starting.split("\n")[:-1]
# We're only interested in columns 2, 6, 10, etc.
abridged = []
for line in removed_last_line:
	abridged += "".join([item[1] for item in filter(lambda enum: enum[0]%4==1, enumerate(line))])

transposed = []
for i in range(9):
	transposed.append(list(reversed([item[1] for item in filter(lambda x,i=i: x[0]%9==i and x[1] != " ", enumerate(abridged))])))

regex = r"(\d+)(?:\D{6})(\d)(?:\D{4})(\d)" # Captures the digits within each command

stacks_1 = copy.deepcopy(transposed)
stacks_2 = copy.deepcopy(transposed)
orders = movements.split("\n")
for line in orders:
	matches = re.search(regex, line)
	chunk_1 = [stacks_1[int(matches[2])-1].pop() for _ in range(int(matches[1]))]
	chunk_2 = list(reversed([stacks_2[int(matches[2])-1].pop() for _ in range(int(matches[1]))]))
	stacks_1[int(matches[3])-1] += chunk_1
	stacks_2[int(matches[3])-1] += chunk_2
print("".join([stack[-1] for stack in stacks_1]))
print("".join([stack[-1] for stack in stacks_2]))

