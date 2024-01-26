# Count Subarray sum Equals K

# https://takeuforward.org/arrays/count-subarray-sum-equals-k/

# Brute Force Approach :

# arr = [3, 1, 2, 4]
# k = 6
#
# final = []
#
# for i in range(len(arr)):
#     cur = arr[i]
#     for j in range(i+1,len(arr)):
#         cur += arr[j]
#         if cur == k:
#             final.append(arr[i:j+1])
#             continue
#
# print(final)

