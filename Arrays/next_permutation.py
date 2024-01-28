# Input format: Arr[] = {1,3,2}
# Output: Arr[] = {2,1,3}
# Explanation: All permutations of {1,2,3} are
# {{1,2,3} , {1,3,2}, {2,1,3} , {2,3,1} , {3,1,2} , {3,2,1}}.
# So, the next permutation just after {1,3,2} is {2,1,3}.


def next_per(arr):
    for i in range(len(arr)-1,-1,-1):
        for j in range(i-1,-1,-1):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
                return arr
            else:
                continue

arr = [1,2,3]
print(next_per(arr))

