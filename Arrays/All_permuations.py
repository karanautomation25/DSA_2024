# Input format: Arr[] = {1,3,2}
# Output: Arr[] = {2,1,3}
# Explanation: All permutations of {1,2,3} are
# {{1,2,3} , {1,3,2}, {2,1,3} , {2,3,1} , {3,1,2} , {3,2,1}}. So, the next permutation just after {1,3,2} is {2,1,3}

arr = [1,2,3]
final = []
new = []

for i in range(len(arr)):
    for j in range(len(arr)):
        if i != j:
            for k in range(len(arr)):
                if i!=k and j!=k:
                    final.append(arr[i])
                    final.append(arr[j])
                    final.append(arr[k])
                    if final not in new:
                        new.append(final)
                        final = []

print(new)
