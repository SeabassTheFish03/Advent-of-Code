def b(o,t,h,f):
	if o<=h:return t>=f or o==h
	return b(h,f,o,t)
a=[int(z) for y in map(lambda w:[i.split("-") for i in w],map(lambda l:l.split(","),open("4").read().split("\n"))) for x in y for z in x]
print(sum(b(*a[i:i+4]) for i in range(0,len(a),4)))