arr = [3,2,1,4]


for i in range(len(arr)-1,-1,-1):
    for j in range(i-1,-1,-1):
        if arr[i] > arr[j]:
            arr[j],arr[i] = arr[i],arr[j]
            res1 = arr[:j+1]
            res2 = sorted(arr[j+1:])
            # res2 = res2[::-1]
            res3 = res1 + res2
            break
    break

print(res3)

