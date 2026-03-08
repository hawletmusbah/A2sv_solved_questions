matrix = []
for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)
# print(matrix)
count = 0
i = 0
while i < 5:
    if 1 in matrix[i]:
        if i  == 2:
            break
        else:
            count += abs( 2 - i) 
            matrix[i] , matrix[2] = matrix[2] , matrix[i]
            break
    else:
        i += 1
# print(matrix)
# print(count)
for j in matrix[2]:
    # print(j)
    if j == 1:
        ind = matrix[2].index(j)
        # print(ind)
        count += abs(2 - ind)  
        break
print(count)