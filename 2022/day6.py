def a(i,l):
	s=open("6").read()
	return len(s[i:i+l])==len(set(s[i:i+l]))

j,f=0,1
while not a(j,14):
	if a(j,4) and f:
		print(j+4)
		f=0
	j=j+1
print(j+14)