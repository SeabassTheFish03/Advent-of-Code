def a(t):s=list(map(lambda v:set(v),t));return s[0].intersection(*s[1:]).pop()
b=lambda c:(ord(c)>64 and ord(c)<97)*(ord(c)-38)+(ord(c)>96)*(ord(c)-96)
r=open("3").read().split("\n")
print(sum(map(lambda k:b(a((k[:int(len(k)/2)],k[int(len(k)/2):]))),r)),sum(map(lambda g:b(a(g)),[(r[i],r[i+1],r[i+2]) for i in range(0,len(r),3)])))