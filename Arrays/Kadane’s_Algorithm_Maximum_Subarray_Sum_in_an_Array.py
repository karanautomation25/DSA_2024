# https://takeuforward.org/data-structure/kadanes-algorithm-maximum-subarray-sum-in-an-array/

# Input: arr = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

arr = [-2,1,-3,4,-1,2,1,-5,4]
cur = 0
max_sum = 0
for i in range(len(arr)):
    cur += arr[i]
    for j in range(i+1,len(arr)):
        cur+=arr[j]
        if cur > max_sum:
            max_sum = cur

print(max_sum)