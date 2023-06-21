def print_matr(matrix):
    for line in matrix:
        print(line, end='\n')


def multiply(matr, vect):
    result = []
    for i in range(len(matr[0])):
        total = 0
        for j in range(len(vect)):
            total += vect[j] * matr[j][i]
        result.append(total)
    return result


def matr_by_num(matr, num):
    result = []
    for i in range(len(matr)):
        result.append([])
        for j in range(len(matr)):
            result[i].append(num * matr[i][j])
    return result


def scalar(x, y):
    res = 0
    for i in range(len(x)):
        res += x[i] * y[i]
    return res


diff = lambda x, y: [x[i]-y[i] for i in range(len(x))]


def div(vect, x):
    for i in range(len(vect)):
            vect[i] /= x
    return vect


def inv_matr(matrix):
    inv_matrix = [[0. for i in range(len(matrix))] for j in range(len(matrix))]
    for i in range(len(inv_matrix)):
        inv_matrix[i][i] = 1.

    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            for j in range(i+1, len(matrix)):
                matrix[i], matrix[j] = matrix[j], matrix[i]
                inv_matrix[i], inv_matrix[j] = inv_matrix[j], inv_matrix[i]

    for k in range(len(matrix)):
        temp = matrix[k][k]
        for j in range(len(matrix)):
            if temp != 0:
                matrix[k][j] /= temp
                inv_matrix[k][j] /= temp

        for i in range(k+1, len(matrix)):
            temp = matrix[i][k]
            for j in range(len(matrix)):
                matrix[i][j] -= matrix[k][j] * temp
                inv_matrix[i][j] -= inv_matrix[k][j] * temp

    for k in range(len(matrix)-1, -1, -1):
        for i in range(k-1, -1, -1):
            temp = matrix[i][k]
            for j in range(len(matrix)-1, -1, -1):
                matrix[i][j] -= matrix[k][j] * temp
                inv_matrix[i][j] -= inv_matrix[k][j] * temp

    return inv_matrix
