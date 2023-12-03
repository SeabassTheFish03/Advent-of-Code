def a(i,l):
	s=open("6").read()
	return len(s[i-l:i])==len(set(s[i-l:i]))
j,f=14,1
while not a(j,14):
	if a(j,4) and f:print(j);f=0
	j=j+1
print(j)