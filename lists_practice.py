
# 1 sum
items = range(1,4)
total = 0
for item in items:
    total = total + item
print("Sum: {}".format(total))


# 2a max
items2 = [8,15,4,3,-2, -18,5,2,9,-3,9]

current_value = items2[0]
for index in range(len(items2)-1):
    if (current_value < items2[index + 1]):
        current_value = items2[index + 1]
print("Max: {}".format(current_value))

# 2b max
# print(max(items2))


# 2c min
current_value = items2[0]
for index in range(len(items2)-1):
    if (current_value > items2[index + 1]):
        current_value = items2[index + 1]
print("Min: {}".format(current_value))


#4 even
list_of_even_numbers = []
for item in items2:
    if (item % 2 == 0):
        list_of_even_numbers.append(item)
print("Even numbers: {}".format(list_of_even_numbers))


#5 Positive/PositiveII(just wants result in a list)
list_greater_than_zero = []
for item in items2:
    if (item > 0):
        list_greater_than_zero.append(item)
print("Greater than zero: {}".format(list_greater_than_zero))


#6 Factor
factor = 5
list_of_factors = []
for item in items2:
    list_of_factors.append("factor of {} = {}".format(item, item*factor))

for item in list_of_factors:
    print(item)


#7 Mutiply Vectors
list1 = [2,4,5]
list2 = [2,3,6]

vector_list = []
for index in range(len(list1)):
    vector_list.append(list1[index] * list2[index])
print("Multiply vectors: {}".format(vector_list))



#8 Matrix Addition
matrix1 = [ [1,3], [2,4] ]
matrix2 = [ [5,2], [1,0] ]

matrix_list_final = []
for i in range(len(matrix1)):
    size = 0
    matrix_list = []
    for ii in range(len(matrix1)):
        matrix_list.append((matrix1[i][ii]) + (matrix2[i][ii]))
        # print(matrix_list)
        
        size = size + 1
        # print(size)
        
        if (size == len(matrix1)):
            matrix_list_final.append(matrix_list)

print(matrix_list_final)



# #8 Matrix Addition (not clean version)
# matrix1 = [ [1,3], [2,4] ]
# matrix2 = [ [5,2], [1,0] ]

# matrix_list_final = []
# for i in range(len(matrix1)):
#     size = 0
#     matrix_list = []
#     for ii in range(len(matrix1)):
#         # matrix_list.append((matrix1[i][ii]) + (matrix2[i][ii]))
#         # print(len(matrix_list))
#         # print((matrix1[i][ii]) + (matrix2[i][ii]))
#         # print(ii)
#         matrix_list.append((matrix1[i][ii]) + (matrix2[i][ii]))
#         # print(matrix_list)
        
#         size = size + 1
#         # print(size)
        
#         if (size == len(matrix1)):
#             matrix_list_final.append(matrix_list)
#             # matrix_list.clear()
        

#     # matrix_list_final.append(matrix_list)


# # print(matrix_list)
# print(matrix_list_final)
#         # print(matrix1[i][ii])
#         # print(matrix2[i][ii])

# # print(matrix_list)


print("")


# 9 Matrix Addition II 
# Extend to work for a pair of matrices of any size, as long as they have the same size.
# Given two-dimensional lists

matrix1a = [ [1,3,1,3], [2,4,2,4] ]
matrix2a = [ [5,2,5,2], [1,0,1,0] ]

# First capture size of list on any one of the inner lists
# For this exercise all inner lists are of the same size
inner_matrix_size = 0
for i in matrix1a[0]:
    inner_matrix_size += 1
print(inner_matrix_size)

matrix_final = []
for i in range(len(matrix1a)):
    size = 0
    matrix_inner = []
    for ii in range(inner_matrix_size):
        matrix_inner.append((matrix1a[i][ii]) + (matrix2a[i][ii]))
        # print(matrix_inner)
        
        size = size + 1
        # print(size)
        
        if (size == len(matrix1a)):
            matrix_final.append(matrix_inner)

print(matrix_final)






