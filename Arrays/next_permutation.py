# Input format: Arr[] = {1,3,2}
# Output: Arr[] = {2,1,3}
# Explanation: All permutations of {1,2,3} are
# {{1,2,3} , {1,3,2}, {2,1,3} , {2,3,1} , {3,1,2} , {3,2,1}}.
# So, the next permutation just after {1,3,2} is {2,1,3}.


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

