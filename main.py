A = [4, 1, 1, 1, 2, 3, 5]
k = 5

n = len(A)

i = 0
j = 0
sum = 0
max_size = 0
while j < n:
    sum = sum + A[j]
    if sum < k:
        j+=1

    elif sum == k:
        size = (j-1)-i+1
        max_size = max(max_size,size)
        j+=1


    i+=1
    print('hey')

