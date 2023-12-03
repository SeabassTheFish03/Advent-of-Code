f = open("2", "r")
input_rounds = f.readlines()
f.close()

# Useful variables for later
connection = "A B C X Y Z".split() # Useful for the modular arithmetic later
score_values = [0, 3, 6] # Loss, draw, and win point values

# We can determine a win or a loss by comparing the indicies of each action, mod 3
# See table A

# Table A
#    X Y Z
#    -----
#  A|d w l
#  B|l d w
#  C|w l d

# If the difference mod 3 is 0, it's a draw
# If the difference mod 3 is 1, it's a win
# If the difference mod 3 is 2, it's a loss

# We can get the score as a result of this by adding 1 mod 3 and multiplying this by 3
# I've decided to do both parts together since they're pretty similar

score_a = 0
score_b = 0
for rnd in input_rounds:
	index_of_elf = connection.index(rnd[0])
	index_of_me = connection.index(rnd[2])

	# Part a
	score_a += ((index_of_me - index_of_elf + 1) % 3)*3 # See above comment. This is win/loss/draw bonus
	score_a += index_of_me - 2 # Since the plays have certain values, these also get added.

	# Part b
	score_b += (index_of_me - 3)*3 # This is simpler because the XYZ now tells me the win/loss/draw.
	score_b += ((index_of_me + index_of_elf - 1) % 3) + 1 # Because what I play is influenced by my win, I have to line both up

print("Score by the rules in part a: " + str(score_a))
print("Score by the rules in part b: " + str(score_b))
