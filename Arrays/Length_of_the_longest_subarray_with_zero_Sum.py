arr = [6, -2, 2, -8, 1, 7, 4, -10]
r = []
for i in range(len(arr)):
    cur = arr[i]
    for j in range(i+1,len(arr)):
        cur = cur+arr[j]
        if cur == 0:
            r.append(len(arr[i:j+1]))

print(max(r))