import copy

old_list = [[1,2,3],[4,5,6],[7,8,9]]

new_list = copy.copy(old_list)

new_list[0][2] = 'c'

print(old_list)
print(new_list)

#output : [[1,2,'c'],[4,5,6],[7,8,9]]
#          [[1,2,'c'],[4,5,6],[7,8,9]]


new_list = copy.deepcopy(old_list)

new_list[0][2] = 'c'

print(old_list)
print(new_list)

#output : [[1,2,3],[4,5,6],[7,8,9]]
#          [[1,2,'c'],[4,5,6],[7,8,9]]
