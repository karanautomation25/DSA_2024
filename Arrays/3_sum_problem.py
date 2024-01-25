# 3 Sum : Find triplets that add up to a zero

# Brute Force
nums = [-1,0,1,2,-1,-4]
final = []

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            cur_sum = nums[i] + nums[j] + nums[k]
            if cur_sum == 0:
                if sorted([nums[i],nums[j],nums[k]]) not in final:
                    final.append(sorted([nums[i],nums[j],nums[k]]))

print(final)