connection = ['A', 'B', 'C', 'X', 'Y', 'Z']
scores = [0, 3, 6]
offset = [-1, 0, 1]

rounds = open("day2.txt").read().split("\n")

print("2a) Total score by rules for a: " + str(sum(map(lambda rnd: scores[(connection.index(rnd[2]) - connection.index(rnd[0]) + 1) % 3] + (connection.index(rnd[2]) - 3) + 1, rounds))))
print("2b) Total score by rules for b: " + str(sum(map(lambda rnd: scores[connection.index(rnd[2]) - 3] + ((connection.index(rnd[0]) + connection.index(rnd[2]) - 4) % 3) + 1, rounds))))