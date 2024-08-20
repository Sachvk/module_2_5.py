def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        s = []
        for j in range(m):
            s.append(value)
        matrix.append(s)
    return matrix

result1 = get_matrix(4, 5, 6)
result2 = get_matrix(7, 8, 9)
result3 = get_matrix(10, 11, 12)
print(result1)
print(result2)
print(result3)
