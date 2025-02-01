
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

print(matrix)
print("----------------------Matrix-------------------")
#get elements by row
for row in matrix:
    print(row)
#get element one by one
for row in matrix:
    for elem in row:
        print(elem, end=" ")
    print()

#get element in the index
for i in range(len(matrix)):#len(matrix) = 3 row --> 3 floor
    for j in range(len(matrix[i])):#len(matrix[i]) --> get all box in the row
        print(matrix[i][j], end=" ")
    print()


print("----------------------List-------------------")
list = [1,2,3]
for elem in list:
    print(elem, end =" ")

print()
import random
matrix = []
row = 3
col = 4

# for i in range(row):
#     numbers = []
#     for j in range(col):
#         numbers.append(random.randint(20,50))
#     matrix.append(numbers)
for i in range(row):
    matrix.append([random.randint(20,50)  for j in range(col)])

for row in matrix:
    for elem in row:
        print(elem, end=" ")
    print()

summa = 0
for row in matrix:
    summa+= sum(row)
    print(f"Summa elements in row : {sum(row)}")
print(f"Summa = {summa}")