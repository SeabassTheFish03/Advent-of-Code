import re,copy;a,b=open("5").read().split("\n\n")
c=lambda x:list(reversed(x))
e,r=list(map(lambda i:c(list(filter(lambda z:z!=" ",[f[i] for f in list(map(lambda x:[y[1] for y in filter(lambda h:h[0]%4==1,enumerate(x))],a.split("\n")[:-1]))]))),range(9))),"(\d+)(\D{6})(\d)(\D{4})(\d)"
o,m=b.split("\n"),copy.deepcopy(e)
for l in o:
	s=re.search(r, l)
	m[int(s[5])-1] += [m[int(s[3])-1].pop() for _ in range(int(s[1]))]
	e[int(s[5])-1] += c([e[int(s[3])-1].pop() for _ in range(int(s[1]))])
print("".join([v[-1] for v in m]),"".join([w[-1] for w in e]))