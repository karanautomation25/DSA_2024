# 1 2 3 5 8 13 21 34 55 89

i = 1
j = 2
num = 5

print(i)
print(j)

count = 0

while count < num:
    temp = i + j
    print(temp)
    count +=1
    i = j
    j = temp
