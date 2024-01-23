# https://takeuforward.org/data-structure/maximum-product-subarray-in-an-array/


# Solution:
# https://www.youtube.com/watch?v=hnswaLJvr6g

# Brute force :
# def maxProductSubArray(nums):
#     result = float('-inf')
#     for i in range(len(nums) - 1):
#         for j in range(i + 1, len(nums)):
#             prod = 1
#             for k in range(i, j + 1):
#                 prod *= nums[k]
#             result = max(result, prod)
#     return result
#
# if __name__ == "__main__":
#     nums = [1, 2, -3, 0, -4, -5]
#     print("The maximum product subarray:", maxProductSubArray(nums))


# Optimal approach :




def maxProductSubArray(arr):
    n = len(arr) # size of array.

    pre, suff = 1, 1
    ans = float('-inf')
    for i in range(n):
        if pre == 0:
            pre = 1
        if suff == 0:
            suff = 1
        pre *= arr[i]
        suff *= arr[n - i - 1]
        ans = max(ans, max(pre, suff))
    return ans

arr = [1, 2, -3, 0, -4, -5]
print("The maximum product subarray is:", maxProductSubArray(arr))

