matrix = []
for i in range(5):
    matrix.append([i])
    for j in range(5):
            matrix.append([j])
print(matrix)

matrix2=[j for j in range(5)for i in range(5)]
print(matrix2) 
