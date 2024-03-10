s = 'zthtzh'
# s = 'abacb'
d = {}
l=[]
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        if len(s[i:j])%2 == 0:
            l.append(s[i:j])

c=1
vals = []
result = []
for s in l:
    d = {}
    vals = []
    for i in range(len(s)):
        if s[i] in d:
            d[s[i]] +=1
        else:
            d[s[i]] = c

    vals = list(d.values())
    for k in range(len(vals)):
        if vals[k]%2!=0:
            break
        else:
            if k == len(vals)-1:
                result.append(s)
max_val = 0
for val in result:
    max_val = max(len(val),max_val)

print(max_val)
